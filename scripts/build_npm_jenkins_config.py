#!/usr/bin/env python3
"""Emit Jenkins flow-definition config.xml wrapping pipelines/npm-project-examples/Jenkinsfile."""
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
GROOVY_PATH = REPO / "pipelines/npm-project-examples/Jenkinsfile"
GROOVY = GROOVY_PATH.read_text(encoding="utf-8")
if "]]>" in GROOVY:
    sys.exit("Jenkinsfile must not contain CDATA terminator ]]>")


def param(name: str, default: str, desc: str) -> str:
    return f"""        <hudson.model.StringParameterDefinition>
          <name>{name}</name>
          <description>{desc}</description>
          <defaultValue>{default}</defaultValue>
          <trim>true</trim>
        </hudson.model.StringParameterDefinition>"""


params_block = "\n".join(
    [
        param(
            "JFROG_SERVER_ID",
            "my-platform",
            "JFrog Platform Server ID (Jenkins → JFrog configuration).",
        ),
        param(
            "JFROG_BUILD_NAME",
            "",
            "Artifactory build-info name. Empty = job short name (JOB_BASE_NAME).",
        ),
        param(
            "NPM_REPO_RESOLVE",
            "npm-virtual",
            "Virtual (or remote) npm repository for dependency resolution.",
        ),
        param(
            "NPM_REPO_DEPLOY",
            "npm-local",
            "Local npm repository for publishing the tarball.",
        ),
        param(
            "NPM_INSTALL_ARGS",
            "",
            "Extra args to pass to npm install only (space-separated), e.g. --omit=dev",
        ),
    ]
)

xml = f"""<?xml version='1.1' encoding='UTF-8'?>
<flow-definition plugin="workflow-job@1571.vb_423c255d6d9">
  <actions/>
  <description>project-examples npm-example: jf npm-config, install, publish, Build Info (env/git), rt build-publish.</description>
  <keepDependencies>false</keepDependencies>
  <properties>
    <hudson.model.ParametersDefinitionProperty>
      <parameterDefinitions>
{params_block}
      </parameterDefinitions>
    </hudson.model.ParametersDefinitionProperty>
  </properties>
  <definition class="org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition" plugin="workflow-cps@4285.v8df38f05c3c5">
    <script><![CDATA[{GROOVY}]]></script>
    <sandbox>true</sandbox>
  </definition>
  <triggers/>
  <disabled>false</disabled>
</flow-definition>
"""
sys.stdout.write(xml)

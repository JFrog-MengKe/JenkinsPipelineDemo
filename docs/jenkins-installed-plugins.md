# 当前 Jenkins 已安装插件

以下列表为控制器 **`$JENKINS_HOME/plugins/*.jpi`** 对应的**插件 ID**（与 **Manage Jenkins → Plugins → Installed** 中的名称一致，含依赖/API 类插件）。**不含版本号。**

**插件数量**：103

| 插件 ID |
|--------|
| ant |
| antisamy-markup-formatter |
| apache-httpcomponents-client-4-api |
| asm-api |
| bootstrap5-api |
| bouncycastle-api |
| branch-api |
| build-timeout |
| caffeine-api |
| checks-api |
| cloudbees-folder |
| commons-lang3-api |
| commons-text-api |
| config-file-provider |
| credentials |
| credentials-binding |
| dark-theme |
| display-url-api |
| durable-task |
| echarts-api |
| eddsa-api |
| email-ext |
| font-awesome-api |
| git |
| git-client |
| github |
| github-api |
| github-branch-source |
| gradle |
| gson-api |
| instance-identity |
| ionicons-api |
| jackson-annotations2-api |
| jackson2-api |
| jackson3-api |
| jakarta-activation-api |
| jakarta-mail-api |
| jakarta-xml-bind-api |
| javadoc |
| javax-activation-api |
| jaxb |
| jfrog |
| jjwt-api |
| joda-time-api |
| jquery3-api |
| jsch |
| json-api |
| json-path-api |
| jsoup |
| junit |
| ldap |
| mailer |
| matrix-auth |
| matrix-project |
| metrics |
| mina-sshd-api-common |
| mina-sshd-api-core |
| nodejs |
| okhttp-api |
| oss-symbols-api |
| pipeline-build-step |
| pipeline-github-lib |
| pipeline-graph-analysis |
| pipeline-graph-view |
| pipeline-groovy-lib |
| pipeline-input-step |
| pipeline-milestone-step |
| pipeline-model-api |
| pipeline-model-definition |
| pipeline-model-extensions |
| pipeline-npm |
| pipeline-rest-api |
| pipeline-stage-step |
| pipeline-stage-tags-metadata |
| pipeline-stage-view |
| plain-credentials |
| plugin-util-api |
| prism-api |
| resource-disposer |
| scm-api |
| script-security |
| snakeyaml-api |
| snakeyaml-engine-api |
| ssh-credentials |
| ssh-slaves |
| structs |
| theme-manager |
| timestamper |
| token-macro |
| trilead-api |
| variant |
| woodstox-core-api |
| workflow-aggregator |
| workflow-api |
| workflow-basic-steps |
| workflow-cps |
| workflow-durable-task-step |
| workflow-job |
| workflow-multibranch |
| workflow-scm-step |
| workflow-step-api |
| workflow-support |
| ws-cleanup |

## 如何更新本文档

在能访问控制器的机器上，列出 `$JENKINS_HOME/plugins/*.jpi` 去掉 `.jpi` 后缀即插件 ID，或从 **Installed** 页复制名称后按字母序整理。安装/升级/卸载插件后请同步更新列表与数量。

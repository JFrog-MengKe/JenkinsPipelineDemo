# JenkinsPipelineDemo

本仓库维护两条 **JFrog CLI + Build Info** 的 Jenkins 脚本式流水线（Maven、npm），以及 **Controller / JFrog / 仓库** 的说明文档与用于生成 `config.xml` 的辅助脚本。

## 目录结构

| 路径 | 说明 |
|------|------|
| `pipelines/maven-project-examples/Jenkinsfile` | Maven：`jf mvn-config` → `jf mvn` → `rt build-collect-env` / `build-add-git` → `rt build-publish` |
| `pipelines/npm-project-examples/Jenkinsfile` | npm：`jf npm-config` → `jf npm install` → enrich → `jf npm publish` → `rt build-publish` |
| `docs/` | Jenkins 插件、JFrog、JDK/npm、仓库与参数说明 |
| `scripts/` | 从 `Jenkinsfile` 生成 `flow-definition` 风格 `config.xml`（便于拷贝到 `$JENKINS_HOME/jobs/<job>/config.xml`） |
| `config/examples/` | 本地生成示例 XML（可选提交到 Git，便于 diff） |

## 文档索引

1. [Controller：插件、JFrog CLI、JDK、npm、Git](docs/controller-setup.md)
2. [Artifactory 仓库与参数对照](docs/jfrog-repositories.md)
3. [流水线参数表](docs/pipeline-parameters.md)

## 生成 Jenkins Job `config.xml`

在仓库根目录执行：

```bash
python3 scripts/build_maven_jenkins_config.py > config/examples/maven-job-config.example.xml
python3 scripts/build_npm_jenkins_config.py   > config/examples/npm-job-config.example.xml
```

将生成的 XML 中 `<script><![CDATA[ ... ]]></script>` 整体可作为 **Pipeline script from SCM** 之外的另一种部署方式：**Freestyle / Pipeline 脚本直接写在任务配置里**。

部署到服务器示例（需 root 或具备写 `JENKINS_HOME` 的权限）：

```bash
sudo cp config/examples/maven-job-config.example.xml /var/lib/jenkins/jobs/project-examples-maven-jfrog/config.xml
sudo chown jenkins:jenkins /var/lib/jenkins/jobs/project-examples-maven-jfrog/config.xml
```

然后 **Reload configuration from disk** 或在 UI 中保存任务。

## 源码与分支

示例检出地址默认为 **`https://github.com/JFrog-MengKe/project-examples`**，可按需在各自 `Jenkinsfile` 中改为官方 `jfrog/project-examples` 或其他 fork。

## 维护约定

- 调整流水线逻辑时，只改对应目录下的 `Jenkinsfile`，再重新运行 `scripts/build_*.py` 更新示例 XML。
- 默认参数（仓库 Key、Server ID）仅为占位，**以各环境 Artifactory / Jenkins 实际配置为准**。

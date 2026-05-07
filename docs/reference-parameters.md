# 参数速查

创建 Pipeline 任务时，**参数名称**须与下表一致（区分大小写），以便与 `Jenkinsfile` 中的 `params.*` 对应。

## Maven 流水线（`pipelines/maven-project-examples/Jenkinsfile`）

在任务配置中勾选 **Parameterize this project**，添加 **String Parameter**：

| 参数名 | 示例默认值 | 说明 |
|--------|------------|------|
| `JFROG_SERVER_ID` | `my-platform` | 与 **Manage Jenkins → System → JFrog** 中的 **Server ID** 完全一致 |
| `JFROG_BUILD_NAME` | （留空） | 留空时使用 Jenkins 的 `JOB_BASE_NAME` 作为 Artifactory Build Info 名称 |
| `RESOLVE_RELEASES` | `libs-release` | Maven 解析 Release 所用仓库 Key |
| `RESOLVE_SNAPSHOTS` | `libs-snapshot` | Maven 解析 Snapshot 所用仓库 Key |
| `DEPLOY_RELEASES` | `libs-release-local` | 部署 Release 的 Maven Local 仓库 Key |
| `DEPLOY_SNAPSHOTS` | `libs-snapshot-local` | 部署 Snapshot 的 Maven Local 仓库 Key |
| `MVN_GOALS` | `install` | 传给 `jf mvn` 的目标，多个目标用空格，如 `clean install` |

构建编号使用 Jenkins 内置 **`BUILD_NUMBER`**，并传给 `jf rt build-*`。

---

## npm 流水线（`pipelines/npm-project-examples/Jenkinsfile`）

| 参数名 | 示例默认值 | 说明 |
|--------|------------|------|
| `JFROG_SERVER_ID` | `my-platform` | 同上 |
| `JFROG_BUILD_NAME` | （留空） | 同上 |
| `NPM_REPO_RESOLVE` | `npm-virtual` | `jf npm-config --repo-resolve`，通常为 Virtual |
| `NPM_REPO_DEPLOY` | `npm-local` | `jf npm-config --repo-deploy`，通常为 Local |
| `NPM_INSTALL_ARGS` | （留空） | 额外传给 `npm install` 的参数，空格分隔，如 `--omit=dev` |

---

## 与脚本生成 XML 的默认值

运行 `scripts/build_maven_jenkins_config.py` / `build_npm_jenkins_config.py` 时，XML 内嵌的 **默认参数值** 可能与上表示例不同（仅为占位）。以你在 Jenkins UI 中为任务配置的默认值为准，或直接修改 Python 脚本中的 `default` 字符串与团队规范对齐。

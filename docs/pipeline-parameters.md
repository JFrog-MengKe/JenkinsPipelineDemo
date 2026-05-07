# 流水线参数说明

## Maven（`pipelines/maven-project-examples/Jenkinsfile`）

| 参数 | 说明 |
|------|------|
| `JFROG_SERVER_ID` | Jenkins 中配置的 JFrog Platform Server ID |
| `JFROG_BUILD_NAME` | 留空时使用 `JOB_BASE_NAME`；否则为 Artifactory Build Info 名称 |
| `RESOLVE_RELEASES` | Maven 解析 Release 仓库 Key |
| `RESOLVE_SNAPSHOTS` | Maven 解析 Snapshot 仓库 Key |
| `DEPLOY_RELEASES` | Maven 部署 Release 仓库 Key |
| `DEPLOY_SNAPSHOTS` | Maven 部署 Snapshot 仓库 Key |
| `MVN_GOALS` | 传给 `jf mvn` 的目标，如 `install`、`clean deploy` |

构建编号使用 Jenkins **`BUILD_NUMBER`**，与 `jf rt build-*` 一致。

## npm（`pipelines/npm-project-examples/Jenkinsfile`）

| 参数 | 说明 |
|------|------|
| `JFROG_SERVER_ID` | 同上 |
| `JFROG_BUILD_NAME` | 同上 |
| `NPM_REPO_RESOLVE` | `jf npm-config --repo-resolve` |
| `NPM_REPO_DEPLOY` | `jf npm-config --repo-deploy` |
| `NPM_INSTALL_ARGS` | 额外传给 `npm install` 的参数（空格分隔），如 `--omit=dev` |

## 可选阶段：`jf bs`

两条流水线均包含 **Security Check**（`jf bs`）。若未启用 JFrog Advanced Security / 许可不足，该阶段可能失败；可在 `Jenkinsfile` 中删除对应 `stage`。

# JFrog Artifactory：与本流水线相关的仓库

以下为概念对照；实际 **仓库 Key** 以你在 Artifactory 中创建的为准，并与 Jenkins 任务参数一致。

## Maven（`project-examples-maven-jfrog`）

| 参数名 | 典型用途 |
|--------|-----------|
| `RESOLVE_RELEASES` | 解析 **Release** 依赖（常为 Maven virtual，聚合 libs-release + remotes） |
| `RESOLVE_SNAPSHOTS` | 解析 **Snapshot** 依赖 |
| `DEPLOY_RELEASES` | 将 Release 构件部署到的 **Maven local** |
| `DEPLOY_SNAPSHOTS` | 将 Snapshot 构件部署到的 **Maven local** |

流水线命令等价于：

1. `jf mvn-config --server-id-resolve/deploy … --repo-resolve-releases … --repo-deploy-releases …`
2. `jf mvn <goals>`
3. `jf rt build-collect-env` / `build-add-git` / `build-publish`

Build Name / Number 与 `JFROG_BUILD_NAME`、`BUILD_NUMBER` 对齐。

## npm（`project-examples-npm-jfrog`）

官方示例流程见 [project-examples npm-example README](https://github.com/jfrog/project-examples/blob/master/npm-example/README.md)。

| 参数名 | 典型用途 |
|--------|-----------|
| `NPM_REPO_RESOLVE` | **Virtual**（或 remote）npm，用于 `jf npm install` 解析依赖 |
| `NPM_REPO_DEPLOY` | **Local** npm，用于 `jf npm publish` 上传包 |

推荐在 Artifactory 中：

1. 创建 **Remote npm**（上游 `https://registry.npmjs.org`）。
2. 创建 **Local npm**（部署目标）。
3. 创建 **Virtual npm**，包含上述 remote + local，并设置 **Default Deployment Repository** 为 local。
4. 将 Virtual 的 Key 填给 `NPM_REPO_RESOLVE`；将 Local 的 Key 填给 `NPM_REPO_DEPLOY`（或与文档示例一致：解析与发布均指向配置好的 virtual / local 组合）。

## Server ID

`JFROG_SERVER_ID` 必须与 Jenkins **JFrog 配置**中的实例 ID 一致，否则 `jf` 无法解析凭据与 URL。

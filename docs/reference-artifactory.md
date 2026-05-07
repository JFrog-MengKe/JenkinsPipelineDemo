# Artifactory 仓库要点（参考）

流水线本身只使用 **仓库 Key**（字符串）；请在 Artifactory 管理员控制台创建并与 Jenkins 任务参数一致。

## Maven

典型布置：

- **Remote**：代理 Maven Central（或你们私服）。
- **Local**：`libs-release-local`、`libs-snapshot-local`（名称自定）。
- **Virtual**：聚合 Remote + Local，供 **`jf mvn-config` 的 `--repo-resolve-releases/snapshots`** 使用；部署目标使用 **`--repo-deploy-releases/snapshots`** 指向对应 Local。

参数 **`RESOLVE_*`** / **`DEPLOY_*`** 必须与 Artifactory 中 **Repository Key** 一致。

---

## npm

参考 JFrog 官方示例：[project-examples npm-example README](https://github.com/jfrog/project-examples/blob/master/npm-example/README.md)。

常见布置：

1. **Remote npm**：上游 `https://registry.npmjs.org`。
2. **Local npm**：存放发布的包。
3. **Virtual npm**：包含上述 Remote 与 Local；配置 **Default Deployment Repository** 指向 Local。

- **`NPM_REPO_RESOLVE`**：通常填用于安装的 **Virtual**（也可按你们策略填 Remote）。
- **`NPM_REPO_DEPLOY`**：填用于 **`jf npm publish`** 的 **Local**（或与文档一致的 Virtual，前提是默认部署仓库已设好）。

---

## Server ID

`JFROG_SERVER_ID` 仅标识 Jenkins 中已配置的 **JFrog 实例**，与仓库 Key 无关；错误会导致 `jf` 无法解析凭据或 URL。

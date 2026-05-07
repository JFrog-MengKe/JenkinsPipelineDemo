# npm：`project-examples` → `npm-example`

- 入口：`Jenkinsfile`。
- 流程遵循 JFrog [npm-example README](https://github.com/jfrog/project-examples/blob/master/npm-example/README.md)：install → 收集 env/git → publish → `rt build-publish`。
- Agent 必须安装 **Node.js** 与 **npm**（`jf npm` 会调用系统 npm）。
- 仓库参数见根目录 `docs/jfrog-repositories.md`。

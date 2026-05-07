# Jenkins + JFrog 流水线模板

本仓库是一份**可照抄的模板**：使用者按文档顺序完成 **Jenkins 配置**与**两条脚本式流水线**（Maven、npm），在 Artifactory 中收集依赖与 Build Info 并发布。

聚焦内容：**Jenkins 插件与全局工具、JFrog 连接、Agent 软件、流水线脚本与任务参数**。

---

## 从这里开始

| 顺序 | 文档 | 说明 |
|------|------|------|
| 1 | [**分步操作指南**](docs/step-by-step.md) | 从安装插件到创建两条 Pipeline 任务（含粘贴 `Jenkinsfile` 或使用 SCM） |
| 2 | [参数速查](docs/reference-parameters.md) | 任务参数与 `Jenkinsfile` 对应关系 |
| 3 | [Artifactory 仓库要点](docs/reference-artifactory.md) | Maven/npm 仓库类型与命名提示 |
| — | [已安装插件清单](docs/jenkins-installed-plugins.md) | 当前控制器已装插件 ID 列表（快照，可随环境更新） |

---

## 仓库结构

```text
pipelines/
  maven-project-examples/Jenkinsfile    # Maven + JFrog CLI
  npm-project-examples/Jenkinsfile      # npm + JFrog CLI
scripts/
  build_maven_jenkins_config.py         # 可选：由 Jenkinsfile 生成 config.xml
  build_npm_jenkins_config.py
docs/
  step-by-step.md                       # ★ 主指南
  reference-parameters.md
  reference-artifactory.md
  jenkins-installed-plugins.md          # 已装插件清单（快照）
```

---

## 流水线做的事（摘要）

- **Maven**：`jf mvn-config` → `jf mvn` → `jf rt build-collect-env` / `build-add-git` → `jf rt build-publish`（可选 `jf bs`）。
- **npm**：`jf npm-config` → `jf npm install` → enrich → `jf npm publish` → `jf rt build-publish`（可选 `jf bs`）。

示例源码默认检出 [jfrog/project-examples](https://github.com/jfrog/project-examples)（可在各 `Jenkinsfile` 中修改）。

---

## 可选：生成 Jenkins `config.xml`

将脚本输出重定向到任意文件后，拷贝到 `$JENKINS_HOME/jobs/<任务名>/config.xml`，再 **Reload configuration from disk**。详见 [分步指南 · 步骤 9](docs/step-by-step.md)。

```bash
python3 scripts/build_maven_jenkins_config.py > maven-job.xml
python3 scripts/build_npm_jenkins_config.py   > npm-job.xml
```

---

## 维护约定

- 改流水线逻辑 → 只编辑对应目录下的 `Jenkinsfile`，必要时同步更新 `docs/reference-parameters.md`。
- 默认参数中的仓库 Key、Server ID 仅为占位，**必须以实际 Artifactory / Jenkins 为准**。

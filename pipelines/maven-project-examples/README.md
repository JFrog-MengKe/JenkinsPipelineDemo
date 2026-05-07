# Maven：`project-examples` → `maven-examples/maven-example`

- 入口：`Jenkinsfile`（脚本式 Pipeline）。
- 使用 **Maven Wrapper**（`./mvnw`），`jf mvn-config` 含 `--use-wrapper`。
- 构建信息：`JFROG_BUILD_NAME` / `BUILD_NUMBER` 与 `jf rt build-*` 一致。
- 详细依赖与插件见仓库根目录 `docs/`。

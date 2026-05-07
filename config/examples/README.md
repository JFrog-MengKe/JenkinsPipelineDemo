# 示例 `config.xml`

由脚本生成，仅作备份与评审；**插件版本号**（`workflow-job@…`、`workflow-cps@…`）可能与你服务器不一致，部署时可保留服务器原有 plugin 属性或升级插件以对齐。

生成命令（在仓库根目录）：

```bash
python3 scripts/build_maven_jenkins_config.py > config/examples/maven-job-config.example.xml
python3 scripts/build_npm_jenkins_config.py   > config/examples/npm-job-config.example.xml
```

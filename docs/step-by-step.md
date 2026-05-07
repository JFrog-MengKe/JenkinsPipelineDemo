# 分步操作指南：从零到两条 JFrog 流水线

按下列顺序执行即可完成 **Maven** 与 **npm** 两条流水线。假设你已有一台可登录的 Jenkins（任意部署方式），以及可访问的 **JFrog Artifactory**（与 Jenkins 网络互通）。

---

## 步骤 0：确认目标

完成后你将拥有：

1. Jenkins 已安装 **Pipeline、Git、JFrog** 插件，并已配置 **JFrog Platform** 与 **JFrog CLI** 全局工具。
2. 运行流水线的 Agent（可与 Jenkins Controller 同一台机器）已安装 **Git、JDK 8、Node.js + npm**（Maven 示例使用项目内 **Maven Wrapper**，不要求全局 `mvn`）。
3. Artifactory 上已准备好 Maven / npm 仓库（或已知仓库 **Key**）。
4. 两个 **Pipeline 类型任务**，分别运行本仓库中的 Maven / npm `Jenkinsfile`。

附录：[参数速查](reference-parameters.md)、[Artifactory 仓库要点](reference-artifactory.md)。

---

## 步骤 1：安装 Jenkins 插件

以管理员登录 Jenkins：**Manage Jenkins → Plugins → Available plugins**，安装并重启：

| 插件 | 说明 |
|------|------|
| **Pipeline**（含 Workflow: CPS / Aggregator 等） | 运行 Pipeline |
| **Git** | 流水线中的 `git 'https://...'` |
| **JFrog**（Jenkins JFrog Plugin，提供 Pipeline 中的 `jf` 步骤） | 调用 `jf mvn` / `jf npm` / `jf rt …` |

安装完成后重启 Jenkins（若提示）。

---

## 步骤 2：在 Jenkins 中连接 JFrog Platform

1. 在 JFrog Platform 为用户生成 **Access Token**（推荐）或准备用户名密码。
2. Jenkins：**Manage Jenkins → System**，找到 **JFrog**（名称随插件版本可能为 “JFrog Platform” / “Artifactory” 配置区）。
3. 新增实例：**Platform URL**、**凭据**，并为该实例设置 **Server ID**（例如 `my-platform`，记下来）。
4. 使用界面上的 **Test connection** 确认成功。

流水线参数 **`JFROG_SERVER_ID`** 必须与这里的 **Server ID 字符串完全一致**。

---

## 步骤 3：配置全局工具「JFrog CLI」

两条流水线均包含：

```groovy
env.JFROG_BINARY_PATH = tool 'jfrog-cli'
```

因此必须在 Jenkins 注册名为 **`jfrog-cli`** 的工具：

**Manage Jenkins → Tools** → **JFrog CLI installations**（名称以实际插件为准）

- **Name**：填 **`jfrog-cli`**（与脚本中一致）。
- 选择自动从 **JFrog 官方发行地址**安装，或指向已在 Agent 上解压的 `jf` 可执行文件路径。

保存后，确认构建用户对该路径有执行权限。

---

## 步骤 4：准备 Agent 操作系统依赖

流水线默认在 **同一个 Jenkins Agent** 上执行（未单独指定 `agent { label '…' }`，等价于 **任意可用 Agent / controller**）。在**实际执行构建的机器**上安装：

### 4.1 Git

用于从 GitHub 克隆示例仓库。

```bash
# Debian/Ubuntu 示例
sudo apt-get update && sudo apt-get install -y git
```

### 4.2 Maven 流水线：JDK 8

`pipelines/maven-project-examples/Jenkinsfile` 中写死了：

```text
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
PATH+JDK8=/usr/lib/jvm/java-8-openjdk-amd64/bin
```

安装示例（路径需与脚本一致，否则请修改 `Jenkinsfile`）：

```bash
sudo apt-get install -y openjdk-8-jdk-headless
```

### 4.3 Maven 流水线：Maven Wrapper

示例工程使用 **`./mvnw`**，脚本已使用 `jf mvn-config … --use-wrapper`。若检出后无法执行，可在 `Jenkinsfile` 的 `dir('maven-examples/maven-example')` 内第一行增加：

```groovy
sh 'chmod +x mvnw || true'
```

### 4.4 npm 流水线：Node.js 与 npm

```bash
sudo apt-get install -y nodejs npm
```

确认 **`jenkins`（或你的构建用户）** 下执行 `node -v`、`npm -v` 正常。

---

## 步骤 5：在 Artifactory 准备仓库（概要）

你需要知道各仓库在 Artifactory 中的 **Repository Key**（创建仓库时在界面中设置）。

- **Maven**：至少一组用于 **解析** 的 Virtual（或 Remote + Virtual），以及用于 **部署** 的 Maven **Local**（release/snapshot 策略按团队规范）。
- **npm**：Remote npm（上游 npmjs）、Local npm、Virtual npm（聚合二者并配置默认部署仓库）。

详细说明见 [reference-artifactory.md](reference-artifactory.md)。

---

## 步骤 6：创建 Maven Pipeline 任务

1. **New Item** → 输入名称（例如 `project-examples-maven-jfrog`）→ 选择 **Pipeline** → OK。
2. 勾选 **This project is parameterized**，添加 **String Parameter**（名称与默认值见 [reference-parameters.md](reference-parameters.md) 中 Maven 表）。默认值可按你的 Artifactory 修改。
3. **Pipeline** 区域：
   - **Definition**：**Pipeline script**，将仓库中 `pipelines/maven-project-examples/Jenkinsfile` **全文粘贴**；  
     **或** 选择 **Pipeline script from SCM**，填写本仓库 Git 地址，`Script Path` 填 `pipelines/maven-project-examples/Jenkinsfile`。
4. 保存。

首次构建选择 **Build with Parameters**，确认 `JFROG_SERVER_ID` 与步骤 2 一致，仓库参数与实际 Key 一致。

---

## 步骤 7：创建 npm Pipeline 任务

1. 同上新建 **Pipeline** 任务（名称示例：`project-examples-npm-jfrog`）。
2. 添加 **String Parameter**（见 [reference-parameters.md](reference-parameters.md) npm 表）。
3. 粘贴 `pipelines/npm-project-examples/Jenkinsfile` 或配置 SCM 同上，`Script Path`：`pipelines/npm-project-examples/Jenkinsfile`。
4. 保存并以参数构建。

---

## 步骤 8：可选阶段「Security Check」说明

两条脚本末尾含 `jf 'bs'`（JFrog 安全扫描）。若平台未授权或未启用相关能力，该阶段可能失败；可在对应 `Jenkinsfile` 中删除 **Security Check** 整个 `stage`。

---

## 步骤 9（可选）：用脚本生成 `config.xml` 下发任务

适合已在服务器上维护 `$JENKINS_HOME`、希望通过文件导入任务的场景。

在克隆本仓库的机器上：

```bash
python3 scripts/build_maven_jenkins_config.py > maven-job.xml
python3 scripts/build_npm_jenkins_config.py   > npm-job.xml
```

将生成的 XML 拷贝到：

```text
$JENKINS_HOME/jobs/<任务名>/config.xml
```

并将所有者设为 Jenkins 进程用户，然后在 Jenkins：**Manage Jenkins → Reload Configuration from Disk**。

XML 中的插件版本号（`workflow-job@…`）可能与你环境不一致；如遇兼容性告警，可在 Jenkins UI 中打开任务一次并保存，由 Jenkins 自动改写插件版本字段。

---

## 步骤 10：Jenkins URL（避免登录后跳转异常）

**Manage Jenkins → System → Jenkins Location**，将 **Jenkins URL** 设为用户在浏览器中实际访问的根地址（例如 `http://jenkins.example.com:8080/`），避免 OAuth 或反向代理场景下重定向错误。这与流水线脚本本身无关，但常见于首次部署。

---

以上完成后，两条流水线应能分别完成 **编译/安装依赖、上传构件、在 Artifactory 中查看 Build Info**。若某步报错，根据控制台日志中 **`jf`** 或 **`npm`/`java`** 的输出对照本指南相应章节排查。

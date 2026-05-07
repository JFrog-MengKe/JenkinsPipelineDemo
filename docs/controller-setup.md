# Jenkins Controller：插件与运行环境

本文说明运行本仓库两条流水线所需的 **Jenkins 插件**、**JFrog CLI 工具链**、以及 **Agent / Controller 上的系统依赖**（Maven、JDK、npm）。版本号会随环境变化，请以你当前 Jenkins 与发行版为准。

## 1. 必需 Jenkins 插件

| 插件 | 用途 |
|------|------|
| **Pipeline**（Workflow: CPS、Workflow: Aggregator 等） | 运行 `Jenkinsfile` / 脚本式流水线 |
| **Git** | `git 'https://...'` 检出源码 |
| **JFrog**（`jenkins-jfrog-plugin`，提供 `jf` Pipeline 步骤） | 调用 `jf mvn` / `jf npm` / `jf rt …` |
| （可选）**Credentials** | 若凭据绑定到 JFrog Server ID |

安装路径：**Manage Jenkins → Plugins → Available plugins**，搜索上述名称安装并重启 Jenkins。

## 2. JFrog Platform 与 Jenkins 绑定

1. 在 JFrog Platform（Artifactory）创建 **Access Token** 或使用用户名密码（推荐 Token）。
2. Jenkins：**Manage Jenkins → System → JFrog**，添加 **Platform instance / Server ID**（例如 `soleng`），填入 URL 与凭据，**Test connection** 成功。
3. 流水线中的 **`JFROG_SERVER_ID`** 参数必须与这里的 **Server ID** 字符串完全一致。

CLI 在构建时会使用 Jenkins 为该 Server ID 注入的配置（等价于本机执行 `jf config`）。

## 3. JFrog CLI 作为全局工具（`tool 'jfrog-cli'`）

流水线使用：

```groovy
env.JFROG_BINARY_PATH = tool 'jfrog-cli'
```

因此必须在 Jenkins 中注册名为 **`jfrog-cli`** 的工具：

**Manage Jenkins → Tools → JFrog CLI installations**

- Name：`jfrog-cli`（与脚本中一致）
- Installer：从 **releases.jfrog.io** 自动安装，或手动指定已下载的 `jf` 路径

确保 **`jenkins`** 用户对安装路径可读可执行。

## 4. Agent 系统依赖（Ubuntu 示例）

### 4.1 Git

```bash
sudo apt-get update && sudo apt-get install -y git
```

### 4.2 Maven 流水线：JDK 8 与路径

脚本使用：

```text
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
PATH+JDK8=/usr/lib/jvm/java-8-openjdk-amd64/bin
```

安装示例：

```bash
sudo apt-get install -y openjdk-8-jdk-headless
```

若 JDK 安装路径不同，请同步修改 `pipelines/maven-project-examples/Jenkinsfile` 中的 `JAVA_HOME` / `PATH+JDK8`。

### 4.3 Maven 流水线：Maven Wrapper

示例仓库使用 **`mvnw`**，`jf mvn-config` 已加 **`--use-wrapper`**，无需全局 `mvn`，但需 Wrapper 可执行：

```bash
chmod +x mvnw
```

（流水线可在检出后增加 `sh 'chmod +x mvnw'`，当前示例依赖仓库内权限。）

### 4.4 npm 流水线：Node.js 与 npm

```bash
sudo apt-get install -y nodejs npm
```

要求：`npm -v`、在 **`jenkins` 用户** 下可调用（用于 `jf npm` 调起的 npm）。

## 5. systemd 与 Jenkins（可选经验）

若在 `/etc/systemd/system/jenkins.service.d/` 下覆盖环境变量，必须使用 systemd 允许的语法，例如：

```ini
[Service]
Environment="JAVA_OPTS=-Djava.awt.headless=true -other.flag=value"
```

一行内多个 JVM 参数需写在 **同一对引号** 内。重复的 `JAVA_ARGS` / `JAVA_OPTS` 可与发行版自带的 `/etc/default/jenkins` 冲突，合并前请备份。

## 6. OrbStack / 本机访问（可选）

若 Jenkins 跑在 OrbStack 虚拟机中，Mac 浏览器通常使用 **`http://127.0.0.1:8080/`** 访问（由 OrbStack 转发）。以 `Manage Jenkins → System` 中的 **Jenkins URL** 为准，避免登录后重定向错误。

## 7. Artifactory 仓库准备（概要）

- **Maven**：需要可用于解析的 virtual（或 remote+virtual），以及用于部署的 **Maven local**（releases/snapshots 按平台策略配置）。仓库 **Key** 必须与任务参数 `RESOLVE_*` / `DEPLOY_*` 一致。
- **npm**：需要 **npm virtual**（解析）、**npm local**（发布），虚拟仓库需聚合 remote npm 与 local，并设置默认部署仓库。详见 `jfrog-repositories.md`。

安装完成后，用流水线参数指向真实仓库 Key；默认值仅为占位，需按环境修改。

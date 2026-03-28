# Node.js和git
检查 Node.js 是否安装
```bash
node -v
#-v显示版本号
#node：运行 JS 的引擎（主角）
```
检查 npm 是否配套安装
```bash
npm -v
#npm：包管理器（配角，负责装库）
```
检查 Git 是否安装
```bash
git --version
#`-v` = verbose（详细输出）
#`-version` = 查看版本号
- `-v` 小写：Git 里是详细模式
- `-V` 大写：Git 里是版本号
- `--version`：所有工具通用，最安全
```
## 一、为什么必须装 Node.js？（核心运行引擎）
OpenClaw 本身就是用 **Node.js + JavaScript/TypeScript** 写的。

- **Node.js = 运行环境**：没有它，龙虾的代码根本跑不起来。
- **npm = 包管理器**：装 Node 时自动带 npm，用来一键安装龙虾需要的所有依赖库（比如网络、文件、系统控制模块）。
- **版本要求**：必须 ≥ v22.0.0，版本低了直接报错。

一句话：**Node.js 是龙虾的 “发动机”，没它转不起来**
## 二、为什么必须装 Git？（代码搬运工）

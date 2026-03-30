# CMD执行
## 创建一个code文件夹和一个openclaw文件夹，并进入
```bash
mkdir D:\code  #mkdir 是创建文件夹指令
mkdir D:\code\openclaw 
D：#是进入指定磁盘
cd D:\code\openclaw
```
## 克隆openclaw源码并进入项目目录
```bash
git clone https://github.com/openclaw/openclaw.git #clone克隆
cd openclaw
```
## 安装依赖和全局安装openclaw命令
```bash
npm install
npm install -g . #-g是全局安装,.是当前所在文件夹
```
> [!note]- npm install做了什么
> ![[解释#`npm install` 做了什么]]
## 安装 pnpm（OpenClaw 官方推荐用 pnpm 管理依赖）
```bash
npm install -g pnpm
```
## 安装依赖 + 执行构建（关键一步）
```powershell
pnpm install && pnpm build
```
### 💡 补充说明
为什么用 `pnpm`？OpenClaw 项目的依赖管理是基于 pnpm 的，用 npm 直接安装可能会导致依赖缺失或构建失败。
还会遇到一个问题就是在用pump build指令的时候可能会提示在调用bash的时候调用失败是因为电脑没有安装着bash，需要用
```bash
winget install --id Git.Git -e --source winget
#因为在linux和ios操作系统会自带bash但是windows需要额外安装
```
## 把openclaw链接到全局并且验证安装是否成功
```bash
npm install -g .
openclaw --version
```
#  ls命令 - 列出目录内容
### 中文翻译

- **命令名**：`ls`
- **中文含义**：列出目录内容（list directory contents）
- **音标标注**：/ɛl ɛs/ （分别读字母"L"和"S"的音）

### 核心用途

查看当前目录下有哪些文件和文件夹。

### 为什么需要这个命令？

- Linux服务器通常没有图形界面，必须用命令查看文件
- 快速确认文件是否存在、文件数量、文件名
- 是几乎所有文件操作的第一步（先查看，再操作）
### 最小命令示例
```bash
# 查看当前目录下的所有文件和文件夹
ls

# 查看指定目录的内容（如data目录）
ls data/

# 查看详细信息（显示文件大小、权限、修改时间）
ls -l

# 按文件大小排序显示
ls -lS
```
>命令参数说明
- `ls`：最基本形式，只显示文件名
- `ls -l`：`-l`是"long listing"的缩写，显示详细信息
- `ls -S`：`-S`按文件大小排序（大写S）
- `ls data/`：查看`data/`目录的内容
# cat命令 - 查看文件内容
### 中文翻译
- **命令名**：`cat`
- **中文含义**：连接文件并打印到标准输出（concatenate and print）
- **音标标注**：/kæt/ （与英文单词"cat"（猫）同音）
### 核心用途

查看文本文件的内容，适合快速检查小文件。
### 为什么需要这个命令？

- 需要确认文件内容是否正确
- 查看配置文件、日志文件、数据文件
- 比用编辑器打开更快速
### 最小命令示例
```bash
# 查看整个文件内容（如果文件很大，会刷屏）
cat data/movies_sample.csv
# 查看文件前几行（结合head命令）
cat data/movies_sample.csv | head -5
# 查看文件后几行（结合tail命令）
cat data/movies_sample.csv | tail -3
```
### 管道符号|说明

- **符号**：`|`（竖线，通常位于回车键上方）
- **中文**：管道
- **音标**：/paɪp/
- **用途**：将一个命令的输出作为另一个命令的输入
- **示例**：`cat 文件 | head -5` = 先读取文件，然后取前5行显示
# 文件路径概念
### 核心概念
- **文件路径**（file path）：文件在文件系统中的位置
- **中文**：文件路径
- **音标**：/faɪl pæθ/
### 两种路径类型
#### 1. 绝对路径（Absolute Path）
- **中文**：绝对路径
- **音标**：/ˈæbsəluːt pæθ/
- **定义**：从根目录`/`开始的完整路径
- **示例**：`/home/user/data/movies_sample.csv`
- **特点**：无论当前在哪，都指向同一个文件
#### 2. 相对路径（Relative Path）
- **中文**：相对路径
- **音标**：/ˈrɛlətɪv pæθ/
- **定义**：相对于当前目录的路径
- **特殊符号**：
    - `.`：当前目录（dot）
    - `..`：上级目录（dot dot）
    - `~`：用户家目录（tilde）
- **示例**：
    - `./data/movies_sample.csv`：当前目录下的data子目录
    - `../project/data/`：上级目录中的project/data目录
### 为什么需要理解路径？
- 准确指定文件位置，避免"文件找不到"错误
- 在脚本和程序中使用正确路径
- 理解文件系统结构
### 相关命令示例
```bash
# 查看当前目录（print working directory）
# pwd /piː dʌbəl juː diː/
pwd

# 切换目录（change directory）
# cd /siː diː/
cd data/          # 进入data目录
cd ..             # 返回上级目录
cd ~              # 回到家目录

# 用相对路径查看文件
cat ./data/movies_sample.csv  # 从当前目录开始
cat ../data/movies_sample.csv # 从上级目录开始
```
# `wc` 命令的全称是 **word count**（单词计数）
它最初是用来统计文本的**单词数**，现在也可以统计：

- `-l`：行数（line count）
- `-w`：单词数（word count）
- `-c`：字节数（byte count）
- `-m`：字符数（character count）
- ```bash
# 1. 统计movies_sample.csv有多少行
# wc /dʌbəl juː siː/ word count（单词统计）
# -l 参数表示统计行数（line）
wc -l data/movies_sample.csv

# 2. 查看文件大小（human readable格式）
# -h 参数表示人类可读（human-readable）
ls -lh data/movies_sample.csv
```
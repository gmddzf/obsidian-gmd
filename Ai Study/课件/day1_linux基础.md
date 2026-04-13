# 第一周 Day 1：Linux文件系统基础

**今天目标**：熟悉Linux的目录结构，掌握基本文件操作命令

---

## 一、Linux目录结构是什么？

**想象你的电脑是一个大房子**：

| 目录 | 相当于 | 里面放什么 |
|------|--------|-----------|
| / | 房子本身 | 根目录，所有文件的起点 |
| /home | 卧室 | 用户的个人文件（你的文档、下载等） |
| /etc | 保险柜 | 系统配置文件（密码本、设置） |
| /var | 杂物间 | 日志文件、临时数据 |
| /usr | 书房 | 安装的软件和程序 |
| /root | 老板的卧室 | 超级管理员的家目录 |
| /tmp | 垃圾桶 | 临时文件，重启后清空 |

**记住这个路径**：`/home/你的用户名/` 就是你登录后默认在的地方

---

## 二、基本文件操作命令

### 1. 查看你在哪里：pwd

```bash
pwd
```

**输出示例**：`/home/zhangsan`

**意思**：打印当前工作目录，告诉你"我在哪"

---

### 2. 查看当前目录有什么：ls

```bash
ls          # 简单列出文件名
ls -l       # 详细信息（权限、大小、时间）
ls -a       # 显示隐藏文件（以.开头的）
ls -lh      # 人性化显示大小（KB、MB）
```

**常用组合**：`ls -lah` = 详细 + 隐藏 + 人性化

---

### 3. 进入目录：cd

```bash
cd Documents      # 进入当前目录下的Documents文件夹
cd /home/user     # 进入指定路径
cd ..             # 返回上一级目录
cd ~              # 回到你的家目录
cd -              # 回到上一次所在的目录
```

**技巧**：
- 输入目录名前几个字母，按 `Tab` 键自动补全
- 路径用 `/` 分隔，不要用 `\`

---

### 4. 创建目录：mkdir

```bash
mkdir myfolder              # 创建一个文件夹
mkdir -p a/b/c              # 创建多级目录（a里面套b，b里面套c）
```

---

### 5. 创建空文件：touch

```bash
touch newfile.txt           # 创建一个空文件
touch file1 file2 file3     # 同时创建多个文件
```

---

### 6. 复制文件：cp

```bash
cp file.txt backup.txt      # 复制文件，新名字叫backup.txt
cp file.txt /home/user/     # 复制到指定目录
cp -r folder1 folder2       # 复制整个文件夹（-r表示递归）
```

---

### 7. 移动/重命名：mv

```bash
mv oldname.txt newname.txt  # 重命名
mv file.txt /home/user/     # 移动到指定目录
mv folder1 /tmp/            # 移动整个文件夹
```

---

### 8. 删除文件：rm

```bash
rm file.txt                 # 删除文件
rm -r folder                # 删除文件夹（-r递归）
rm -f file.txt              # 强制删除，不询问
rm -rf folder               # 删除文件夹且不询问（危险！）
```

**警告**：
- `rm -rf /` 会删除整个系统，千万别试
- 删除前想清楚，Linux没有回收站

---

## 三、查看文件内容

### 1. cat：一次性显示全部

```bash
cat file.txt                # 显示文件全部内容
cat file1 file2             # 同时显示多个文件
```

**适合**：小文件（几十行以内）

---

### 2. less：分页查看

```bash
less file.txt
```

**操作方式**：
- 空格键：下一页
- b：上一页
- /关键词：搜索
- q：退出

**适合**：大文件（几百行以上）

---

### 3. head 和 tail：看开头和结尾

```bash
head file.txt               # 显示前10行
head -20 file.txt           # 显示前20行

tail file.txt               # 显示后10行
tail -20 file.txt           # 显示后20行
tail -f logfile.txt         # 实时追踪（看日志文件必备）
```

---

## 四、综合练习

### 练习1：创建一个项目结构

用命令完成以下操作：

1. 在家目录下创建 `projects` 文件夹
2. 进入 `projects`，创建 `myapp` 文件夹
3. 在 `myapp` 里创建三个文件：`main.py`、`config.txt`、`README.md`
4. 创建 `data` 子文件夹

**自己先试试，再看答案↓**

<details>
<summary>点击查看答案</summary>

```bash
cd ~
mkdir projects
cd projects
mkdir myapp
cd myapp
touch main.py config.txt README.md
mkdir data
```

</details>

---

### 练习2：文件复制和移动

1. 把 `config.txt` 复制一份叫 `config_backup.txt`
2. 把 `config_backup.txt` 移动到 `data` 文件夹里
3. 删除 `data` 文件夹里的备份文件

<details>
<summary>点击查看答案</summary>

```bash
cp config.txt config_backup.txt
mv config_backup.txt data/
rm data/config_backup.txt
```

</details>

---

### 练习3：查看文件

1. 用 `ls` 查看 `myapp` 文件夹内容
2. 用 `pwd` 确认当前路径
3. 用 `ls -lh` 查看详细信息

---

## 五、常见问题

**Q：命令输入错了怎么办？**
A：按 `Ctrl + C` 取消当前命令，重新输

**Q：找不到文件怎么办？**
A：用 `ls` 看看当前目录有什么，用 `pwd` 确认在哪

**Q：怎么知道命令怎么用？**
A：输入 `man 命令名` 或 `命令名 --help`，比如 `ls --help`

---

## 六、今日总结

**今天学会了**：

| 命令 | 作用 |
|------|------|
| pwd | 我在哪 |
| ls | 这里有什么 |
| cd | 去哪里 |
| mkdir | 创建文件夹 |
| touch | 创建文件 |
| cp | 复制 |
| mv | 移动/重命名 |
| rm | 删除 |
| cat | 看小文件 |
| less | 看大文件 |
| head/tail | 看开头/结尾 |

---

## 七、明天预告

**明天学**：文件权限与用户管理
- 为什么有时候删不了文件？（权限问题）
- chmod 怎么用
- sudo 是什么

---

**学完了？去做练习题，或者明天继续！**

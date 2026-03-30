# Week 1 Day 1 全天练习题集

## 🎯 练习目标
通过本练习题集，巩固掌握Day 1上午（Pandas数据加载基础）和下午（Linux文件操作基础）的所有知识点，通过大量练习实现真正掌握。

**知识点回顾**
- **上午（Pandas）**：`pd.read_csv()`（读取CSV文件）、`.head()`（预览数据前几行）
- **下午（Linux）**：`ls`（列出目录内容）、`cat`（查看文件内容）、文件路径概念（绝对路径与相对路径）

**英语支持**：所有新英文术语提供中文翻译和音标标注，帮助你理解和记忆。

**练习结构**（按难度递增）
1. **基础知识回顾** - 每个知识点核心用途复述
2. **代码补全** - 给出部分代码，补全关键函数调用
3. **实际问题解决** - 结合电影数据集，用所学知识点解决稍复杂分析任务
4. **知识串联挑战** - 上午Pandas+下午Linux交叉应用

**重要提示**
- 请先独立完成所有练习，不要提前看参考答案
- 完成后，参考答案在文档末尾单独列出，用于自我检查
- 如果有错误，分析原因并重做相关练习

---

## 第一部分：基础知识回顾

**说明**：用一句话或简短描述回答以下问题，回顾每个知识点的核心用途。

### 上午知识点：Pandas数据加载基础

1. **`pd.read_csv()`函数**（/piː diː riːd siː es viː/ 读取CSV文件）
   - 这个函数能解决什么问题？（用你自己的话描述）
   
2. **`.head()`方法**（/hɛd/ 查看前几行）
   - 解释`.head(3)`和`.head(10)`的区别？
   - 为什么查看数据时常用这个方法而不是直接打印全部数据？

3. **DataFrame概念**（/ˈdeɪtə freɪm/ 数据框）
   - 什么是DataFrame？它和Excel表格有什么相似之处？

### 下午知识点：Linux文件操作基础

4. **`ls`命令**（/ɛl ɛs/ 列出目录内容）
   - 描述`ls -l`命令输出的每一列含义（如权限、文件数量、所有者、大小、修改时间、文件名）
   
5. **`cat`命令**（/kæt/ 连接文件并打印）
   - `cat`命令适合查看什么类型的文件？如果文件很大（如1GB）会有什么问题？
   - 如何结合管道`|`（/paɪp/ 管道）和`head`命令查看文件前5行？

6. **文件路径概念**（/faɪl pæθ/ 文件路径）
   - 解释绝对路径`/home/user/data/movies_sample.csv`和相对路径`data/movies_sample.csv`的区别？
   - 以下特殊符号代表什么目录？
     - `.`（dot 点）
     - `..`（dot dot 点点）
     - `~`（tilde 波浪号）

---

## 第二部分：代码补全

**说明**：在空白处补全代码，使程序能够正常运行。

### 上午练习：Pandas代码补全

**练习1**：加载电影数据文件
```python
# 请补全代码
import pandas as pd

# 读取电影数据文件（data/movies_sample.csv）
movies_df = pd.read_csv('data/movies_sample.csv')  # 填入函数名

# 查看前5行数据
print(movies_df.head(5))  # 填入方法名
```

**练习2**：查看数据维度
```python
# 接续上面的代码
# 查看movies_df有多少行、多少列
print("数据维度：", movies_df.shape)  # 填入属性名
```

**练习3**：自定义查看行数
```python
# 查看movies_df的前3行
print(movies_df.head(3))  # 填入方法名和参数
```

**练习4**：加载评分数据并查看
```python
# 读取评分数据文件
ratings_df = pd.read_csv('data/tatings.csv')  # 填入函数名和文件名

# 查看评分数据的前10行
print(ratings_df.head(10))  # 填入方法名和参数
```

### 下午练习：Linux命令补全

**练习5**：探索目录结构
```bash
# 1. 查看当前所在目录
pwd

# 2. 列出当前目录下所有文件和文件夹（详细格式）
ls -l

# 3. 查看data目录下的内容
ls data/

# 4. 查看data目录下所有文件（包括隐藏文件）
ls -a data/
```

**练习6**：查看文件内容
```bash
# 1. 查看movies_sample.csv文件的全部内容
cat data/movies_sample.csv

# 2. 仅查看movies_sample.csv文件的前3行（使用管道）
cat data/movies_sample.csv | head -3

# 3. 仅查看ratings.csv文件的最后2行
cat data/ratings.csv | tail -2
```

**练习7**：路径操作
```bash
# 1. 切换到data目录
cd data/

# 2. 查看当前目录（确认已进入data目录）
pwd

# 3. 查看当前目录下的movies_sample.csv文件（使用相对路径）
cat ./movies_sample.csv | head -1

# 4. 返回上级目录
cd ..
```

---

## 第三部分：实际问题解决

**说明**：结合电影数据集，用所学知识点解决稍复杂的分析任务。请写出完整的代码或命令序列。

### 问题1：Linux文件探索与查看任务

**任务描述**：
在Linux环境中，你需要探索电影数据文件的结构和内容，仅使用今天学过的`ls`、`cat`命令和文件路径知识。

**具体步骤**：
1. 查看当前工作目录位置
2. 列出`data/`目录下的所有文件
3. 查看`data/movies_sample.csv`文件的前5行内容
4. 查看`data/ratings.csv`文件的最后2行内容
5. 使用相对路径和绝对路径两种方式查看同一文件

**请写出完整的命令序列**：
```bash
# 步骤1：查看当前所在目录（显示完整路径）
pwd
# 步骤2：列出data目录下的所有文件（详细格式）
ls -l data/

# 步骤3：查看movies_sample.csv文件的前5行（使用管道）
cat data/movies_sample.csv | head -5

# 步骤4：查看ratings.csv文件的最后2行（使用管道）
cat data/ratings.csv | tail -2

# 步骤5：假设当前在项目根目录，用绝对路径查看movies_sample.csv的第一行
# 提示：先用pwd获取当前绝对路径，然后拼接/data/movies_sample.csv
# 例如：如果pwd返回/home/user/project，则绝对路径为/home/user/project/data/movies_sample.csv
# 请写出查看第一行的命令（使用你获得的绝对路径）
cat /home/user/data/movies_sample.csv | head -1
```

### 问题2：Pandas数据分析任务

**任务描述**：
使用Pandas分析电影数据集，完成以下分析任务：

**具体任务**：
1. 加载`data/movies_sample.csv`文件
2. 统计电影数据集中总共有多少部电影
3. 找出评分最高的5部电影，显示它们的`title`（电影标题）和`rating`（评分）
4. 统计平均评分是多少

**请写出完整的Python代码**：
```python
import pandas as pd

# 任务1：加载电影数据文件
movies_df = pd.read_csv('data/movies_sample.csv')  # 补全

# 任务2：统计电影数量
# 提示：DataFrame的.shape属性返回(行数, 列数)
movie_count = movies_df.shape[0]  # 补全获取行数
print(f"电影数据集中共有{movie_count}部电影")

# 任务3：找出评分最高的5部电影
# 提示：使用.sort_values()方法按rating列降序排序
top_movies = movies_df.sort_values(by='rating', ascending=False)  # 补全
print("评分最高的5部电影：")
print(top_movies["titlr","reting"].head(5))  # 补全：选择title和rating列

# 任务4：计算平均评分
average_rating = movies_df['rating'].mean()  # 补全
print(f"平均评分为：{average_rating:.2f}")
```

---

## 第四部分：知识串联挑战

**说明**：将上午的Pandas技能和下午的Linux技能结合起来，完成一个端到端的数据探索任务。

### 综合任务：电影数据分析工作流

**任务描述**：
作为一名AI工程师，你需要在Linux服务器上探索电影数据集，然后用Python进行分析。请按照以下步骤完成：

**步骤1：Linux环境准备**
1. 查看当前工作目录
2. 列出`data/`目录下有哪些文件
3. 快速查看`data/movies_sample.csv`文件的表头（第一行）
4. 快速查看`data/ratings.csv`文件的大小（行数）

**步骤2：Pandas数据分析**
1. 用Pandas加载`data/movies_sample.csv`文件
2. 查看数据的前5行，了解数据结构
3. 查看数据维度（行数和列数）
4. 加载`data/ratings.csv`文件
5. 查看评分数据的前3行

**步骤3：知识串联思考**
1. 这两个数据集之间可能有什么关系？（提示：可以通过`movieId`字段关联）
2. 如果让你分析"哪些电影最受欢迎"，你需要结合这两个数据集做什么操作？

**请完成以下任务**：

**A. Linux命令部分**（写出具体命令）
```bash
# 1. 查看当前目录
pwd

# 2. 列出data目录内容
ls data/

# 3. 查看movies_sample.csv的表头（第一行）
cat data/movies_sample.csv | head -1

# 4. 查看ratings.csv的行数（使用wc命令）
wc -l data/ratings.csv
#`-l` = line（行）的缩写 只统计文件有多少行
```


**B. Python代码部分**（写出完整代码）
```python
import pandas as pd

# 1. 加载电影数据
movies_df = pd.read_csv('data/movies_sample.csv')
print("电影数据前5行：")
print(movies_df.head(5))

# 2. 查看电影数据维度
print(f"电影数据维度：{movies_df.shape________}")

# 3. 加载评分数据  
ratings_df = ____pd.read_csv____('data/_____ratings___.csv')
print("\\n评分数据前3行：")
print(ratings_df.____head____(3))

# 4. 查看评分数据维度
print(f"评分数据维度：{ratings_df.____shape____}")
```

**C. 思考题**（简要回答）
1. 这两个数据集可能有什么关系？
   
2. 如何分析"哪些电影最受欢迎"？
   

---

## 参考答案

**提示**：先独立完成所有练习，再对照参考答案检查。

### 第一部分：基础知识回顾

**上午知识点**
1. **`pd.read_csv()`函数**：将CSV格式的数据文件加载到Python中，转换为Pandas的DataFrame数据结构，用于后续数据分析。
   
2. **`.head()`方法**：
   - `.head(3)`显示前3行数据，`.head(10)`显示前10行数据
   - 常用这个方法是因为数据文件可能有成千上万行，不能一次性打印全部，只需要看前几行就能了解数据结构、列名和大致内容
   
3. **DataFrame概念**：DataFrame是Pandas中的二维表格数据结构，类似Excel表格，有行和列，每列可以是不同的数据类型（字符串、整数、浮点数等）。

**下午知识点**
4. **`ls`命令**：`ls -l`输出包括：
   - 文件权限（如drwxr-xr-x）
   - 文件数量（目录）
   - 所有者
   - 所属组
   - 文件大小（字节）
   - 最后修改时间
   - 文件名
   
5. **`cat`命令**：
   - 适合查看文本文件、配置文件、日志文件、数据文件等
   - 如果文件很大（1GB），`cat`会一次性输出全部内容，导致终端刷屏且难以查看
   - 查看前5行：`cat data/movies_sample.csv | head -5`
   
6. **文件路径概念**：
   - **绝对路径**从根目录`/`开始，完整指定文件位置，如`/home/user/data/movies_sample.csv`
   - **相对路径**相对于当前目录，如`data/movies_sample.csv`表示当前目录下的data子目录中的文件
   - 特殊符号：
     - `.`：当前目录
     - `..`：上级目录  
     - `~`：当前用户的家目录

### 第二部分：代码补全

**上午练习答案**
```python
# 练习1
import pandas as pd
movies_df = pd.read_csv('data/movies_sample.csv')
print(movies_df.head())

# 练习2
print("数据维度：", movies_df.shape)

# 练习3
print(movies_df.head(3))

# 练习4
ratings_df = pd.read_csv('data/ratings.csv')
print(ratings_df.head(10))
```

**下午练习答案**
```bash
# 练习5
pwd
ls -l
ls data/
ls -a data/

# 练习6
cat data/movies_sample.csv
cat data/movies_sample.csv | head -3
cat data/ratings.csv | tail -2

# 练习7
cd data/
pwd
cat ./movies_sample.csv | head -1
cd ..
```

### 第三部分：实际问题解决

**问题1：Linux文件探索与查看任务答案**
```bash
# 步骤1：查看当前所在目录（显示完整路径）
pwd

# 步骤2：列出data目录下的所有文件（详细格式）
ls -l data/

# 步骤3：查看movies_sample.csv文件的前5行（使用管道）
cat data/movies_sample.csv | head -5

# 步骤4：查看ratings.csv文件的最后2行（使用管道）
cat data/ratings.csv | tail -2

# 步骤5：假设当前在项目根目录，用绝对路径查看movies_sample.csv的第一行
# 提示：先用pwd获取当前绝对路径，然后拼接/data/movies_sample.csv
# 例如：如果pwd返回/home/user/project，则绝对路径为/home/user/project/data/movies_sample.csv
# 请写出查看第一行的命令（使用你获得的绝对路径）
# 假设pwd返回/home/user/project，则命令如下：
cat /home/user/project/data/movies_sample.csv | head -1
```

**问题2：Pandas数据分析任务答案**
```python
import pandas as pd

# 任务1：加载电影数据文件
movies_df = pd.read_csv('data/movies_sample.csv')

# 任务2：统计电影数量
movie_count = movies_df.shape[0]  # 获取行数
print(f"电影数据集中共有{movie_count}部电影")

# 任务3：找出评分最高的5部电影
top_movies = movies_df.sort_values(by='rating', ascending=False)
print("评分最高的5部电影：")
print(top_movies[['title', 'rating']].head(5))

# 任务4：计算平均评分
average_rating = movies_df['rating'].mean()
print(f"平均评分为：{average_rating:.2f}")
```

### 第四部分：知识串联挑战答案

**A. Linux命令部分答案**
```bash
# 1. 查看当前目录
pwd

# 2. 列出data目录内容
ls data/

# 3. 查看movies_sample.csv的表头
cat data/movies_sample.csv | head -1

# 4. 查看ratings.csv的行数
wc -l data/ratings.csv
```

**B. Python代码部分答案**
```python
import pandas as pd

# 1. 加载电影数据
movies_df = pd.read_csv('data/movies_sample.csv')
print("电影数据前5行：")
print(movies_df.head(5))

# 2. 查看电影数据维度
print(f"电影数据维度：{movies_df.shape}")

# 3. 加载评分数据
ratings_df = pd.read_csv('data/ratings.csv')
print("\n评分数据前3行：")
print(ratings_df.head(3))

# 4. 查看评分数据维度
print(f"评分数据维度：{ratings_df.shape}")
```

**C. 思考题参考答案**
1. **两个数据集的关系**：`movies_sample.csv`包含电影的基本信息（movieId, title, genres, rating），`ratings.csv`包含用户对电影的评分（userId, movieId, rating, timestamp）。两个数据集可以通过`movieId`字段关联，从而分析每部电影收到的用户评分情况。

2. **分析"哪些电影最受欢迎"**：
   - 方法1：使用`movies_sample.csv`中的`rating`字段，评分高的电影可能更受欢迎
   - 方法2：结合两个数据集，统计`ratings.csv`中每部电影收到的评分数量，评分次数多的电影可能更受欢迎
   - 方法3：计算每部电影的平均用户评分（来自`ratings.csv`），再结合评分数量综合判断

---

## 🎉 练习完成总结

恭喜你完成了Day 1的全部练习！通过这四部分练习，你应该已经：

1. **巩固了核心概念**：能清晰描述每个函数/命令的用途
2. **掌握了基础操作**：能正确写出Pandas代码和Linux命令
3. **提升了问题解决能力**：能结合多个知识点解决实际分析任务
4. **建立了知识串联思维**：理解数据分析与环境操作的完整工作流

**下一步建议**：
- 如果有任何练习做错，分析错误原因并重做相关部分
- 在实际环境中运行你的代码和命令，观察输出结果
- 尝试用今天学到的技能分析你自己的数据文件

明天我们将学习Pandas数据筛选与排序（上午）和Linux文件编辑与操作（下午），继续深化全栈AI工程师技能树。
# Week 1 Day 2 上午：Pandas 数据筛选与排序

## 1. 问题引入

昨天我们已经学会了两个核心技能：
- **`pd.read_csv()`**（读CSV文件）：将硬盘上的数据文件加载到内存中，变成可操作的DataFrame表格
- **`.head()`**（看前几行）：快速查看数据的“样貌”，了解列名和前几条记录

但在真实的数据分析工作中，我们经常遇到更复杂的需求：

> **场景一**：项目经理说：“给我看第30-40条数据，我想了解中间部分的情况。”  
> **现有知识局限**：`.head()`只能看前5行，`.tail()`只能看后5行，无法查看任意区间

> **场景二**：产品经理问：“有哪些电影的评分在4分以上？我想找高质量内容。”  
> **现有知识局限**：我们只会整体查看数据，无法根据条件“过滤”出特定记录

> **场景三**：运营同事说：“按评分从高到低排序，我想看看最受欢迎的电影。”  
> **现有知识局限**：数据现在是原始顺序，无法按任何标准重新排列

**总结来说**：我们掌握了数据的“加载”和“初步查看”，但还不会：
1. 按位置精确选择数据行（查看指定行号范围）
2. 按条件筛选数据（只留下符合条件的内容）
3. 按规则排序数据（让数据按某列有序排列）

今天上午，我们就来解决这三个问题，掌握Pandas的**数据筛选**与**数据排序**核心能力。

## 2. 知识点1：`.iloc[]`索引器

### 核心概念
- **中文**：基于整数位置的索引（integer location）
- **音标**：/ˈaɪlɒk/ （读作"I-lock"）
- **用途**：按行号、列号精确选择DataFrame中的数据子集
- **类比理解**：就像Excel中的“第几行第几列”定位方式

### 为什么要学`.iloc[]`？
在实际工作中，数据文件可能有成千上万行，我们经常需要：
- 查看开头、中间、结尾的不同部分
- 抽取特定位置的数据进行抽查验证
- 处理大型数据时，只加载部分行以节省内存

### 最小示例
让我们先加载电影数据，然后尝试`.iloc[]`的各种用法：

```python
import pandas as pd

# 加载电影数据（复习昨天的知识）
# pd.read_csv() - 读CSV文件 (read CSV file)
# 音标：/ˈriːd ˈsiː es ˈviː faɪl/ 
df = pd.read_csv('data/movies_sample.csv')

# 查看前5行（复习）
print("前5行数据（复习.head()）：")
print(df.head())
print("\n" + "="*50 + "\n")

# ================== .iloc[] 基础用法 ==================

# 1. 选择前10行数据
# 语法：df.iloc[起始行:结束行]
# 注意：结束行不包含在内（和Python切片规则一致）
first_10 = df.iloc[0:10]  # 行号0-9，共10行
print("1. 前10行数据：")
print(first_10)
print("\n" + "="*50 + "\n")

# 2. 选择第30-40行（共11行）
# 行号从0开始，所以第30行对应索引29，第40行对应索引39
rows_30_to_40 = df.iloc[29:40]  # 29到39，共11行
print("2. 第30-40行数据：")
print(rows_30_to_40)
print("\n" + "="*50 + "\n")

# 3. 选择单行数据（第15行）
# 注意：单行选择需要使用单个数字，而不是切片
row_15 = df.iloc[14]  # 索引14对应第15行
print("3. 第15行数据（单行）：")
print(row_15)
print("\n" + "="*50 + "\n")

# 4. 选择特定列（第1列和第3列）
# df.iloc[ 行 , 列 ] 没有逗号 = 只选行！
# 语法：df.iloc[行选择, 列选择]
# 列索引：0=第1列(movieId), 1=第2列(title), 2=第3列(genres), 3=第4列(rating)
cols_1_and_3 = df.iloc[:, [0, 2]]  # 所有行，第1列和第3列
print("4. 第1列(movieId)和第3列(genres)：")
print(cols_1_and_3.head())
print("\n" + "="*50 + "\n")

# 5. 同时选择行和列范围
# 选择第50-55行，第2-4列
subset = df.iloc[49:55, 1:4]  # 行50-54，列2-4（不含列4）
print("5. 第50-55行，第2-4列：")
print(subset)
```

### 关键语法总结
| 语法 | 含义 | 示例 |
|------|------|------|
| `df.iloc[起始:结束]` | 选择行范围（不含结束行） | `df.iloc[0:10]` 选择前10行 |
| `df.iloc[行号]` | 选择单行 | `df.iloc[14]` 选择第15行 |
| `df.iloc[:, 列号]` | 选择单列 | `df.iloc[:, 2]` 选择第3列 |
| `df.iloc[行范围, 列范围]` | 同时选择行和列 | `df.iloc[0:5, 1:3]` |

### 动手练习1：`.iloc[]`实战
现在请你尝试以下任务：

```python
# 任务1：查看电影的中间部分数据（第100-110行）
# 提示：索引从0开始，第100行对应索引99
middle_rows = df.iloc[99:110]  # 请补全代码
print("任务1 - 第100-110行：")
print(middle_rows)

# 任务2：只查看电影标题（第2列）的前20条记录
# 提示：用`.iloc`选择所有行（用`:`表示）和特定列
titles_first_20 = df.iloc[0:20, 1]  # 请补全代码
print("\n任务2 - 前20部电影标题：")
print(titles_first_20)

# 任务3：查看第50行电影的评分（第4列）
# 提示：先选择第50行（索引49），再选择评分列
row_50_rating = df.iloc[49, 3]  # 请补全代码
print("\n任务3 - 第50部电影的评分：")
print(row_50_rating)
```

**先不要看下面的答案，自己尝试写代码**

<details>
<summary>点击查看参考答案</summary>

```python
# 任务1答案
middle_rows = df.iloc[99:110]
print("任务1 - 第100-110行：")
print(middle_rows)

# 任务2答案  
titles_first_20 = df.iloc[0:20, 1]
print("\n任务2 - 前20部电影标题：")
print(titles_first_20)

# 任务3答案
row_50_rating = df.iloc[49, 3]
print("\n任务3 - 第50部电影的评分：")
print(row_50_rating)```
</details>
```


```
## 3. 知识点2：条件筛选

### 核心概念
- **中文**：条件筛选（conditional filtering）
- **音标**：/kənˈdɪʃənl ˈfɪltərɪŋ/
- **用途**：根据布尔条件（True/False）从DataFrame中筛选出符合条件的行
- **类比理解**：就像在Excel中使用“筛选”功能，只显示满足条件的行

### 为什么要学条件筛选？
在数据分析中，我们很少需要分析所有数据，更多时候是：
- 只分析高价值客户（如评分>4的用户）
- 只关注特定类别的产品（如类型包含"Action"的电影）
- 排除异常数据（如价格异常高的记录）

### 最小示例
```python
# ================== 条件筛选基础 ==================

# 1. 基础条件筛选语法
# 语法：df[条件表达式]
# 条件表达式生成一个布尔序列（True/False），True对应的行被保留

# 筛选评分大于4.0的电影
high_rating_movies = df[df['rating'] > 4.0]
print("1. 评分>4.0的电影（共{}部）：".format(len(high_rating_movies)))
print(high_rating_movies.head())
print("\n" + "="*50 + "\n")

# 2. 多条件组合（与运算）
# 使用 & 符号连接多个条件，每个条件要用括号括起来
action_high_rating = df[(df['genres'].str.contains('Action')) & (df['rating'] > 3.5)]
print("2. 动作片且评分>3.5的电影（共{}部）：".format(len(action_high_rating)))
print(action_high_rating.head())
print("\n" + "="*50 + "\n")

# 3. 多条件组合（或运算）
# 使用 | 符号连接多个条件
comedy_or_animation = df[(df['genres'].str.contains('Comedy')) | (df['genres'].str.contains('Animation'))]
print("3. 喜剧或动画片（共{}部）：".format(len(comedy_or_animation)))
print(comedy_or_animation.head())
print("\n" + "="*50 + "\n")

# 4. 范围筛选（between）
# 筛选评分在某个范围内的电影
mid_rating_movies = df[df['rating'].between(3.0, 4.0)]
print("4. 评分在3.0-4.0之间的电影（共{}部）：".format(len(mid_rating_movies)))
print(mid_rating_movies.head())
print("\n" + "="*50 + "\n")

# 5. 字符串包含筛选（contains）
# 筛选类型中包含特定关键词的电影
drama_movies = df[df['genres'].str.contains('Drama')]
print("5. 剧情片（共{}部）：".format(len(drama_movies)))
print(drama_movies.head())
```

### 条件筛选的底层逻辑
1. **`df['rating'] > 4.0`** 会产生一个布尔序列（长度和DataFrame行数相同）
2. 每个位置是True或False，表示该行是否满足条件
3. **`df[布尔序列]`** 只保留True对应的行

```python
# 查看布尔序列的样子
bool_series = df['rating'] > 4.0
print("布尔序列前10个值：")
print(bool_series.head(10))
print("\n数据类型：", type(bool_series))
```

### 动手练习2：条件筛选实战
```python
# 任务4：筛选出评分在3.5到4.5之间的电影
# 提示：可以使用between()方法或两个条件用&连接
mid_high_rating = df[df['rating'].between(3.5, 4.5)]  # 请补全代码
print("任务4 - 评分3.5-4.5的电影（共{}部）：".format(len(mid_high_rating)))
print(mid_high_rating.head())

# 任务5：筛选出类型中包含"Children"或"Fantasy"的电影
# 提示：使用|（或）运算符，注意括号
children_or_fantasy = df[(df['genres'].str.contains('Children')) | (df['genres'].str.contains('Fantasy'))]
print("\n任务5 - 儿童或奇幻片（共{}部）：".format(len(children_or_fantasy)))
print(children_or_fantasy.head())

# 任务6：筛选出评分低于3.0且类型中包含"Comedy"的电影
# 提示：使用&（与）运算符
low_rating_comedy = df[(df['rating'] < 3.0) & (df['genres'].str.contains('Comedy'))]
print("\n任务6 - 低评分喜剧片（共{}部）：".format(len(low_rating_comedy)))
print(low_rating_comedy)
```

<details>
<summary>点击查看参考答案</summary>

```python
# 任务4答案
mid_high_rating = df[df['rating'].between(3.5, 4.5)]
print("任务4 - 评分3.5-4.5的电影（共{}部）：".format(len(mid_high_rating)))
print(mid_high_rating.head())

# 任务5答案
children_or_fantasy = df[(df['genres'].str.contains('Children')) | (df['genres'].str.contains('Fantasy'))]
print("\n任务5 - 儿童或奇幻片（共{}部）：".format(len(children_or_fantasy)))
print(children_or_fantasy.head())

# 任务6答案
low_rating_comedy = df[(df['rating'] < 3.0) & (df['genres'].str.contains('Comedy'))]
print("\n任务6 - 低评分喜剧片（共{}部）：".format(len(low_rating_comedy)))
print(low_rating_comedy)
```
</details>

## 4. 知识点3：`.sort_values()`排序

### 核心概念
- **中文**：按值排序（sort by values）
- **音标**：/sɔːrt baɪ ˈvæljuːz/
- **用途**：按照指定列的值对DataFrame进行升序或降序排列
- **类比理解**：就像在Excel中点击列标题的排序按钮

### 为什么要学排序？
排序是数据整理的基础操作：
- 找最大值/最小值（排序后看第一行或最后一行）
- 数据分析前整理数据（如按时间顺序排列）
- 制作排行榜（如电影评分Top 10）

### 最小示例
```python
# ================== .sort_values() 基础 ==================

# 1. 基本升序排序（默认）
# 语法：df.sort_values(by='列名')
sorted_by_rating_asc = df.sort_values(by='rating')
print("1. 按评分升序排序（前10部）：")
print(sorted_by_rating_asc.head(10))
print("\n" + "="*50 + "\n")

# 2. 降序排序
# 使用 ascending=False 参数
sorted_by_rating_desc = df.sort_values(by='rating', ascending=False)
print("2. 按评分降序排序（前10部）：")
print(sorted_by_rating_desc.head(10))
print("\n" + "="*50 + "\n")

# 3. 多列排序
# 先按评分降序，评分相同再按movieId升序
multi_sorted = df.sort_values(by=['rating', 'movieId'], ascending=[False, True])
print("3. 先按评分降序，再按ID升序（前10部）：")
print(multi_sorted.head(10))
print("\n" + "="*50 + "\n")

# 4. 排序后重置索引
# 排序后索引会乱序，使用 reset_index() 重新编号
sorted_reset = df.sort_values(by='rating', ascending=False).reset_index(drop=True)
print("4. 降序排序并重置索引（前5部）：")
print(sorted_reset.head())
print("\n注意：reset_index(drop=True)会丢弃旧的索引，生成新的连续索引")
```

### 排序的注意事项
1. **原地排序**：可以使用 `inplace=True` 参数直接修改原DataFrame
2. **缺失值处理**：默认NaN会被放在排序结果的最后
3. **性能考虑**：大数据集排序可能较慢，考虑是否需要全部排序

```python
# 原地排序示例（会修改原df，谨慎使用）
df_copy = df.copy()  # 创建副本以防影响后续操作
df_copy.sort_values(by='rating', ascending=False, inplace=True)
print("原地排序后的前5行：")
print(df_copy.head())
```

### 动手练习3：排序实战
```python
# 任务7：按电影ID（movieId）升序排序，查看排序后的前15部电影
# 提示：使用sort_values，by参数指定'movieId'
sorted_by_id = df.sort_values(by='movieId')  # 请补全代码
print("任务7 - 按ID升序排序（前15部）：")
print(sorted_by_id.head(15))

# 任务8：按评分从低到高排序（升序），查看评分最低的10部电影
# 提示：ascending=True是默认值，可以省略
lowest_rating = df.sort_values(by='rating')  # 请补全代码
print("\n任务8 - 评分最低的10部电影：")
print(lowest_rating.head(10))

# 任务9：创建电影评分排行榜（降序排序），并重置索引
# 提示：先排序，再reset_index(drop=True)
rating_rank = df.sort_values(by='rating', ascending=False).reset_index(drop=True)
print("\n任务9 - 电影评分排行榜（前10名）：")
print(rating_rank.head(10))
print("排行榜共{}部电影".format(len(rating_rank)))
```

<details>
<summary>点击查看参考答案</summary>

```python
# 任务7答案
sorted_by_id = df.sort_values(by='movieId')
print("任务7 - 按ID升序排序（前15部）：")
print(sorted_by_id.head(15))

# 任务8答案  
lowest_rating = df.sort_values(by='rating')
print("\n任务8 - 评分最低的10部电影：")
print(lowest_rating.head(10))

# 任务9答案
rating_rank = df.sort_values(by='rating', ascending=False).reset_index(drop=True)
print("\n任务9 - 电影评分排行榜（前10名）：")
print(rating_rank.head(10))
print("排行榜共{}部电影".format(len(rating_rank)))
```
</details>

## 5. 综合实战与掌握验证

### 综合练习：电影数据分析师任务
假设你是一家流媒体平台的数据分析师，收到以下业务需求：

```python
# 需求1：查看平台中间部分的电影质量（第150-160行）
middle_quality = df.iloc[149:160]
print("需求1 - 中间部分电影（150-160行）：")
print(middle_quality)

# 需求2：筛选出高质量动作片（评分>4.0且类型含Action）
high_quality_action = df[(df['rating'] > 4.0) & (df['genres'].str.contains('Action'))]
print("\n需求2 - 高质量动作片（共{}部）：".format(len(high_quality_action)))
print(high_quality_action)

# 需求3：制作不同类型的电影排行榜
# 3.1 喜剧片排行榜（降序）
comedy_rank = df[df['genres'].str.contains('Comedy')].sort_values(by='rating', ascending=False).reset_index(drop=True)
print("\n需求3.1 - 喜剧片排行榜（前10名）：")
print(comedy_rank.head(10))

# 3.2 动画片排行榜（降序）  
animation_rank = df[df['genres'].str.contains('Animation')].sort_values(by='rating', ascending=False).reset_index(drop=True)
print("\n需求3.2 - 动画片排行榜（前10名）：")
print(animation_rank.head(10))
```

### 掌握验证测试
请在不看代码的情况下，回答以下问题：

1. **概念复述**（费曼技巧）
   - 请用一句话说明`.iloc[]`的用途
   - 请解释条件筛选的底层逻辑（布尔序列）
   - 描述`.sort_values()`排序时`ascending`参数的作用

2. **代码填空**
   ```python
   # 填空1：选择第80-90行数据
   rows_80_90 = df.iloc[_____:_____]
   
   # 填空2：筛选评分在4.0以上的电影
   high_rating = df[_____]
   
   # 填空3：按标题字母顺序升序排列
   sorted_by_title = df.sort_values(by=_____, ascending=_____)
   ```

3. **实际问题解决**
   > 产品经理问：“我想看评分最高的5部剧情片（Drama），并且只显示电影标题和评分两列，你能做到吗？”
   
   请写出完整代码实现这个需求。

### 验证答案
<details>
<summary>点击查看掌握验证答案</summary>

**1. 概念复述参考答案**
- `.iloc[]`：基于整数位置选择DataFrame中的行和列，可以按行号、列号精确选择数据子集
- 条件筛选底层逻辑：条件表达式生成布尔序列（True/False），`df[布尔序列]`只保留True对应的行
- `ascending`参数：控制排序方向，`True`为升序（从小到大），`False`为降序（从大到小）

**2. 代码填空参考答案**
```python
# 填空1：选择第80-90行数据
rows_80_90 = df.iloc[79:90]  # 索引从0开始，第80行对应索引79

# 填空2：筛选评分在4.0以上的电影
high_rating = df[df['rating'] > 4.0]

# 填空3：按标题字母顺序升序排列
sorted_by_title = df.sort_values(by='title', ascending=True)
```

**3. 实际问题解决参考答案**
```python
# 筛选剧情片
drama_movies = df[df['genres'].str.contains('Drama')]

# 按评分降序排序
top_drama = drama_movies.sort_values(by='rating', ascending=False)

# 选择前5部，只显示标题和评分两列
top_5_drama = top_drama[['title', 'rating']].head(5)

print("评分最高的5部剧情片：")
print(top_5_drama)
```
</details>

## 6. 知识衔接与交叉学习

### 与昨日内容的关联
| 昨日技能 | 今日扩展 | 能力提升 |
|----------|----------|----------|
| `pd.read_csv()` 加载数据 | `.iloc[]` 精确选择数据 | 从"全部加载"到"精准定位" |
| `.head()` 查看前几行 | 条件筛选查看特定行 | 从"看前面"到"看想要的部分" |
| 整体数据概览 | `.sort_values()` 有序查看 | 从"原始顺序"到"智能排列" |

**知识演进路径**：
```
加载数据 → 查看数据 → 筛选数据 → 排序数据
    ↓         ↓          ↓          ↓
  基础     初步了解    精准分析    深度洞察
```

### 与下午Linux内容的交叉
上午我们学会了用Pandas**筛选**和**排序**数据文件，下午将学习用Linux命令**操作**这些文件：

| 上午（Pandas） | 下午（Linux） | 完整工作流 |
|----------------|---------------|------------|
| `.iloc[]` 选择数据行 | `head/tail` 查看文件首尾 | 精准定位+快速预览 |
| 条件筛选特定数据 | `grep` 搜索文件内容 | 逻辑筛选+文本搜索 |
| `.sort_values()` 排序 | `sort` 命令排序文本 | 内存排序+文件排序 |

**实际应用场景**：
1. 上午用Pandas筛选出高评分电影 → 下午用Linux命令批量重命名这些电影文件
2. 上午按评分排序生成排行榜 → 下午用Linux命令将排行榜导出为文本文件
3. 上午筛选特定类型电影 → 下午用Linux命令统计各类型电影文件数量

### OpenClaw/AI模型部署场景提及
在AI模型数据处理中，今天学的三个技能有直接应用：

1. **`.iloc[]` 在数据批处理中**
   - 大型训练集分批次加载（如每次加载1000条）
   - 验证集/测试集按比例分割
   - 示例：`training_batch = dataset.iloc[0:1000]`

2. **条件筛选在数据清洗中**
   - 过滤低质量训练样本（如置信度<0.8的标注）
   - 筛选特定类别的数据用于分类模型
   - 示例：`high_quality_data = raw_data[raw_data['confidence'] > 0.9]`

3. **`.sort_values()` 在结果分析中**
   - 按预测概率排序，取Top-K结果
   - 按损失值排序，找出最难样本
   - 示例：`hard_samples = predictions.sort_values(by='loss', ascending=False).head(100)`

**实际工作流举例**：
```python
# OpenClaw数据处理管道
# 1. 加载原始数据
raw_data = pd.read_csv('dataset.csv')

# 2. 筛选高质量样本（条件筛选）
clean_data = raw_data[raw_data['quality_score'] > 0.8]

# 3. 分割训练/验证集（.iloc[]）
train_set = clean_data.iloc[0:8000]
val_set = clean_data.iloc[8000:]

# 4. 按难度排序样本用于课程学习（.sort_values()）
hard_first = train_set.sort_values(by='difficulty', ascending=False)

# 5. 保存处理后的数据（下午Linux命令会用到）
hard_first.to_csv('processed/train_hard_first.csv', index=False)
```

## 7. 今日总结与明日预告

### 今日掌握清单
✓ **`.iloc[]` 整数位置索引**：按行号、列号精确选择数据  
✓ **条件筛选**：根据布尔条件过滤出符合条件的行  
✓ **`.sort_values()` 排序**：按指定列升序/降序排列数据  

### 每个技能能解决的实际问题
1. **`.iloc[]`** → "给我看数据的第X到第Y行"（精确定位）
2. **条件筛选** → "只显示评分>4.0/类型包含Action的电影"（逻辑过滤）
3. **`.sort_values()`** → "按评分从高到低排个序"（有序查看）

### 明日学习目标
**Week 1 Day 2 下午：Linux文件编辑与操作**
- 命令1：`cp`（copy）复制文件
- 命令2：`mv`（move）移动/重命名文件  
- 命令3：`mkdir`（make directory）创建目录
- 实际应用：操作上午生成的电影数据文件，建立项目目录结构

### 英语术语快速复习
| 英文术语 | 中文翻译 | 音标 | 今日重点 |
|----------|----------|------|----------|
| `.iloc[]` | 整数位置索引 | /ˈaɪlɒk/ | 行号列号定位 |
| conditional filtering | 条件筛选 | /kənˈdɪʃənl ˈfɪltərɪŋ/ | 布尔条件过滤 |
| `.sort_values()` | 按值排序 | /sɔːrt baɪ ˈvæljuːz/ | 升序降序排列 |
| ascending | 升序 | /əˈsendɪŋ/ | 从小到大 |
| descending | 降序 | /dɪˈsendɪŋ/ | 从大到小 |

---

**学习建议**：
1. 完成所有动手练习，确保代码能正常运行
2. 尝试修改参数（如改变行号范围、调整筛选条件）观察不同结果
3. 思考这些技能在你感兴趣的项目中如何应用
4. 有问题随时记录，下午学习时我们可以一起解决

现在运行上面的代码，开始今天的Pandas数据筛选与排序实战吧！
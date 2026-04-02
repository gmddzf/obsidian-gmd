# Week 1 Day 3 上午：Pandas数据聚合

## 🎯 今日学习目标
通过「问题驱动、单函数教学」模式，掌握Pandas中数据聚合的三个核心操作：
1. `.groupby()` - 按列分组
2. `.agg()` - 聚合计算
3. 多列分组与多重聚合

**学习循环**：问题引入 → 知识点讲解 → 代码示例 → 动手练习 → 掌握验证

**英语支持**：所有新英文术语提供中文翻译和音标标注，帮助你理解和记忆。

**数据集**：继续使用电影数据 `data/movies_sample.csv`

**与前期知识衔接**：今天的内容建立在Day 1（数据加载）和Day 2（数据筛选）的基础上，让你从“查看数据”进阶到“分析数据”。

**交叉学习设计**：今天下午将学习Linux权限管理（`chmod`、`sudo`），这是部署数据分析服务时的必备技能，与上午的数据分析形成完整的工作流闭环。

---

## 🔍 问题引入：如何从数据中发现模式？

### 场景设定
前两日我们掌握了Pandas的核心基础：

**Day 1 上午**：学会了加载电影数据
- `pd.read_csv()` - 读取CSV文件
- `.head()` - 预览数据前几行

**Day 2 上午**：学会了筛选和排序数据
- `.iloc[]` - 按位置选择数据
- 条件筛选 - 筛选出高评分电影（`rating > 4.0`）
- `.sort_values()` - 按评分排序

但现在，作为数据分析师，你需要回答更复杂的问题：

**问题1**：不同电影类型的平均评分是多少？
> 比如：“动画类电影平均评分 vs 喜剧类电影平均评分”

**问题2**：每年的电影数量分布如何？
> 比如：“1995年有多少部电影？1996年呢？”

**问题3**：能否同时按年份和类型分组，做更精细的分析？
> 比如：“1995年的动画类电影平均评分是多少？”

### 现有知识检查
- **当前能力**：你可以加载数据、查看数据、筛选数据、排序数据
- **知识缺口**：无法对数据进行**分组统计**，无法计算**聚合指标**（平均值、总和、计数等）

### 思考时间
暂停10秒，想一想：
- 如果你只有Day 1和Day 2的知识，你会怎么解决“计算动画类电影平均评分”？
- 你可能会：先筛选出动画类电影 → 计算评分的平均值
- 但如果要同时计算10种类型的平均评分，你需要重复10次筛选+计算
- 随着问题复杂度增加（年份+类型组合），工作量会指数级增长

**结论**：现有知识无法**高效**完成分组统计任务。我们需要学习Pandas的**数据聚合**功能。

---

## 📚 知识点1：`.groupby()` - 按列分组

### 中文翻译
- **函数名**：`.groupby()`
- **中文含义**：按列分组
- **音标标注**：/ɡruːp baɪ/ （"group"读作"groop"，"by"读作"buy"）

### 核心用途
根据某一列（或多列）的值，将数据分成多个小组（group），每个小组包含该列值相同的所有行。

**类比理解**：
- 就像把全班同学按“性别”分成男生组和女生组
- 或者把电影按“类型”分成动画组、喜剧组、动作组...

### 为什么要学`.groupby()`？
在实际数据分析中，分组是发现模式的第一步：
- 电商分析：按商品类别统计销售额
- 用户分析：按年龄段统计用户数量
- 电影分析：按类型统计平均评分

### 最小示例
让我们先加载电影数据，然后尝试按电影类型分组：

```python
import pandas as pd

# 加载电影数据（复习Day 1知识）
# pd.read_csv() - 读CSV文件 (read CSV file)
# 音标：/ˈriːd ˈsiː es ˈviː faɪl/
movies_df = pd.read_csv('data/movies_sample.csv')

# 查看数据前几行（复习Day 1知识）
print("数据前5行：")
print(movies_df.head())

# 知识点1：.groupby() - 按列分组
# 按电影类型（genres列）分组
# 注意：genres列是"类型1|类型2|类型3"的格式，我们先按整个字符串分组
groups = movies_df.groupby('genres')

# 查看分组结果
print("\n分组数量：", groups.ngroups)
print("分组后的组名（前5个）：")
for name in list(groups.groups.keys())[:5]:
    print(f"  - {name}")
```

**运行结果示例**：
```
数据前5行：
   movieId                title                         genres  rating
0        1  Toy Story (1995)      Animation|Children|Comedy     4.0
1        2      Jumanji (1995)    Adventure|Children|Fantasy    3.5
2        3  Grumpier Old Men (1995)          Comedy|Romance     3.0
3        4  Waiting to Exhale (1995)  Comedy|Drama|Romance     3.5
4        5        Father of the Bride Part II (1995)  Comedy     3.0

分组数量： 20
分组后的组名（前5个）：
  - Adventure|Children|Fantasy
  - Animation|Children|Comedy
  - Comedy
  - Comedy|Drama
  - Comedy|Drama|Romance
```

**关键解释**：
- `movies_df.groupby('genres')`：按`genres`列的值进行分组
- `groups`：是一个`DataFrameGroupBy`对象，不是普通的DataFrame
- `groups.ngroups`：返回分组的数量（这里20种不同的类型组合）
- `groups.groups.keys()`：返回每个分组的名称（即genres的值）

### 动手练习1：按年份分组（拓展思考）

**背景**：我们的数据集没有单独的年份列，但可以从`title`中提取年份（例如"Toy Story (1995)"中的1995）。

**任务**：我们暂时不实际提取年份，而是先理解分组的概念。请回答以下问题：

1. 如果数据中有`year`列，写出按年份分组的代码：
```python
groups=movies_df.groupby('year')# [请在此处填写代码]
```

2. 分组后，`groups`对象包含了什么？（多选题）
   - A. 每个年份对应的数据行
   - B. 按年份排序后的整个DataFrame
   - C. 每个年份组的统计结果
   - D. 年份的唯一值列表

**提示**：回想一下`.groupby()`的原理：按列值分组，每个组包含该值对应的所有行。

### 掌握验证1：复述核心概念

请在脑中复述（或小声说出来）：
- `.groupby()`能解决什么问题？
- 分组后得到的是什么类型的对象？
- 如果要按"城市"和"月份"两列同时分组，代码怎么写？

**答案提示**：
- 解决：按某列值将数据分成多个小组，便于分别分析
- 得到：`DataFrameGroupBy`对象（可以理解为"分组后的数据集合"）
- 代码：`df.groupby(['城市', '月份'])`

---

## 📚 知识点2：`.agg()` - 聚合计算

### 中文翻译
- **函数名**：`.agg()`
- **全称**：aggregate（聚合）
- **中文含义**：聚合计算
- **音标标注**：/ˈæɡrɪɡeɪt/ （aggregate），缩写读作/æɡ/ （agg）

### 核心用途
对每个分组（group）计算一个或多个统计量，如：
- 平均值（mean）
- 总和（sum）
- 计数（count）
- 最大值（max）、最小值（min）
- 标准差（std）等

**完整流程**：分组 → 聚合 = 分组统计

### 为什么要学`.agg()`？
单纯分组只是第一步，我们需要对每个组进行计算：
- 计算每个电影类型的**平均评分**
- 计算每个年份的**电影数量**
- 计算每个地区的**销售总额**

### 最小示例
继续使用电影数据，计算每个电影类型的平均评分：

```python
# 知识点2：.agg() - 聚合计算
# 先分组，再聚合
# 按电影类型分组，对rating列计算平均值
avg_rating_by_genre = movies_df.groupby('genres')['rating'].agg('mean')

print("每个电影类型的平均评分：")
print(avg_rating_by_genre.head(10))
```

**运行结果示例**：
```
每个电影类型的平均评分：
genres
Adventure|Children|Fantasy    3.50
Animation|Children|Comedy     4.00
Comedy                        3.00
Comedy|Drama                  3.50
Comedy|Drama|Romance          3.50
Comedy|Romance                3.00
Crime|Thriller                4.00
Documentary                   4.50
Drama                         4.00
Drama|Romance                 3.50
Name: rating, dtype: float64
```

**语法分解**：
- `movies_df.groupby('genres')`：按genres分组
- `['rating']`：只选择rating列进行后续计算（可选，如果不指定则对所有数值列计算）
- `.agg('mean')`：对每个分组计算平均值
- 其他常用聚合函数：`'count'`, `'sum'`, `'min'`, `'max'`, `'std'`

### 动手练习2：计算每个类型的电影数量

**任务**：使用`.agg()`计算每个电影类型（genres）包含的电影数量。

1. 写出完整代码：
```python
# [请在此处填写代码]
```

2. 运行代码后，回答：哪种电影类型数量最多？数量是多少？

**提示**：
- 电影数量 = 对任意列（如`movieId`）进行计数（`'count'`）
- 可以使用`.sort_values(ascending=False)`排序查看最多

### 掌握验证2：理解聚合函数

请回答：
1. `.agg('mean')`和`.agg('count')`有什么区别？
2. 如果我想同时计算平均评分和最高评分，应该怎么写代码？
3. 聚合计算的结果是什么数据类型？（Series还是DataFrame？）

**答案提示**：
1. `mean`计算平均值，`count`计算非空值的数量
2. 可以传入列表：`.agg(['mean', 'max'])`
3. 单列聚合返回Series，多列或多聚合可能返回DataFrame

---

## 📚 知识点3：多列分组与多重聚合

### 问题引入
我们学会了按单列分组（如`genres`），但真实分析中经常需要：
- 同时按年份**和**类型分组
- 对每个分组计算多个统计量（如平均评分+电影数量）

这就是**多列分组**与**多重聚合**。

### 多列分组
语法：`.groupby(['列1', '列2', ...])`

**示例**：假设我们有年份列`year`，想同时按年份和类型分组
```python
# 假设数据中有year列
# multi_group = movies_df.groupby(['year', 'genres'])
```

### 多重聚合
语法：`.agg({'列名1': '聚合函数1', '列名2': ['聚合函数1', '聚合函数2']})`

**示例**：对rating列计算平均值和最大值，对movieId列计数
```python
# 假设数据中有year列
# result = movies_df.groupby(['year', 'genres']).agg({
#     'rating': ['mean', 'max'],
#     'movieId': 'count'
# })
```

### 实际应用：模拟年份数据
由于我们的数据集没有年份列，我们模拟一个简单场景：添加虚拟年份列。

```python
# 知识点3：多列分组与多重聚合
# 首先，我们为数据添加一个虚拟年份列（仅用于教学）
# 在实际项目中，年份可能从title中提取或来自其他数据源
import numpy as np

# 为前5部电影分配1995年，接着5部分配1996年，以此类推
years = []
for i in range(len(movies_df)):
    if i < 5:
        years.append(1995)
    elif i < 10:
        years.append(1996)
    else:
        years.append(1997)  # 其余分配1997年

movies_df['year'] = years  # 添加新列

print("添加年份列后的数据前10行：")
print(movies_df[['title', 'genres', 'rating', 'year']].head(10))

# 多列分组：同时按年份和类型分组
multi_group = movies_df.groupby(['year', 'genres'])

print("\n多列分组后的组数：", multi_group.ngroups)
print("前5个分组名称：")
for name in list(multi_group.groups.keys())[:5]:
    print(f"  - {name}")

# 多重聚合：计算每个（年份,类型）组的统计量
multi_result = movies_df.groupby(['year', 'genres']).agg({
    'rating': ['mean', 'max', 'count'],  # 平均评分、最高评分、评分数量
    'movieId': 'count'  # 电影数量（与rating count应该一致）
})

print("\n多重聚合结果（前10行）：")
print(multi_result.head(10))
```

**运行结果示例**：
```
添加年份列后的数据前10行：
                           title                         genres  rating  year
0             Toy Story (1995)      Animation|Children|Comedy     4.0  1995
1                 Jumanji (1995)    Adventure|Children|Fantasy    3.5  1995
2         Grumpier Old Men (1995)          Comedy|Romance     3.0  1995
3         Waiting to Exhale (1995)  Comedy|Drama|Romance     3.5  1995
4  Father of the Bride Part II (1995)  Comedy     3.0  1995
5                     Heat (1995)          Crime|Thriller     4.0  1996
6                  Sabrina (1995)          Comedy|Romance     3.0  1996
7             Tom and Huck (1995)    Adventure|Children     3.0  1996
8             Sudden Death (1995)               Action     3.5  1996
9                    GoldenEye (1995)          Action|Adventure|Thriller     3.5  1996

多列分组后的组数： 20
前5个分组名称：
  - (1995, Adventure|Children|Fantasy)
  - (1995, Animation|Children|Comedy)
  - (1995, Comedy)
  - (1995, Comedy|Drama)
  - (1995, Comedy|Drama|Romance)

多重聚合结果（前10行）：
                       rating                    movieId
                         mean max count             count
year genres                                              
1995 Adventure|Children|Fantasy  3.5  3.5     1               1
     Animation|Children|Comedy   4.0  4.0     1               1
     Comedy                     3.0  3.0     1               1
     Comedy|Drama               3.5  3.5     1               1
     Comedy|Drama|Romance       3.5  3.5     1               1
     Comedy|Romance             3.0  3.0     1               1
     Crime|Thriller             4.0  4.0     1               1
     Documentary                4.5  4.5     1               1
     Drama                      4.0  4.0     1               1
     Drama|Romance              3.5  3.5     1               1
```

**关键解释**：
1. **多列分组**：`.groupby(['year', 'genres'])`创建了二维分组，每个组由(year, genres)唯一标识
2. **多重聚合**：可以同时对不同列应用不同聚合函数，甚至对同一列应用多个聚合函数
3. **结果结构**：多重聚合的结果是MultiIndex的DataFrame，列有两层：第一层是原始列名，第二层是聚合函数名

### 动手练习3：实战分析任务

**任务**：基于添加了年份列的数据，完成以下分析：

1. 找出1995年平均评分最高的电影类型：
```python
# [请在此处填写代码]
```

2. 计算每年（year）的电影总数：
```python
# [请在此处填写代码]
```

3. 输出一个完整的分析报告，包含：
   - 每年的电影数量
   - 每个类型的平均评分（按年份）
   - 评分最高的类型-年份组合

**提示**：
- 使用`.groupby()`和`.agg()`的组合
- 使用`.sort_values()`排序
- 使用`.head()`查看前几条结果

### 掌握验证3：综合理解

请回答以下问题，检验对数据聚合的全面理解：

1. 数据聚合的核心步骤是什么？（两步）
2. 什么时候需要使用多列分组？
3. 聚合结果如何帮助业务决策？（举例说明）

**答案提示**：
1. 分组（`.groupby()`）→ 聚合（`.agg()`）
2. 需要同时按多个维度分析时（如按年份+地区+产品类别）
3. 例如：发现某类电影在特定年份评分最高，可以指导内容采购策略

---

## 🎓 今日总结与下一步

### 今日掌握清单
经过今天上午的学习，你现在能够：

✅ **按列分组**：使用`.groupby()`将数据按指定列分成多个小组  
✅ **聚合计算**：使用`.agg()`对每个分组计算统计量（平均值、计数、最大值等）  
✅ **多维度分析**：同时按多列分组，进行多重聚合计算  
✅ **实际应用**：用分组聚合回答业务问题（如"各类型平均评分"、"每年电影数量"）

### 与前期知识串联
现在你掌握了Pandas的**数据加载**→**数据筛选**→**数据聚合**完整链条：
- **Day 1**：学会把数据"拿进来"（`pd.read_csv()`）
- **Day 2**：学会"挑出"想要的数据（条件筛选、排序）
- **Day 3**：学会"分析"数据的模式和规律（分组聚合）

### 交叉学习衔接
**今天下午**，我们将学习Linux权限管理（`chmod`、`sudo`），这是部署数据分析服务时的必备技能：

- **为什么需要权限管理**：当你写的Python脚本需要读取/写入系统文件时，需要正确设置文件权限
- **实际场景**：下午的练习会涉及为数据分析脚本设置执行权限，确保脚本能正常运行
- **完整工作流**：上午分析数据 → 下午部署脚本 = 端到端的数据分析工程师能力

### 下一步行动

1. **立即练习**：完成今天上午的动手练习，确保真正掌握三个知识点
2. **复习回顾**：下午学习前，快速浏览今天上午的要点（5分钟）
3. **知识串联**：思考如何将今天学的聚合函数，应用到前两天学过的筛选场景中

---

## 💡 扩展思考（选做）

如果你已经掌握今天的内容，可以挑战以下问题：

1. **实际数据挑战**：如果真实电影数据有100万行、50个列，分组聚合时如何提高性能？
2. **业务场景迁移**：将电影分析的分组聚合思路，迁移到电商销售数据分析中（商品类别、月份、销售额）
3. **技术进阶**：了解Pandas的`.transform()`和`.apply()`函数，它们与`.agg()`有什么异同？

---

## 📚 参考资料

- **Pandas官方文档**：[Group By: split-apply-combine](https://pandas.pydata.org/docs/user_guide/groupby.html)
- **常用聚合函数**：`mean`, `sum`, `count`, `min`, `max`, `std`, `var`, `first`, `last`
- **下一步学习**：数据可视化（Matplotlib）、数据清洗（缺失值处理）、高级分组技巧

---

**学习进度**：🎉 恭喜完成Week 1 Day 3上午的学习！  
**下一节**：Linux权限管理（今天下午）
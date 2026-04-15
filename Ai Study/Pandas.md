# 导入pandas库、读取CSV文件
```python
import pandas as pd
#假设movies.csv在data目录下
movies_df=pd.read_csv('date/movies_sample.csv')
```
>[!note]- 代码执行说明
>**第一行**：`import pandas as pd`
> -  导入pandas库，并起一个简称`pd`
> -  行业惯例，所有人都这么写
>## **第四行**：`movies_df = pd.read_csv(...)`
>- 调用`pd.read_csv()`函数
>-  将结果赋值给变量`movies_df`
>- 文件名用引号括起来（字符串

# .head() 预览数据前几行
核心用途：
>快速查看`DataFrame`的前几行数据，了解数据结构和内容。
>为什么需要这个方法？
>>- 只需要看前几行就能了解：
    - 有哪些列（字段）
    - 数据的格式
    - 大致内容
```python
# 接上面的代码，movies_df已经加载了数据
# 查看前5行数据 
print(movies_df.head()) 
# 可选：查看前3行 
print(movies_df.head(3))
```
# .shape属性
- 中文：形状
- 音标：/ʃeɪp/
- 用途：返回DataFrame的行数和列数（元组格式）
```python
#查看movies_df有多少行、多少列
print("数据维度：",movies_df.shape)
```
# 练习
## 练习一  加载电影数据
```python
# 请补全代码
import pandas as pd

# 读取电影数据文件
movies_df = ___pd.read_csv_____('data/movies_sample.csv')

# 查看前5行
print(movies_df.___head____(5))
```
## 练习二  查看数据维度
```python
# 接续上面的代码
# 查看movies_df有多少行、多少列
print("数据维度：", movies_df.__shape______)
```
## 练习三：自定义查看行数
```python
# 查看movies_df的前3行
print(movies_df.___head_____(____3____))
```
## 练习四：加载评分数据并查看
```python
# 读取评分数据文件
ratings_df = ___pd.read_csv_____('data/_____ratings___.csv')

# 查看评分数据的前10行
print(ratings_df.____head____(____10____))
```

# `.iloc[]`索引器
[[课件/day2_pandas#1. 问题引入#]]
# 条件筛选 df[条件表达式]
[为什么要学条件筛选？](课件/day2_pandas.md#为什么要学条件筛选？)
```python
#一、筛选评分大于4.0的电影
high_rating_movies = df[df['rating'] > 4.0]

# 二. 多条件组合（与运算）
# 使用 & 符号连接多个条件，每个条件要用括号括起来
action_high_rating = df[(df['genres'].str.contains('Action)) & (df['rating'] > 3.5)]
#选择评分大于3.5的武打片

#三、多条件组合（或运算）
# 使用 | 符号连接多个条件
comedy_or_animation = df[(df['genres'].str.contains('Comedy')) | (df['genres].str.contains('Animation'))]
#喜剧 或者 动画 的电影，全部筛选出来！
print("动作片且评分>3.5的电影（共{}部）：".format(len(action_high_rating)))
# `{}` 是一个占位符，表示 “这里要放一个变量的值”
# `.format(...)` 就是把括号里的内容（这里是电影数量）填到 `{}` 的位置

#四、范围筛选（between）
# 筛选评分在某个范围内的电影
mid_rating_movies = df[df['rating'].between(3.0,4.0)]
#评分在3.0-4.0之间的电影

#五、字符串包含筛选（contains）
# 筛选类型中包含特定关键词的电影
drama_movies = df[df['genres'].str.contains('Drama')]
print("剧情片共{}部",format(len(drama_movies))
#剧情片共几部
```
<details>
<summary>条件筛选的底层逻辑</summary>
1.<strong> df['rating'] > 4.0</strong> &nbsp会产生一个布尔序列（长度和DataFrame行数相同）<br>
2. <span style="color:red">每个位置是True或False，表示该行是否满足条件</span><br>
3. <strong>df[布尔序列]</strong> 只保留True对应的行<br>
</details>
# .sort_values()排序
## 核心概念
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
#基本升序排序（默认）
#语法：df.sort_values(by='列名')
sorted_by_rating_asc = df.sort_values(by='rating')
#按照升序排序

#降序排序
# 使用 ascending=False 参数
sorted_by_movies_desc = df.sort_values(by='rating',ascending=False)

#多列排序
#先按评分降序，评分相同再按movieId升序
multi_sorted = df.sort_values(['rating','movieId'],ascending=[False,True])

#排序后重置索引
# 排序后索引会乱序，使用 reset_index() 重新编号
sorted_reset = df.sort_values(by='rating', ascending=False).reset_index(drop=True)
```
### 排序的注意事项
1. **原地排序**：可以使用 `inplace=True` 参数直接修改原DataFrame
2. **缺失值处理**：默认NaN会被放在排序结果的最后
3. **性能考虑**：大数据集排序可能较慢，考虑是否需要全部排序
```python
#原地排序示例（会修改原df，谨慎使用）
df_copy=df.copy()#创建副本，以防影响后续操作
df_copy=sort_values(by='rating',ascending=False,inplace=True)
```
### 动手练习：排序实战
```python
# 任务7：按电影ID（movieId）升序排序，查看排序后的前15部电影
# 提示：使用sort_values，by参数指定'movieId'
df_movieId_asc=df.sort_values(by='movieId',ascending=True)
print(df_movieId_asc.head(15))
# 任务8：按评分从低到高排序（升序），查看评分最低的10部电影
# 提示：ascending=True是默认值，可以省略
df_rating_asc=df.sort_values(by='rating',ascending=True)
print(df_rating_asc.head(10))
# 任务9：创建电影评分排行榜（降序排序），并重置索引
# 提示：先排序，再reset_index(drop=True)
df_sorted_desc=df.sort_values(by='rating',ascending=False).reset_index(drop=True)
```
### 综合练习：电影数据分析师任务
假设你是一家流媒体平台的数据分析师，收到以下业务需求：
```python
# 需求1：查看平台中间部分的电影质量（第150-160行）
mid_quality=df.iloc[149:160]
print(mid_quality)
# 需求2：筛选出高质量动作片（评分>4.0且类型含Action）
high_quality_action=df[(df['genres].str.contains('Action')) &
(df['rating'] > 4.0)]
# 需求3：制作不同类型的电影排行榜
# 3.1 喜剧片排行榜（降序）
comedy_desc_rank=df[df['genres'].str.contains('comedy')]
.sort_values(by='rating',ascending=False)
.reset_index(drop=True)
# 3.2 动画片排行榜（降序）
animation_desc_rank=df[df['genres'].str.contains('animation')]
.sort_values(by='rating',ascending=False)
.reset_index(drop=True)
```
# .groupby() 按列分组
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
**关键解释**：
- `movies_df.groupby('genres')`：按`genres`列的值进行分组
- `groups`：是一个`DataFrameGroupBy`对象，不是普通的DataFrame
- `groups.ngroups`：返回分组的数量（这里20种不同的类型组合）
- `groups.groups.keys()`：返回每个分组的名称（即genres的值）
# .agg() 聚合计算
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
**语法分解**：
- `movies_df.groupby('genres')`：按genres分组
- `['rating']`：只选择rating列进行后续计算（可选，如果不指定则对所有数值列计算）
- `.agg('mean')`：对每个分组计算平均值
- 其他常用聚合函数：`'count'`, `'sum'`, `'min'`, `'max'`, `'std'`
# **多列分组与多重聚合**
 ### 问题引入
我们学会了按单列分组（如`genres`），但真实分析中经常需要：
- 同时按年份**和**类型分组
- 对每个分组计算多个统计量（如平均评分+电影数量）
### 多列分组
语法：`.groupby(['列1', '列2', ...])`
**示例**：假设我们有年份列`year`，想同时按年份和类型分组
```python
# 假设数据中有year列
multi_group = movies_df.groupby(['year', 'genres'])
```
### 多重聚合
语法：`.agg({'列名1': '聚合函数1', '列名2': ['聚合函数1', '聚合函数2']})`

**示例**：对rating列计算平均值和最大值，对movieId列计数
```python
# 假设数据中有year列
 result = movies_df.groupby(['year', 'genres']).agg({
     'rating': ['mean', 'max'],
     'movieId': 'count'
 })
```
### 实际应用：模拟年份数据
由于我们的数据集没有年份列，我们模拟一个简单场景：添加虚拟年份列。
```python
# 知识点3：多列分组与多重聚合
# 首先，我们为数据添加一个虚拟年份列（仅用于教学）
# 在实际项目中，年份可能从title中提取或来自其他数据源
import numpy as up

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
**关键解释**：
1. **多列分组**：`.groupby(['year', 'genres'])`创建了二维分组，每个组由(year, genres)唯一标识
2. **多重聚合**：可以同时对不同列应用不同聚合函数，甚至对同一列应用多个聚合函数
3. **结果结构**：多重聚合的结果是MultiIndex的DataFrame，列有两层：第一层是原始列名，第二层是聚合函数名
**任务**：基于添加了年份列的数据，完成以下分析：

4. 找出1995年平均评分最高的电影类型：
```python
movies_1995 = movies_df[movies_df['years'] == 1995]
avg_rating_1955=movies_1955.group('genres')['rating'].mean
high_rating_1955=avg_rating_1955.idmax()
```

2. 计算每年（year）的电影总数：
```python

```

# w3school
## 使用index参数可以自定义标签
```python
import pandas as pd
a = [1,7,2]
myvar = pd.Series(a,index = ['x','y','z'])
print(myvar)
#实例：返回 "y" 的值：
print(myvar['y'])
```
## 在创建Series时，还可以使用键/值对象，如字典
```python
#从字典创建一个简单的Pandas Series
import pandas as pd
calories = {'day1':420,'day2':380,'day3':390}
myvar = pd.Series(calories)
print(myvar)
```
**注意：** 字典的键成为标签。
若要选择字典中的某些项，请使用 `index` 参数并仅指定要包含在 Series 中的项。
实例：仅使用 "day1" 和 "day2" 的数据创建一个 Series：
```python
import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)
```
## 数据帧（DateFrames）
- Pandas 中的数据集通常是多维表，称为数据帧。
- Series 就像一列，而数据帧是整个表。
实例：从两个Series创建一个数据帧：
```python
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)
```
## 什么是DateFrame？
Pandas DataFrame 是二维数据结构，就像二维数组，或者带有行和列的表格。
### 实例
创建一个简单的 Pandas DataFrame：
```python
import micropip 
await micropip.install("pandas")

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
# 将数据加载到 DataFrame 对象中：
df = pd.DataFrame(data)
print(df)
```
<details>
<summary>定位行</summary>
从上面的结果可以看出，DataFrame 就像一个有行和列的表格。
Pandas 使用 `loc` 属性返回一行或多行指定行。
</details>
### 实例
返回第 0 行：
```python
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
# 将数据加载到 DataFrame 对象中：
df = pd.DataFrame(data)
print(df.loc[0])
#返回第 0 行和第 1 行：
#使用索引列表：
print(df.loc[[0, 1]])
```
 #引用行索引：
**注意**: 当使用 `[]` 时，结果是 Pandas _DataFrame_。
<details>
<summary><strong>命名索引</strong></summary> 

使用 `index` 参数，您可以命名自己的索引。

</details>
### **实例**
添加一个名称列表，为每一行命名：
```python
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)
```
<details>
<summary><strong>定位命名索引</strong></summary> 
<b><span style="color: #F44336;">loc</span></b>：**按索引的 “名字” 取行**（自定义索引后必须用名字）<br>
<b><span style="color: #F44336;">iloc</span></b>：**按行的 “位置” 取行**（永远用 0,1,2...，和索引名字无关）
</details>
## 将文件加载到DateFrame中
如果数据集存储在文件中，Pandas 可以将它们加载到 DataFrame 中。
### 实例
将逗号分隔的文件（CSV 文件）加载到 DataFrame 中：
```python
import pandas as pd
df = pd.read_csv('date.csv')
print (df)
```
## 读取CSV文件
存储大型数据集的简单方法是使用 CSV 文件（逗号分隔的文件）。
CSV 文件包含纯文本，是一种众所周知的格式，可以被每个人（包括 Pandas）读取。
### **实例**
```python
import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string())
```
<b><span style="color: orange;">提示:</span></b>使用 <span style="color: #F44336;">to_string()</span>打印整个 DataFrame。
如果你有一个包含很多行的大型 DataFrame，Pandas 将仅返回前 5 行和最后 5 行：
### **实例**
不使用 <span style="color: #F44336;">to_string()</span> 方法打印 DataFrame：
```python
import pandas as pd
df = pd.read_csv('date_csv')
print(df)
```
<span style="font-size: 22px;color:red">总结</span>
**不用 to_string ()**：打印表格，**数据多了会自动省略**，好看但不全。
**用 to_string ()**：打印**纯文本**，**所有内容全部显示，不省略**。
## max_rows 返回的行数在 Pandas 选项设置中定义。
您可以使用 <b><span style="color: #F44336;">`pd.options.display.max_rows`</span></b> 语句检查系统的最大行数
### **实例**
检查返回的最大行数：
```python
import pandas as pd
print(pd.options.display.max_rows)
```
在我的系统中，数字是 60，这意味着如果 DataFrame 包含超过 60 行，则 `print(df)` 语句将仅返回标题以及前 5 行和最后 5 行。

可以使用相同的语句更改最大行数。
### **实例**
```python
import pandas as pd
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df)
```
## 读取 JSON
大型数据集通常以 JSON 格式存储或提取。
JSON 是纯文本，但具有对象的格式，在编程领域（包括 Pandas）中广为人知。
在我们的例子中，我们将使用一个名为 'data.json' 的 JSON 文件。
### **实例**
将JSON文件加载到DateFrame中：
```python
import pandas as pd
df = pd.read_json('data.json')
print(df.to_string())
```
<b><span style="color: green">提示：</span></b>使用 `to_string()` 打印整个 DataFrame。
## 字典作为JSON
**JSON = Python 字典**
JSON 对象与 Python 字典具有相同的格式。
如果您的 JSON 代码不在文件中，而是在 Python 字典中，您可以直接将其加载到 DataFrame 中：
### **实例**
将Python字典加载到DateFrame中：
```python
import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df)
```
## 查看数据
获取 DataFrame 快速概览最常用的方法之一是使用 <span style="color: #F44336;">`head()`</span> 方法。
<span style="color: #F44336;">`head()`</span> 方法从顶部开始返回表头和指定数量的行。
### **实例**
通过打印DateFrame的前10行来快速预览：
```python
import pandas as pd
df = pa.read_csv('date.cas')
print(df.head(10))
```
**注意:** 如果未指定行数，`head()` 方法将返回前 5 行。
还有一个 <span style="color: #F44336;">`tail()` </span>方法用于查看 DataFrame 的最后几行。
<span style="color: #F44336;">`tail()`</span>方法从底部开始返回表头和指定数量的行。
## 有关数据的信息
DataFrame对象有一个名为<b><span style="color: #F44336;">info()</span></b>的方法，可以提供有关数据集的更多信息。
### 实例
打印有关数据的信息：
```pthon
print(df.info())
```
**结果**
```bash
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 169 entries, 0 to 168
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   Duration  169 non-null    int64  
 1   Pulse     169 non-null    int64  
 2   Maxpulse  169 non-null    int64  
 3   Calories  164 non-null    float64
dtypes: float64(1), int64(3)
memory usage: 5.4 KB
None
```
**结果说明**
结果告诉我们有169行和4列
```bash
RangeIndex: 169 entries, 0 to 168
Data columns (total 4 columns):
```
以及每列的名称和数据类型：
```bash
#   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   Duration  169 non-null    int64  
 1   Pulse     169 non-null    int64  
 2   Maxpulse  169 non-null    int64  
 3   Calories  164 non-null    float64
```
**控制**
<b><span style="color: #F44336;">`info()`</span></b> 方法还告诉我们每列中存在多少个非空值，而在我们的数据集中，"Calories" 列中似乎有 164 个非空值。
这意味着出于某种原因，"Calories" 列中有 5 行完全没有值。
在分析数据时，空值或 Null 值可能是有害的，您应该考虑删除具有空值的行。这是迈向所谓数据清洗的一步，您将在接下来的章节中了解更多信息。
## 数据清洗
数据清理意味着修复数据集中的不良数据。
不良数据可能是：
- 空单元格
- 格式错误的数据
- 错误的数据
- 重复项
**我们的数据集**
```DataFrame
    Duration          Date  Pulse  Maxpulse  Calories
0         60  '2020/12/01'    110       130     409.1
1         60  '2020/12/02'    117       145     479.0
2         60  '2020/12/03'    103       135     340.0
3         45  '2020/12/04'    109       175     282.4
4         45  '2020/12/05'    117       148     406.0
5         60  '2020/12/06'    102       127     300.0
6         60  '2020/12/07'    110       136     374.0
7        450  '2020/12/08'    104       134     253.3
8         30  '2020/12/09'    109       133     195.1
9         60  '2020/12/10'     98       124     269.0
10        60  '2020/12/11'    103       147     329.3
11        60  '2020/12/12'    100       120     250.7
12        60  '2020/12/12'    100       120     250.7
13        60  '2020/12/13'    106       128     345.3
14        60  '2020/12/14'    104       132     379.3
15        60  '2020/12/15'     98       123     275.0
16        60  '2020/12/16'     98       120     215.2
17        60  '2020/12/17'    100       120     300.0
18        45  '2020/12/18'     90       112       NaN
19        60  '2020/12/19'    103       123     323.0
20        45  '2020/12/20'     97       125     243.0
21        60  '2020/12/21'    108       131     364.2
22        45           NaN    100       119     282.0
23        60  '2020/12/23'    130       101     300.0
24        45  '2020/12/24'    105       132     246.0
25        60  '2020/12/25'    102       126     334.5
26        60    2020/12/26    100       120     250.0
27        60  '2020/12/27'     92       118     241.0
28        60  '2020/12/28'    103       132       NaN
29        60  '2020/12/29'    100       132     280.0
30        60  '2020/12/30'    102       129     380.3
31        60  '2020/12/31'     92       115     243.0
```
>该数据集包含一些空单元格（第 22 行中的 "Date"，第 18 行和第 28 行中的 "Calories"）。
>数据集包含错误的格式（第 26 行中的 "Date"）。
>数据集包含错误数据（第 7 行中的 "Duration"）。
>该数据集包含重复项（第 11 行和第 12 行）。
### **空单元格**
在分析数据时，空单元格可能会带来错误的结果
**删除行**
处理空单元格的一种方法是删除包含空单元格的行。
这通常是可行的，因为数据集可能非常大，删除几行不会对结果产生很大影响。
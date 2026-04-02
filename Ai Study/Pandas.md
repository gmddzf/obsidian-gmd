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

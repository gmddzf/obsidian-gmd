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
### 为什么要学`.iloc[]`？
在实际工作中，数据文件可能有成千上万行，我们经常需要：
- 查看开头、中间、结尾的不同部分
- 抽取特定位置的数据进行抽查验证
- 处理大型数据时，只加载部分行以节省内存


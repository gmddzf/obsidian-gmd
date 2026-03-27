### 一、基础入门（创建与查看表格）

```python
import pandas as pd
'''创建字典，转换为DataFrame表格'''
date = {
    "姓名":["张三","李四","王五"],
    "分数":[10,20,30],
    "专业":["语文","数学","英语"]
}
df=pd.DataFrame(date)  # 把字典转换为表格
print("基础表格：")
print(df)
# 读取单列数据
print("姓名列：", df["姓名"])
# 读取多列数据（列表包裹列名）
print("分数+专业列：", df[["分数","专业"]])
# 筛选满足条件的行（分数>10）
print("分数>10的记录：", df[df["分数"]>10])
```

```python
import pandas as pd
'''创建字典，转换为DataFrame表格'''
date = {
    "姓名":["张三","李四","王五"],
    "分数":[10,20,30],
    "专业":["语文","数学","英语"]
}
df=pd.DataFrame(date)  # 把字典转换为表格
print("基础表格：")
print(df)
# 读取单列数据
print("姓名列：", df["姓名"])
# 读取多列数据
print("分数+专业列：", df[["分数","专业"]])
# 筛选满足条件的行（分数>10）
print("分数>10的记录：", df[df["分数"]>10])
```

### 二、表格读取与保存

```python
df=pd.read_excel("学生信息.xlsx")  # 读取Excel文件
print(df)
df.to_excel("保存后的学生信息.xlsx", index=False)  # 保存表格，不生成多余序号
```

### 三、数据清洗（核心操作）

```python
# 1. 查看空值（核心操作）
df=pd.read_excel("学生信息.xlsx")
print("各列空值数量：", df.isnull().sum())

# 2. 删除空值行（无需重新赋值，原地修改）
df.dropna(inplace=True)
print("删除空值后：")
print(df)

# 3. 替换内容（专业列）
df["专业"]=df["专业"].replace("计算机","软件")  # 单个替换
# 多值替换（字典形式）
df["专业"]=df["专业"].replace({
    "计算机":"软件",
    "电气":"电子信息"
})

# 4. 修改列名（重点：将“分数”改为“总成绩”）
# 方式1：单个列名修改（最常用，精准高效）
df.rename(columns={"分数": "总成绩"}, inplace=True)
# 方式2：多个列名修改（可搭配使用，示例）
# df.rename(columns={"分数": "总成绩", "专业": "所学专业"}, inplace=True)
print("修改列名后（分数→总成绩）：")
print(df)

# 5. 删除重复行（两种方式）
df.drop_duplicates(inplace=True)  # 删除所有重复行
df.drop_duplicates(subset=["姓名"], keep="first", inplace=True)  # 按姓名去重，保留第一个
print("去重后：")
print(df)

# 6. 删除列（重点：以删除“年级”列为例）
# 方式1：drop()方法（最常用，推荐），inplace=True表示原地修改
df.drop(columns=["年级"], inplace=True)
# 方式2：del关键字（简单直接，适合单个列删除）
del df["年级"]
# 方式3：删除多列（示例，可搭配使用）
# df.drop(columns=["年级", "性别"], inplace=True)
print("删除“年级”列后：")
print(df)
```

### 四、数据统计与分析

```python
df=pd.read_excel("学生信息.xlsx")
# 1. 数字列统计（分数相关）
print("分数统计：")
print(df["分数"].describe())  # 包含计数、均值、最值等
# 统计说明（嵌入代码注释，不单独列出）
# count：有效数据量；mean：平均分；min/max：最值

# 2. 分组统计
result=df.groupby("专业")["分数"].agg([
    "count",  # 人数
    "mean",   # 平均分
    "max",    # 最高分
    "min"     # 最低分
])
print("按专业分组统计：")
print(result)

#3. 取前五名
top5_students = df.nlargest(5, "分数") 
# 取分数前5名，5是数量，"分数"是排序列
```

### 五、表格排序与索引重置

```python
df=pd.read_excel("学生信息.xlsx")
# 按分数倒序排序
df=df.sort_values(by="分数", ascending=False)
# 重置索引（删除旧行号）
df=df.reset_index(drop=True)
print("排序并重置索引后：")
print(df)
```

### 六、综合练习题（核心操作汇总）

```python
# 综合练习题（完整流程，可直接运行）
df=pd.read_excel("学生信息.xlsx")
# 1. 删除空值行
df.dropna(inplace=True)
# 2. 按姓名去重（保留第一个）
df.drop_duplicates(subset=["姓名"], keep="first", inplace=True)
# 3. 替换专业名称（计算机→计算机科学）
df["专业"]=df["专业"].replace("计算机","计算机科学")
# 4. 按分数倒序排序，重置索引
df.sort_values(by="分数", ascending=False, inplace=True)
df.reset_index(drop=True, inplace=True)
# 5. 新增加分后列
df["加分后"]=df["分数"]+10
# 6. 新增等级列（条件赋值）
df.loc[df["分数"]>=600,"等级"]="优秀"
df.loc[(df["分数"]>=500) & (df["分数"]<600),"等级"]="合格"
df.loc[df["分数"]<500,"等级"]="不合格"
# 7. 筛选高分+对应专业记录
df_1=df.loc[(df["分数"]>=550) & (df["专业"]=="计算机科学")]
print("筛选结果：")
print(df_1)
# 8. 保存处理后的表格
df.to_excel("处理后学生信息.xlsx", index=False)
print("表格已保存！")

```

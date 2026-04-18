# 线性回归
## 第1行：导入线性回归
```python
form sklearn.linear_model import LinearRegression
```
>从 sklearn 这个工具箱里，把“线性回归”这个工具拿出来。
- sklearn= 一个机器学习工具箱
-  `linear_model` = 工具箱里的“线性模型”区域
- `LinearRegression` = 线性回归这个具体工具
## 第2行：导入numpy
```python
import numpy as np
```
>把 numpy 这个数学库叫进来，并给它起个昵称 np。
>>为什么要用 numpy？
>>因为 sklearn 要求数据必须是“数组格式”，numpy 就是专门处理数组的。
## 第3~4行：准备数据x和y
~~~python
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([50, 60, 65, 70, 80])
~~~
>**x:输入（学习时间）**
>>`[[1], [2], [3], [4], [5]]`
>>这是 5 个学生的学习时间
>>每个数字外面套一层 `[]` 是 sklearn 的要求（二维数组）
>**x= 输入特征（学习了多少小时）**
>
>**y:输出（考试分数）**
>> `[50, 60, 65, 70, 80]`
>>这是 5 个学生的真实分数
>**y=要预测的结果（考了多少分）**
## 第5行：创建模型
~~~python
model = LinearRegression()
~~~
>**创建一个线性回归模型对象，叫model**
>>就像你说：
>>>给我一个空的线性回归模型，我等会要训练它
## 第6行：训练模型
~~~python
model.fit(X, y)
~~~
>**把X和y喂给模型，让它学会"学习时间→分数"的关系**
>>fit = 训练
>可以理解为：
>“model，你看一下这些学生的学习时间和分数，自己找出规律。”
## 第7~8行：查看训练结果
~~~python
print("斜率 a =", model.coef_)
print("截距 b =", model.intercept_)

~~~
**🌟 这两行会告诉你模型学到的公式：**
$$
𝑦
=
𝑎
𝑥
+
𝑏
$$
- `coef_` = 斜率 a
- `intercept_` = 截距 b
你会看到类似：
- a = 7.5
- b = 42
意思是：
>每多学1小时，分数大概涨7.5分
~~~python
model.predict([[6]])

~~~
**让 模型预测“学6个小时”会考多少分**
# 可视化线性回归
```python
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt  # 新增：画图用

# 1. 准备数据
X = np.array([[1], [2], [3], [4], [5]])   # 学习时间
y = np.array([50, 60, 65, 70, 80])        # 分数

# 2. 创建并训练模型
model = LinearRegression()
model.fit(X, y)

# 3. 打印参数
print("斜率 a =", model.coef_)
print("截距 b =", model.intercept_)

# 4. 画散点图（原始数据）
plt.scatter(X, y, color="blue", label="真实数据")

# 5. 画回归直线
X_line = np.linspace(1, 5, 100).reshape(-1, 1)   # 在 1~5 之间取很多点
y_line = model.predict(X_line)                   # 用模型预测这些点
plt.plot(X_line, y_line, color="red", label="回归直线")

# 6. 美化一下图
plt.xlabel("学习时间（小时）")
plt.ylabel("考试分数")
plt.legend()
plt.title("学习时间 vs 分数 的线性回归")

plt.show()

```
1. plt.scatter(X,y,...)
- 把原始数据画成蓝色小点
- 每个点=一个学生（学习时间，分数）
>**可以把它理解成：**
>>先把真实情况画出来
2. plt.plot(X_line, y_line, ...)
- `X_line`：在 1 到 5 之间取很多“学习时间”的点
- `model.predict(X_line)`：模型对这些点的预测分数
- 把这些点连起来，就是那条红色直线
>**可以把它理解成：**
>>把模型学到的那条直线画出来
# 线性回归
## 基础部分

### 第1行：导入线性回归
```python
form sklearn.linear_model import LinearRegression
```
>从 sklearn 这个工具箱里，把“线性回归”这个工具拿出来。
- sklearn= 一个机器学习工具箱
-  `linear_model` = 工具箱里的“线性模型”区域
- `LinearRegression` = 线性回归这个具体工具
### 第2行：导入numpy
```python
import numpy as np
```
>把 numpy 这个数学库叫进来，并给它起个昵称 np。
>>为什么要用 numpy？
>>因为 sklearn 要求数据必须是“数组格式”，numpy 就是专门处理数组的。
### 第3~4行：准备数据x和y
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
### 第5行：创建模型
~~~python
model = LinearRegression()
~~~
>**创建一个线性回归模型对象，叫model**
>>就像你说：
>>>给我一个空的线性回归模型，我等会要训练它
### 第6行：训练模型
~~~python
model.fit(X, y)
~~~
>**把X和y喂给模型，让它学会"学习时间→分数"的关系**
>>fit = 训练
>可以理解为：
>“model，你看一下这些学生的学习时间和分数，自己找出规律。”
### 第7~8行：查看训练结果
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
## 可视化线性回归
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
## 多点预测
~~~python
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([50, 60, 65, 70, 80])

model = LinearRegression()
model.fit(X, y)

print("斜率 a =", model.coef_)
print("截距 b =", model.intercept_)
print("预测学 6 小时的分数 =", model.predict([[6]]))

# 预测多个学习时间的分数
X_test = np.array([[6], [7], [8]])   # 学 6、7、8 小时
y_pred = model.predict(X_test)

print("预测结果：")
for x, y_hat in zip(X_test.flatten(), y_pred):
    print(f"学 {x} 小时 -> 预测分数 {y_hat:.2f}")
~~~
**1、新加的第一行**
~~~python
X_test = np.array([[6], [7], [8]])   # 学 6、7、8 小时
~~~
- `X_test` 就是我们要测试的新输入数据。
- 它的格式和之前的 `X` 一样：二维数组，每个里面一个数字。
- 这里表示：我们想让模型预测 **学 6 小时、7 小时、8 小时**的分数。
**2、新加的第二行**
~~~python
y_pred = model.predict(X_test)

~~~
- `model.predict(...)` 就是用训练好的模型来预测结果。
- 输入是 `X_test`（学 6、7、8 小时）。
- 输出是 `y_pred`，里面存的是模型预测的分数。
**3、新加的第三部分（循环打印）**
~~~python
print("预测结果：")
for x, y_hat in zip(X_test.flatten(), y_pred):
    print(f"学 {x} 小时 -> 预测分数 {y_hat:.2f}")
~~~
- `zip(X_test.flatten(), y_pred)`
    - 把学习时间和预测分数一一配对。
    - 比如 (6, 87.5), (7, 95.0), (8, 102.5)。
-  `print(f"学 {x} 小时 -> 预测分数 {y_hat:.2f}")`
    - 用 f-string 打印结果。
    - `{y_hat:.2f}` 表示保留两位小数。
    - 输出会像这样：
~~~code
学 6 小时 -> 预测分数 87.50
学 7 小时 -> 预测分数 95.00
学 8 小时 -> 预测分数 102.50
~~~
**一、numpy的核心知识**
**1、创建数组**
~~~python
import numpy as np
X = np.array([[1], [2], [3]])
~~~
- `np.array` 就是把普通的 Python 列表 `[1,2,3]` 变成 numpy 数组。
- sklearn 要求输入必须是这种数组格式。
**2、二维vs一维**
- `[[1], [2], [3]]` → 二维数组（每个数字外面再套一层方括号）
- `[1, 2, 3]` → 一维数组 sklearn 要求输入特征是二维的，所以我们写成 `[[1],[2],[3]]`。
**3、常用操作**
-  `.reshape(-1,1)` → 把一维数组变成二维数组
- `.flatten()` → 把二维数组变回一维数组
👉 在刚才的代码里，`X_test.flatten()` 就是把 `[[6],[7],[8]]` 变成 `[6,7,8]`，方便打印
**二、for循环的核心知识**
**配对使用zip**
~~~python
names = ["小明", "小红"]
scores = [90, 85]

for n, s in zip(names, scores):
    print(n, s)
~~~
输出：
~~~code
小明 90
小红 85
~~~
👉 `zip` 的作用就是把两个列表里的元素一一配对。
在我们的代码里：
~~~python
for x, y_hat in zip(X_test.flatten(), y_pred):
    print(f"学 {x} 小时 -> 预测分数 {y_hat:.2f}")
~~~
就是把：
- 学习时间 `[6,7,8]`
- 预测分数 `[87.5, 95.0, 102.5]
配对成：
- (6, 87.5)
- (7, 95.0)
- (8, 102.5)
然后逐个打印出来。
### <span style="background: linear-gradient(90deg, #2196F3, #F44336); -webkit-background-clip: text; color: transparent; font-size: 22px; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">超级浓缩总结</span>
- `zip` = **把多个列表捆成一对一对**
- `for a,b in zip(list1, list2)` = **同时循环两个列表**
- AI 里用来循环 **特征 + 标签**，一对一对喂给模型
- 长度不一样 → 按**最短**的来
## 评估模型 R^2
### **⭐ 为什么要评估模型？**
到目前为止，你的模型能预测分数，但我们还不知道它到底“准不准”。 在 sklearn 里，有一些指标可以帮我们量化模型的好坏。
最简单的一个就是 **R²（决定系数）**。

### **🧩 R² 的直觉解释**

不用数学公式，只要记住：
- R² = 1 → 模型完美预测
- R² 越接近 1 → 模型越好
- R² 越接近 0 → 模型没啥用（预测效果和乱猜差不多）
- R² 甚至可能是负数 → 模型比乱猜还差
👉 所以你只要看这个数字，就能知道模型大概好不好。

### **✅ 在代码里加上 R²**
在训练完模型之后，加上这一行：
```python
print("模型的 R² =", model.score(X, y))
```
完整代码片段（放在 `fit` 之后）：
```python
model.fit(X, y)

print("斜率 a =", model.coef_)
print("截距 b =", model.intercept_)
print("模型的 R² =", model.score(X, y))
```
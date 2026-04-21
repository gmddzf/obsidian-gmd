```python
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return """
    <html>
        <head><title>我的第一个网页</title></head>
        <body>
            <h1>欢迎来到首页</h1>
            <p>这是用 Flask 返回的 HTML 页面。</p>
            <a href="/about">关于页面</a> 
        </body>
    </html>
    """

@app.route("/about")
def about():
    return "<h1>关于我们</h1>"
if __name__ == "__main__":
    app.run()
```
# 基础
## 动态插入变量
~~~python
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    user_name = "小白同学"   # 定义一个变量
    return render_template("index.html", name=user_name)
if __name__ == "__main__":
    app.run()
~~~

```html
<!DOCTYPE html>
<html>
<head>
    <title>我的第一个网页</title>
</head>
<body>
    <h1>欢迎来到首页</h1>
    <p>你好，{{ name }}！这是动态插入的变量。</p>
    <a href="/about">关于页面</a>
</body>
</html>

```
> `render_template("index.html", name=user_name)`
    这里我们把 Python 里的变量 `user_name` 传给模板。 
    在 HTML 里就能用 `{{ name }}` 来显示它。
        
- `{{ name }}`
    - 这是 Jinja2 模板语法（Flask 默认用的模板引擎）。
    - 它会把传进来的变量替换成实际的值。
    - 所以网页上会显示：`你好，小白同学！这是动态插入的变量。`
## 表单
```html
<!DOCTYPE html>
<html>
<head>
    <title>输入示例</title>
</head>
<body>
    <h1>请输入你的名字</h1>
    <form action="/hello" method="post">
        <input type="text" name="username" placeholder="名字">
        <input type="text" name="userage" placeholder="年龄">
        <button type="submit">提交</button>
    </form>
</body>
</html>
```

```python
from flask import Flask, render_template, request
app = Flask(__name__)  
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/hello", methods=["POST"])
def hello():
    name = request.form["username"]   # 获取姓名
    age = request.form["userage"] #获取年龄
    return f"<h1>你好，{name}！,你的年龄是{age}</h1>"
if __name__ == "__main__":
    app.run()
```
### **拆解**
 1. `<form action="/hello" method="post">`
- **form**：表示这是一个表单区域。
- **action="/hello"**：告诉浏览器，用户点提交后，把数据发送到网站的 `/hello` 地址。
- **method="post"**：告诉浏览器，用 **POST** 方式发送数据。

👉 为什么用 POST？
- GET：数据会直接显示在网址后面，比如 `?username=张三`。
- POST：数据藏在请求体里，不会显示在网址上，更适合提交表单。
 2. `<input type="text" name="username">`
- **input**：表示一个输入框。
- **type="text"**：说明这是一个文本框，可以输入文字。
- **name="username"**：给这个输入框起一个名字，方便 Flask 在后台识别。

👉 举例： 如果你在输入框里写了“张三”，提交后 Flask 就能用 `request.form["username"]` 拿到这个值。
 3. `<button type="submit">提交</button>`
- **button**：表示一个按钮。
- **type="submit"**：说明这是一个提交按钮，点击后会把表单里的数据发送到服务器。
- 按钮上的文字就是“提交”。
👉 如果没有这个按钮，用户就没法把输入的数据交给 Flask。
 🔍 总结
- **form**：表单区域，决定数据往哪里提交。
- **input**：输入框，用户在这里输入内容。
- **name**：输入框的名字，后台用这个名字来取值。
- **type="text"**：文本框。
- **button type="submit"**：提交按钮，点击后把数据发出去。
- **POST**：一种提交方式，数据不会显示在网址上。
### 🌱 常见的 `type` 值
1. `text`
2. 
    - 普通文本框，可以输入任何文字。
    ```html
    <input type="text" name="username" placeholder="请输入名字">
    ```
    👉 用来输入名字、地址等。
2. `password`
    - 密码框，输入的内容会显示成小点点或星号。     
    ```html
    <input type="password" name="pwd" placeholder="请输入密码">
    ```
    👉 用来输入密码，别人看不到你输入的内容。
3. `number`
    - 数字框，只能输入数字，还会出现上下箭头可以加减。   
    ```html
    <input type="number" name="age" placeholder="请输入年龄">
    ```
    👉 用来输入年龄、数量等。
4. `email`
    - 邮箱框，浏览器会检查输入的格式是不是邮箱。        
    ```html
    <input type="email" name="mail" placeholder="请输入邮箱">
    ```
    👉 如果你输入 `abc`，浏览器会提示格式不对。
5. `submit`
    - 提交按钮，点击后会把表单里的数据发送到服务器。
    ```html
    <input type="submit" value="提交">
    ```
    👉 和 `<button type="submit">提交</button>` 效果一样。
### **单选按钮（radio）和复选框（checkbox）**
- **作用：** 让用户在多个选项里只能选一个
- 写法：
```html
<form>
    <p>请选择性别：</p>
    <input type="radio" name="gender" value="male"> 男
    <input type="radio" name="gender" value="female"> 女
</form>
```
>type="radio" 表示这是单选按钮
>name="gender" 同一组单选按钮必须有相同的名字，这样才能保证只能选什么
>value="male"/value="female" 提交时传给后台的值，比如选了“男”，后台拿到的就是“male”

**复选框（checkbox）**
**作用：** 让用户可以同时选择多个选项
写法：
```html
<form>
    <p>请选择爱好：</p>
    <input type="checkbox" name="hobby" value="reading"> 阅读
    <input type="checkbox" name="hobby" value="sports"> 运动
    <input type="checkbox" name="hobby" value="music"> 音乐
</form>
```
`type="checkbox"` → 表示这是复选框。
 `name="hobby"` → 多个复选框可以用同一个名字。
 `value="reading"` 等 → 提交时传给后台的值。比如你勾选了“阅读”和“音乐”，后台就能拿到这两个值。
 
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
    <title>表单示例</title>
</head>
<body>
    <h1>欢迎来到首页</h1>
    <form action="/submit" method="post">
        <label for="name">请输入你的名字：</label>
        <input type="text" id="name" name="name">
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

@app.route("/submit", methods=["POST"])
def submit():
    user_name = request.form["name"]   # 获取表单里的数据
    return f"<h1>你好，{user_name}！</h1>"

if __name__ == "__main__":
    app.run()
```

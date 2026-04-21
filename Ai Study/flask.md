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


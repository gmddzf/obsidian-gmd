# HTTP请求结构（request Line）
## 第一部分：请求行
它包含三样东西：
- 方法（GET/POST）
- 路径（要访问的资源）
- 协议版本（HTTP/1.1)
例如：
```code
GET /weather HTTP/1.1
POST /login HTTP/1.1
```
## HTTP请求的第二部分：请求头（Headers）
作用是：告诉服务器“我是谁、我能接受什么、我带了什么格式的数据”。
比如：
```code
Content-Type:application/json
```
1. Content-Type  
    - 英文单词：Content-Type
    - 中文意思：内容的类型
    - 作用：告诉服务器"我发给你的数据是什么格式“
2. application/json
    - 英文单词：application/json
    - 中文意思：应用程序格式/JSON格式
    - 作用：告诉服务器”我发的是JSON数据“
为什么不是写成 `json`？ 因为 HTTP 的标准规定 JSON 属于一种“应用程序数据格式”，所以写成：
`application/json`
### **发送表单数据**
`application/x-www-form-urlencoded`
1. application
    - 应用程序
    - 这是一种”应用程序数据格式“，不是纯文本
2. /
    表示”类型/子类型“
3. x-www-form-urlencoded
    - x-
        - 历史遗留前缀
        - 表示”非标准但被广泛使用的格式“
    - www-form
        - 网页表单
        - 这是网页表单的数据格式
    - urlencoded
        - URL编码
        - 数据会被编码成URL的格式
        - 例如空格会变成`+`，中文会变成`%E4%BD%A0%E5%A5%BD`
    
### **发送文件**
`multipart/form-data`
1. `multipart`
    - multi+part
    - multi:多
    - part:部分
    - 多部分的
    - 这个请求体不是一整块，而是被拆成很多部分（part）
    - 因为上传文件时，数据结构很复杂：
        - 一部分是文本字段（比如 username=md）
        - 一部分是文件内容（二进制数据）
        - 一部分是文件名
        - 一部分是文件类型
2. `form-data`
    form:表单
    date:数据
    中文意思：表单的数据
    含义：这些多部分内容来自于一个HTML表单
如果上传一张图片，浏览器就会把请求体拆成这样：
```code
------boundary
Content-Disposition: form-data; name="username"

md
------boundary
Content-Disposition: form-data; name="avatar"; filename="me.png"
Content-Type: image/png

(这里是图片的二进制内容)
------boundary--
```
- 第一段是普通文本（username）
- 第二段是文件（avatar）
- 每一段都有自己的头部（Content-Disposition、Content-Type）
- 整个请求体被 boundary 分隔成多段（multi-part）
**multipart是唯一能同时装文本+文件的格式**
普通表单格式：
```Code
application/x-www-form-urlencoded
```
只能装：
```code
username=md&password=123
```
它不能装文件，因为文件是二进制，不能被URL编码。
而multipat/form-data可以这样装：
```code
------boundary
Content-Disposition: form-data; name="username"

md
------boundary
Content-Disposition: form-data; name="avatar"; filename="me.png"
Content-Type: image/png

(这里是图片的二进制内容)
------boundary--
```
- 文本字段是一段
- 文件是一段
- 每段都有自己的头部
- boundary把它们隔开
- 服务器可以逐段解析
这就是为什么 **只要有文件，就必须用multipart/form-data**
### **发送纯文本**
`text/plain`
1. `text`
    - 文本
    - 告诉服务器这是纯文本，没有复杂结构
2. `plain`
    - 纯的、简单的
    - 没有格式化的，没有标签，就是普通的文本
举例：
如果你是POST的内容是：
```code
你好，这是我的留言
```
那请求头应该写：
```code
Content-Type:text/palin
```
服务器就会按”纯文本“来解析。
### **当提交的数据是有结构的JSON用application/json**
比如：
```code
{"title":"留言","content":"你好，这是我的留言"}
```
这时候就必须用：
```code
Content-Type: application/json
```
因为服务器要按JSON的规则来解析
### **传输HTML本身**
text/html
比如：
```code
<html>
  <head><title>我的页面</title></head>
  <body><h1>你好</h1></body>
</html>
```
就必须用`text/html`
1. `text`
- **英文原词**：text
- **中文意思**：文本
- **作用**：告诉服务器这是文本数据，而不是二进制文件。
1.  `html`
- **英文原词**：HTML (HyperText Markup Language)
- **中文意思**：超文本标记语言
- **作用**：告诉服务器，这段文本是 HTML 网页格式，不是普通文本。
举例说明：
如果POST的内容是:
```html
<h1>欢迎来到我的网站</h>
<p>这是一个段落。</p>
```
那请求头应该写：
```code
Content-Type:text/html
```
意思就是：服务器你好，我发给你的是一个HTML网页，请按网页
### **提交PNG照片时**
image/png
`image`
- 图像；图片
- 告诉服务器，这是一种照片数据，而不是文本或应用数据。
`png`
- 告诉服务器，这张图片的具体格式是PNG
举例说明：
```code
Content-Type:image/png
```
<b><span style="color: #F44336;">其他的照片就是什么格式照片后面对应什么格式</span></b>

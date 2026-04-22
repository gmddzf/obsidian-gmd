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
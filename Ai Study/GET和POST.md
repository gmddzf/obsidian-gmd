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
    

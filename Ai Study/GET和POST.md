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
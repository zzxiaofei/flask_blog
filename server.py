# wsgiref 纯python编写的WSGI服务器
from wsgiref.simple_server import make_server
from hello import application

# 创建一个服务器，IP地址为空，端口8000，处理函数是application
httpd = make_server('', 8000, application)
print('Serving on port 8000...')
# 开始监听HTTP请求
httpd.serve_forever()
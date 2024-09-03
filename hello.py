"""
WSGI:Web server Gateway interface
"""


# environ:一个包含所有HTTP请求信的dict对象
# start_response: 一个发送HTTP响应的函数
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    response_body = '<h1>Hello World!</h1>'
    return [response_body.encode('utf-8')]

from urllib.parse import urlparse
import socket


# class http:
#     """This is the http class for server side operations"""
#
#     # headers = dict()
#     # parameters = dict()
#
#     def __init__(self, url, port=80):
#         # splitting a URL string into its components, or on combining URL components into a URL string.
#         self.url = urlparse(url)
#         self.port = port
#         self.host = self.url.netloc
#         self.path = self.url.path
#         self.headers = {'Host': self.host}
#         self.protocol = 'HTTP/1.0'
#         self.is_verbose = False
#         self.status_code = ''
#         self.body = ''
#         self.method = ''
#         self.params = self.url.params
#
#     def setMethod(self, method):
#         self.method = method
#
#     def setHeader(self, key, value):
#         self.headers[key] = value
#
#     def getHeader(self):
#         head = '\r\n'
#         for k, v in self.header.items():
#             head += (k + ": " + v + '\r\n')
#         return head
#
#     def http_request(self):
#         pass
#
#     def http_get(self):
#         pass
#
#     def http_post(self):
#         pass
#
#     def setStatus(self, status):
#         self.status_code = status
#
#     def getStatus_code(self):
#         if self.status_code == 200:
#             return "OK"
#         elif self.status_code == 301:
#             return "Moved Permanently"
#         elif self.status_code == 400:
#             return "Bad Request"
#         elif self.status_code == 404:
#             return "Not Found"
#         elif self.status_code == 505:
#             return "HTTP Version Not Supported"
#         else:
#             return "Unknown Error"
#
#     def getBody(self):
#         return self.body
#
#     def setVerbosity(self, verbosity):
#         self.is_verbose = verbosity
#
#     def getVerbosity(self):
#         return self.is_verbose
#
#     def complete_Form(self):
#         if self.url.query != '':
#             query = self.url.query
#         else:
#             query = ''
#
#         if self.method == 'GET':
#             self.body = self.method.upper() + '' + self.path + query + 'HTTP/1.0' + self.getHeader() + '\r\n'

def http_get(url, headers, is_verbose):
    url = urlparse(url)
    host = url.netloc
    param = url.query
    path = url.path

    request_msg = 'GET' + path
    if len(param) > 0:
        # like /get?course=networking&assignment=1'  this line
        request_msg = request_msg + '?' + param

    head_msg = ''
    if bool(headers):
        for k, v in headers.items():
            head_msg = head_msg + k + ': ' + v + '\r\n'

    request_msg = request_msg + ' HTTP/1.0\r\n' + 'Host: ' + host + '\r\n' + head_msg + '\r\n'


def http_post(url, headers, is_verbose):
    url = urlparse(url)
    host = url.netloc
    param = url.query
    path = url.path

    request_msg = 'POST ' + path + ' HTTP/1.0\r\n'
    head_msg = ''
    if bool(headers):
        for k, v in headers.items():
            head_msg = head_msg + k + ': ' + v + '\r\n'


import socket
from urllib.parse import urlparse
from urllib.parse import urlsplit, parse_qs

class httpclient:
    """This is the http class for client side operations"""
    port = 80
    FORMAT = 'utf-8'

    def __init__(self, verbose, headers, url):
        """Init required params"""
        self.parsed_url = urlparse(url)
        self.verbose = verbose
        self.headers = headers
        self.host = self.parsed_url.netloc
        self.path = self.parsed_url.path
        self.query = self.parsed_url.query
        if self.parsed_url.port is not None:
            self.port = self.parsed_url.port
        #self.parsed_url.hostname

    def get(self):
        """ Build GET and send to host"""
        data = ""
        data += "GET "+self.path+"?"+self.query+" HTTP/1.1\r\n"
        data += "Host: "+self.host+"\r\n"
        data += "User-Agent: Concordia-HTTP/1.0\r\n"
        if self.headers is not None:
            data += "Accept: "+self.headers+"\r\n"
        else:
            data += "Accept: */*\r\n"
        # Pass this data to TCP Client
        self.run_client(data)

    def run_client(self,data):
        """A TCP Client"""
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #  This allows the address/port to be reused immediately instead of
        #  it being stuck in the TIME_WAIT state for several minutes, waiting for late packets to arrive.
        client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            client.connect((self.host,self.port))
            request = data.encode(self.FORMAT)
            client.sendall(request)
            # MSG_WAITALL waits for full request or error
            response = client.recv(5*len(request), socket.MSG_WAITALL)
            if self.verbose:
                print(response)
            print(response.decode(self.FORMAT))
        finally:
            client.close()
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


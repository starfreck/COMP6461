import socket
from urllib.parse import urlparse

class httpclient:
    """This is the http class for client side operations"""
    port = 80
    FORMAT = 'utf-8'
    BUFFER_SIZE = 102400

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
        request = ""
        request += "GET "+self.path+"?"+self.query+" HTTP/1.1\r\n"
        request += "Host: "+self.host+"\r\n"
        request += "User-Agent: Concordia-HTTP/1.0\r\n"
        if self.headers is not None:
            #for header in self.headers:    # Activate this for Multiple Headers
            #    request += header+"\r\n"
            request += self.headers+"\r\n"  # Activate this for Single Header
        # Ending of the request or body
        request += "\r\n"
        # Pass this data to TCP Client
        self.run_client(request)

    def run_client(self,request):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #  This allows the address/port to be reused immediately instead of
        #  it being stuck in the TIME_WAIT state for several minutes, waiting for late packets to arrive.
        client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            client.connect((self.host, self.port))
            request = request.encode(self.FORMAT)
            client.sendall(request)
            # MSG_WAITALL waits for full request or error
            response = client.recv(self.BUFFER_SIZE)
            response = response.decode(self.FORMAT)
            response = response.split("\r\n\r\n")
            print()
            if self.verbose:
                print(response[0].strip(),"\n")
            print(response[1].strip())
        finally:
            client.close()
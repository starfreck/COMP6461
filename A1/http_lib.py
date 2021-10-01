import json
import socket
from urllib.parse import urlparse

class httpclient:
    """This is the http class for client side operations"""
    port = 80
    FORMAT = 'utf-8'
    BUFFER_SIZE = 102400

    def __init__(self, verbose, headers, url, string=None, file=None):
        """Init required params"""
        self.parsed_url = urlparse(url)
        self.verbose = verbose
        self.headers = headers
        self.host = self.parsed_url.netloc
        self.path = self.parsed_url.path
        self.query = self.parsed_url.query
        if self.parsed_url.port is not None:
            self.port = self.parsed_url.port
        # Extra Params for POST
        self.string = string
        self.file = file
        #self.parsed_url.hostname

    def is_json_data(self):
        if self.headers is not None and "application/json" in self.headers:
            return True
        return False

    def to_json(self,string):
        return json.dumps(json.loads(string))

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

    def post(self):
        """ Build POST and send to host"""

        # Guard
        if self.string and self.file is not None:
            print("Either [-d] or [-f] can be used but not both.")
            return

        # Start Building our POST request
        request = ""
        request += "POST "+self.path+"?"+self.query+" HTTP/1.1\r\n"
        request += "Host: "+self.host+"\r\n"
        request += "User-Agent: Concordia-HTTP/1.0\r\n"

        # Add Headers
        if self.headers is not None:
            #for header in self.headers:    # Activate this for Multiple Headers
            #    request += header+"\r\n"
            request += self.headers+"\r\n"  # Activate this for Single Header

        # Load file as string in self.file if file is present
        if self.file is not None:
            with open(self.file, 'r') as f:
                self.file = f.read().replace('\n', '')

        # See if the data is JSON
        if self.is_json_data():
            if self.string is not None:
                self.string = self.to_json(self.string)
            if self.file is not None:
                with open(self.file, 'r') as f:
                    self.file = self.to_json(self.file)

        # Add Content-Length in Header
        if self.string is not None:
            request += "Content-Length: "+ str(len(self.string)) + "\r\n"
        if self.file is not None:
            request += "Content-Length: " + str(len(self.file)) + "\r\n"

        # Ending of the request header
        request += "\r\n"

        # Adding POST Body
        if self.string is not None:
            request += self.string
        if self.file is not None:
            request += self.file

        print(request)

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
            if self.verbose:
                print(response[0].strip(),"\n")
            print(response[1].strip())
        finally:
            client.close()



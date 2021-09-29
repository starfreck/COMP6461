import socket
import threading
import argparse

from http_lib import http


def run_server(host, port):
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # https://stackoverflow.com/questions/12362542/python-server-only-one-usage-of-each-socket-address-is-normally-permitted
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        listener.bind((host, port))
        listener.listen(5)
        print('Echo server is listening at', port)
        while True:
            conn, addr = listener.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()
    finally:
        listener.close()


def handle_client(conn, addr):
    print('New client from', addr)
    try:
        while True:
            data = conn.recv(1024)
            #print(type(data))
            print(data.decode('utf-8'))

            req = http(data)

            http_response = b"""HTTP/1.1 200 OK\r\n
Date: Mon, 27 Jul 2009 12:28:53 GMT\r\n
Server: Apache/2.2.14 (Win32)\r\n
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT\r\n
Content-Length: 88\r\n
Content-Type: text/html\r\n
Connection: Closed\r\n"""

            conn.sendall(http_response)
            conn.close()
            # if not data:
            #     break
            # conn.sendall(data)
    finally:
        conn.close()


# Usage python echoserver.py [--port port-number]
parser = argparse.ArgumentParser()
parser.add_argument("--port", help="echo server port", type=int, default=8009)
args = parser.parse_args()
run_server('', args.port)

import socket
import threading
import argparse

FORMAT = 'utf-8'


def run_server(host, port):
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #  This allows the address/port to be reused immediately instead of
    #  it being stuck in the TIME_WAIT state for several minutes, waiting for late packets to arrive.
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        listener.bind((host, port))
        listener.listen(5)
        print(f'[LISTENING] Server is listening on {port}')
        while True:
            conn, addr = listener.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f'[ACTIVE CONNECTION] {threading.active_count() - 1}')

    finally:
        listener.close()


def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.')
    try:
        while True:
            request_data = conn.recv(1024)
            print(request_data.decode(FORMAT))
            #
            # if not data:
            #     break
            # conn.sendall(data)
            http_response = b"""\
            HTTP/1.1 200 OK

            Hello, World!
            """
            conn.sendall(http_response)

    finally:
        conn.close()


# Usage python echoserver.py [--port port-number]
parser = argparse.ArgumentParser()
parser.add_argument("--port", help="echo server port", type=int, default=8007)
args = parser.parse_args()
run_server('', args.port)

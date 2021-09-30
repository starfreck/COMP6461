import socket
import argparse
import sys

FORMAT = 'utf-8'


def run_client(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #  This allows the address/port to be reused immediately instead of
    #  it being stuck in the TIME_WAIT state for several minutes, waiting for late packets to arrive.
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        client.connect((host, port))
        print("Type any thing then ENTER. Press Ctrl+C to terminate")
        while True:
            line = sys.stdin.readline(1024)
            request = line.encode(FORMAT)
            client.sendall(request)
            # MSG_WAITALL waits for full request or error
            response = client.recv(len(request), socket.MSG_WAITALL)
            print("Replied:", response.decode(FORMAT))
    finally:
        client.close()


# Usage: python echoclient.py --host host --port port
parser = argparse.ArgumentParser()
parser.add_argument("--host", help="server host", default="localhost")
parser.add_argument("--port", help="server port", type=int, default=8007)
args = parser.parse_args()
run_client(args.host, args.port)

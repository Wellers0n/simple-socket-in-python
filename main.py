import socket
import pickle
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect(("localhost", 8081))
except Exception as erro:
    print(str(erro))
    sys.exit(1)

msg_server = s.recv(4048)

data_server = pickle.loads(msg_server)

print(data_server)
import socket
import pickle

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('localhost', 8081)

socket_servidor.bind(address)

socket_servidor.listen()

print("server ON in the port ", address[1])

(socket_cliente, addr) = socket_servidor.accept()

print("Connection: ", str(addr))

data = {
    'hello': 'world'
}

dataSerialized = pickle.dumps(data)

socket_cliente.send(dataSerialized)


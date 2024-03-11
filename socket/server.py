import socket

server_address = ("localhost", 12345)

# Create Socket object
server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen()

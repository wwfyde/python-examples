import socket

server_address = ("localhost", 12345)

# Create Socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen()



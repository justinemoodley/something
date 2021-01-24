import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 60000        # Port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    print('Connecting...')
    # Creates a connection to the specified server
    client.connect((HOST, PORT))
    client.sendall(b'Hello world!!!!')
    data = client.recv(1024)

print('Received: ', data)
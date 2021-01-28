import socket

HOST = '127.0.0.1' # Standard loopback interface address (localhost)
PORT = 60000 # Port to listen on (non-privileged port are > 1023)

# Creates a new socket. socket.AF INET is the socket type for IPv4
# socket.SOCK_Stream is the socket type for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    # Tells the socket to use the specified HOST and PORT details
    server.bind((HOST, PORT))
    # Sets the socket to be a connection-mode socket, i.e on that accept incoming connections.
    # It may be called with a backlog parameter that specifies how long the queue of outstanding connections may be.
    # If the queue exceeds the backog parameter, clients will be refused a connection.
    server.listen()
    print('Listening:...')
    # The accept() method block / pauses the script and waits for a connection request.
    # Once established, it returns a socket for the new connection and the address of the remote device.
    conn, addr = server.accept()
    with conn:
        print('Connected by ', addr)

        # A continuous loop to receive data until the client closes the connection.
        while True:
            # Receives data from the remote connection.
            # At most 1024 byte will be read before blocking
            data = conn.recv(1024)

            # If the data object is empty, then the client had stopped the connection and the loop should end.
            if not data:
                break

            # Otherwise print the received data on the server's terminal window.
            print('Received: ', data)
            # This is an optional step - sends a message back to the client.
            # In this case, we know there will only be a single messgae, so the message includes Good-Bye
            conn.sendall(b'You have been sucessfully connected. Good-Bye!')
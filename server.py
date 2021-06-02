import socket                   # Import socket module

port = 51100                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    data = conn.recv(4096)
    
    print('Receiving file')
    open('received_file', 'w').close()
    with open('received_file', 'wb') as f:
        print('file opened')
        while (data):
            print('receiving data...')
            f.write(data)
            f.flush()
            data = conn.recv(4096)
        f.close()
    
    filename = repr(conn.recv(4096))
    print('Filename is: ' + filename)
    
    conn.close()
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
    
    file = 'received_file'
        
    counter = 0
    
    a = 0
    while a != 1:
        print('checking output file existence')
        try:
            with open(file, 'r') as f:
                f.close()
            counter = counter + 1
            file = 'received_file' + str(counter)
            print(file)
            print('file already exists')
            a = 0
        except:
            a = 1
    
    
    print('Receiving file')
    open(file, 'w').close()
    with open(file, 'wb') as f:
        print('file opened')
        while data != b'':
            print('receiving data...')
            f.write(data)
            f.flush()
            data = conn.recv(4096)
        print('Done receiving')
        f.close()
    
    conn.close()

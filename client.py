import socket                   # Import socket module

host = ""
def saveip():
    while True:
        saveyn = input('Do you want to save your ip for next time? yes/no ')
        if saveyn == "yes":
            h = open('ipname', 'w')
            h.write(host)
            h.close()
            break
        elif saveyn == "no":
            break

try:
    with open('ipname', 'r') as f:
        ipfilec = ""
        ipfilec = f.read()
        if ipfilec == "":
            print('ipname file is empty')
            print('Where to connect to (IP can be found through "ip addr" on linux, "ipconfig" on windows): ')
            print('If you do not want to type this on next startup, create a file called "ipname" containing the target IP')
            host = input('IP: ')
            saveip()
        else:
            host = ipfilec
except:
    print('ipname file not found')
    print('Where to connect to (IP can be found through "ip addr" on linux, "ipconfig" on windows): ')
    print('If you do not want to type this on next startup, create a file called "ipname" containing the target IP')
    host = input('IP: ')
    saveip()
port = 51100

print('Connect to: ' + host)

while True:
    filename= input('Input name of file \(has to be in same directory as this script\) you want to send here: ')
    
    s = socket.socket()
    s.connect((host, port))
    f = open(filename,'rb')
    l = f.read(4096)
    while l != b'':
        s.send(l)
        print('Sent '+ repr(l))
        l = f.read(4096)
    f.close()
    
    print('Done sending')
    s.close()

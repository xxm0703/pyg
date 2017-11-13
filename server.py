import socket

s = socket.socket()
s.bind(('192.168.1.102', 50000))
s.listen(2)
while True:
    c1, addr1 = s.accept()
    print("First connect")
    c2, addr2 = s.accept()
    print("Second connect")

    for x in range(9):
        data = ''  # data = '3'
        if x % 2:
            print("c2")
            c2.send("Y")
            c1.send("O")
            while True:
                data = c2.recv(1024)
                if data != '':
                    break
            c2.send(str(data))
            c1.send(str(data))
        else:
            print("c1")
            c1.send("Y")
            c2.send("O")
            while True:
                data = c1.recv(1024)
                if data != '':
                    break
            c1.send(str(data))
            c2.send(str(data))

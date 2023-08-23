import socket
import time


host_name = "localhost"
port = 6666
internet_socket = socket.socket()
internet_socket.bind((host_name,port))

internet_socket.listen(1)

connect, adress = internet_socket.accept()
print(str(adress)+" Connected. ")

while True:
    while True:
        try:
            gelen_veri = str(connect.recv(1024).decode())
            print("Message from the client : "+gelen_veri)
            break
        except ConnectionResetError:
            time.sleep(2)
            print(str(adress)+" Connected")
    if gelen_veri == "Quit":
        break
    else:
        message = input("Message to be send: ")
        print("Waitting client..")
        connect.send(message.encode())
        
connect.close()
internet_socket.close()

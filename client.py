import socket
import time

host_name = "localhost"
port = 6666
internet_socket = socket.socket()
internet_socket.connect((host_name,port))

print("Connected. {}:{}".format(host_name, port))

mesaj = input("Message to be sen: ")
print("Server Waitting")

while mesaj != "Quit":
    internet_socket.send(mesaj.encode())
    gelen_veri = internet_socket.recv(1024).decode()

    print("SERVER: "+gelen_veri)

    mesaj = input("Message to be send: ")
    print("Server Waitting")

internet_socket.close()




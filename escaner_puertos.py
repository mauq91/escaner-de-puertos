#Scanner de puertos

import socket

puertos = [22, 80, 443]
ip = input("Ingrese dirección IP: ")

for puerto in (puertos):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    result = sock.connect_ex((ip, puerto))

    if result == 0:
        print("Puerto Abierto: " + str(puerto))
        sock.close()
    else:
        print("Puerto Cerrado: " + str(puerto))
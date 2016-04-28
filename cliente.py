import socket
import sys
def pro():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10000)
    print("Conectando al puerto", server_address)
    sock.connect(server_address)
    try:
        messagestr = "Este es el mensaje"
        print("Enviando",messagestr)
        message = messagestr.encode(encoding='UTF-8')
        sock.sendall(message)
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(19)
            amount_received += len(data)
            print("Resiviendo",message.decode(encoding='UTF-8'))
    finally:
        print("Cerrando socket")
        sock.close()

import socket
import sys
def pro():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10000)
    print("Iniciando servidor en el puerto",server_address)
    sock.bind(server_address)
    sock.listen(1)
    while True:
        print("Esperando conexión")
        connection, client_address = sock.accept()
        try:
            print("Conexión desde",client_address)
            while True:
                data = connection.recv(19)
                if data:
                    print("Enviando mensaje de vuelta")
                    connection.sendall(data)
                else:
                    print("No hay más datos")
                    break
        finally:
            connection.close()

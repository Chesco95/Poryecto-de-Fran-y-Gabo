import socket
import sys
def pro():
    usuarios="[[1,'Vero'],[2,'Fran'],[13,'Maria']]"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', 10000)
    print("Iniciando servidor en el puerto",server_address)
    sock.bind(server_address)
    sock.listen(1)
    while True:
        print("Esperando conexión")
        connection, client_address = sock.accept()
        try:
            print("Conexión desde",client_address)
            while True:
                data = connection.recv(100)
                print(data.decode(encoding='UTF-8'))
                if data:
                    print("Enviando mensaje de vuelta")
                    usuarios=usuarios.encode(encoding='UTF-8')
                    connection.sendall(usuarios)
                else:
                    print("No hay más datos")
                    break
        finally:
            connection.close()

import socket
import sys
def pro():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    global sock
    server_address = ('172.19.13.78', 10000)
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
            data = sock.recv(100)
            amount_received += len(data)
            print("Resiviendo",data.decode(encoding='UTF-8'))
            usuarios = data.decode(encoding='UTF-8')
            usuarios = eval(usuarios)
            #inventario
            menu()
            
    finally:
        #sal = input("¿Salir? (S/N): ")
        #if sal == "S":
            print("Cerrando socket")
            sock.close()
        #else:
            #menu()

def menu():
    print("1 - Iniciar Seción")
    print("2 - Solicitar Registro")
    print("3 - Realizar Compra")
    print("4 - Solicitar Facturación")
    print("5 - Eliminar Producto")
    print("6 - Salir del sistema")
    op = input("Seleción: ")
    if op == "1":
        menu()
    elif op == "2":
        menu()
    elif op == "3":
        menu()
    elif op == "4":
        menu()
    elif op == "5":
        menu()
    elif op == "6":
        print("Adios")


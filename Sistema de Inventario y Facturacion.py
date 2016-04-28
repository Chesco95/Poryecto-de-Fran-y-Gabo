import time
#Funcion Pricipal.
def sistema():
    archivo1='Ciudades.txt'
    archivo2='Inventario.txt'
    archivo3='Supermercado.txt'
    archivo4='Usuarios.txt'
    global Ciudades
    global Inventario
    global Supermercado
    global Usuarios
    global registrado
    global cliente_venta
    global estaba
    estaba=0
    cliente_venta=''
    registrado='no'
    Ciudades=lectura(archivo1)
    Inventario=lectura(archivo2)
    Supermercado=lectura(archivo3)
    Usuarios=lectura(archivo4)
    Ciudades=vali_ciudades(Ciudades)
    Usuarios=vali_usuario(Usuarios,Ciudades)
    Supermercado=vali_super(Supermercado,Ciudades)
    Inventario=vali_invent(Inventario,Supermercado)
    print("\n")
    print("*******************************************************")
    print("* Bienvenido al sistema de inventario y facturación!! *")
    print("*******************************************************","\n")
    print ("Fecha "  + time.strftime("%x"),"\n")
    verificacion_de_usuario()
    menu_funcionario()
    
    

#Funcion que lee los archivos y los convierte en listas.
def lectura(x):
    archivo=open(x,'r')
    lista=[]
    for i in archivo.readlines():
        palabras=[i[:-1].split(",")]
        for n in palabras:
            lista=lista+[n]
        for i in lista:
            if i==['']:
                lista=lista[:-1]
    return lista
    

#Funcion para validar la lista de ciudades.
def vali_ciudades(x):
    lista=x
    e=x[0]
    nueva=[]
    nueva.append(e)
    for num in lista:
        temp=num
        temp2=temp[0]
        cont=0
        for i in nueva:
            if str(temp2) == str(i[0]):
                cont+=1
        if cont==0:
            nueva.append(num)
    return nueva
            
                
#Funcion para validar la lista de clientes.
def vali_usuario(x,y):
    usuario=vali_ciudad(x,y)
    usuario=vali_cedula_y_permiso(usuario)
    return usuario

def vali_ciudad(x,y):
    nueva=[]
    for i in x:
        temp=i
        temp2=temp[0]
        cont=0
        for e in y:
            if str(temp2) == str(e[0]):
                cont+=1
        if cont==1:
                nueva.append(i)
    return nueva

def vali_cedula_y_permiso(x):
    lista=x
    e=x[0]
    nueva=[]
    nueva.append(e)
    for num in lista:
        temp=num
        temp2=temp[0]
        temp3=temp[1]
        temp4=temp[4]
        cont=0
        posicion=0
        for i in nueva:
            if str(temp2) != str(i[0]) and str(temp3) == str(i[1]):
                cont+=1
            elif str(temp2) == str(i[0]) and str(temp3) == str(i[1]):
                cont+=2
                if str(temp4) != str(i[4]):
                    num[4]=str(2)
                    del nueva[posicion]
                else:
                    cont=cont-1
            posicion+=1
        if cont==0 or cont==2:
            nueva.append(num)
    return nueva


#Funcion para validar la lista de supermercados.
def vali_super(x,y):
    supermercados=vali_ciudad(x,y)
    supermercados=vali_cod_super(supermercados)
    return supermercados

def vali_cod_super(x):
    lista=x
    e=x[0]
    nueva=[]
    nueva.append(e)
    for num in lista:
        temp=num
        temp2=temp[0]
        temp3=temp[1]
        cont=0
        for i in nueva:
            if str(temp2) == str(i[0]) and str(temp3) == str(i[1]):
                cont+=1
        if cont==0:
            nueva.append(num)
    return nueva  


#Funcion para validar la lista de Inventario.
def vali_invent(x,y):
    #Para validar el supermercado.
    inventario=vali_invent_super(x,y)
    #Para validar el cod de producto.
    inventario=vali_cod_super(inventario)
    return inventario
    
def vali_invent_super(x,y):
    nueva=[]
    for i in x:
        temp=i
        temp2=temp[0]
        cont=0
        for e in y:
            if str(temp2) == str(e[1]):
                cont+=1
        if cont==1:
                nueva.append(i)
    return nueva



#Funcion de permiso de usuario para ingresar al sistema.


def verificacion_de_usuario():
    encontrado=0
    print("Ingrese los datos de su usuario por favor.","\n")
    usuario = input("Ingrese su nombre: ")
    cedula = input("Ingrese su cedula: ")
    print("\n")
    for i in Usuarios:
        if usuario in i and cedula in i:
            if str(i[4])==str(2) or str(i[4])==str(1):
                print("Usuario valido!!","\n")
                encontrado+=1
    if encontrado==0:
        print("Usuario no valido, ingrese un usuario válido.","\n")
        verificacion_de_usuario()


#Funcion de MENU principal.
def menu_funcionario():
    global Usuarios
    global registrado
    registrado='no'
    print("\n")
    print('MENÚ PRINCIPAL!!!',"\n")
    print("Elija el numero del trámite a realizar: ","\n")
    print("1. Realizar venta.")
    print("2. Ingresar un nuevo producto al sistema.")
    print("3. Eliminar un producto del sistema.")
    print("4. Registrar a un cliente.")
    print("5. Consultar el precio de un producto.")
    print("6. Consultar productos de un supermercado.")
    print("7. Salir.","\n")
    opcion=input("Ingrese la opción: ")
    if opcion==str(1):
        venta()
    if opcion==str(4):
        respuesta='si'
        while respuesta=='si':
            print("\n")
            print('Registrando nuevo usuario!!!',"\n")
            Usuarios=registrar_cliente()
            print("\n")
            print('Desea agregar otro usuario? (ingrese si o no)',"\n")
            respuesta=input("Ingrese la opcion: ")
            print("\n")
        menu_funcionario()
    if opcion==str(2):
        respuesta='si'
        while respuesta=='si':
            print('Registrando nuevo producto!!!',"\n")
            Inventario=agregar_producto()
            print("\n")
            print('Producto registrado exitosamente!!!',"\n")
            print('Desea registrar otro producto? (Ingrese: si o no)',"\n")
            respuesta=input("Ingrese la opcion: ")
            print("\n")
        menu_funcionario()
    if opcion==str(3):
        eliminar_producto()
        menu_funcionario()
    if opcion==str(5):
        consultar_precio()
    if opcion==str(6):
        consultar_inventario()

#Funcion para venta.
def venta():
    global Usuarios
    global Inventario
    global registrado
    global cliente_venta
    global Supermercado
    if registrado=='si':
        super_registrado=0
        compra=[]
        compra=compra+[cliente_venta]
        articulos=[]
        opcion='no'
        print("\n")
        cod_super=input('Ingrese el código de el supermercado: ')
        for e in Supermercado:
            if cod_super==e[1]:
                compra=compra+[e]
                super_registrado+=1
        if super_registrado==0:
            print("\n")
            print('Código no válido, ingrese el código del supermercado.')
            venta()
        print("\n")
        print("Cliente registrado: ",cliente_venta[0],"\n")
        print("Opciones para ingresear:","\n")
        print("* El código de un producto para añadir a la compra.")
        print("* Ó ingrese ok para para terminar la compra.","\n")
        while opcion!='ok':
            cantidad=0
            opcion=input("Ingrese: ")
            if opcion!='ok':
                no_encontrado=0
                for i in Inventario:
                    if str(opcion)==str(i[1]) and str(cod_super)==str(i[0]):
                        cantidad=input("Cantidad: ")
                        print("\n")
                        temp=[i[1],i[3],cantidad]
                        if cantidad<=i[2]:    
                            if articulos==[]:
                                articulos=articulos+[temp]
                            else:
                                articulos=comparar_prod(temp,articulos)
                            Inventario=reduccion_inventario(i,cantidad)
                            break
                        else:
                            print("\n")
                            print('Lo sentimos, no tenemos esa cantidad disponible. Ingrese una cantidad menor u otro producto.',"\n")
                    elif str(cod_super)!=str(i[0]) and str(opcion)==str(i[1]):
                        print("\n")
                        print('Lo sentimos, este producto solo se encuentra disponible en el supermercado ',i[0],"\n")
                    else:
                        no_encontrado+=1
                if no_encontrado==len(Inventario):
                    print("Código no válido.")
        articulos=sub_total(articulos)
        compra=compra+[articulos]
        compra=total_pagar(compra)
        print("\n")
        print(compra)
        temp=compra[0]
        cedula=str(temp[0])
        factura=open(cedula+".txt","w")
        fecha="Fecha "  + time.strftime("%x")
        factura.writelines(fecha+"\n")
        pos=compra[0]
        Cliente='Cliente: '+pos[0]
        factura.writelines(Cliente+"\n")
        pos=compra[1]
        cod_ciudad='Código de ciudad: '+pos[0]
        factura.writelines(cod_ciudad+"\n")
        pos=compra[1]
        cod_super='Código de supermercado: '+pos[1]
        factura.writelines(cod_super+"\n")
        factura.writelines("\n")
        producto='Producto Precio(c/u) Cantidad Subtotal'
        factura.writelines(producto+"\n")
        pos=compra[2]
        for i in pos:
            producto='  '+i[0]+'       '+i[1]+'         '+i[2]+'      '+i[3]
            factura.writelines(producto+"\n")
        factura.writelines("\n")
        pos=compra[3]
        subtotal='Sub_total: '+pos[0]
        factura.writelines(subtotal+"\n")
        pos=compra[3]
        subtotal='Descuento:  '+pos[1]
        factura.writelines(subtotal+"\n")
        pos=compra[3]
        subtotal='Total:     '+pos[2]
        factura.writelines(subtotal+"\n")
        factura.close()
        registrado='no'
        print()
        ir_a_menu=input('Compra realizada!! Presione enter para ir al menú principal')
        if ir_a_menu=='':
            menu_funcionario()
            
    elif registrado=='no':
        verificar_si_cliente_registrado()

def reduccion_inventario(i,cantidad):
    global Inventario
    posicion=Inventario.index(i)
    cantidad=int(cantidad)
    resta=int(i[2])
    i[2]=str(resta-cantidad)
    Inventario[posicion]=i
    return Inventario

def comparar_prod(prod,articulos):
    cont=0
    for i in articulos:
        if prod[0] == i[0]:
            temp=int(prod[2])+int(i[2])
            i[2]=str(temp)
            cont+=1
    if cont==0:
        temp=prod
        articulos=articulos+[temp]
    return articulos

def total_pagar(compra):
    total=[]
    for i in compra[2]:
        temp=int(i[1])*int(i[2])
        if total==[]:
            total=total+[temp]
        else:
            temp2=total[0]
            total[0]=temp2+temp
    total=descuento(total)
    compra=compra+[total]
    return compra

def sub_total(articulos):
    nueva_lista=[]
    temp2=[]
    for i in articulos:
        temp=int(i[1])*int(i[2])
        temp2=i+[str(temp)]
        nueva_lista=nueva_lista+[temp2]
    return nueva_lista

def descuento(total):
    global estaba
    inicio=total[0]
    nuevo_total=[str(inicio)]
    if estaba==0:
        if inicio>=5000 and inicio<10000:
            desc=(inicio/100)*5
            temp=inicio-desc
        elif inicio>=10000 and inicio<50000:
            desc=(inicio/100)*7
            temp=inicio-desc
        elif inicio>=50000:
            desc=(inicio/10)
            temp=inicio-desc
        else:
            desc=0
            temp=inicio
    elif estaba!=0:
        desc=(inicio/100)*2
        temp=inicio-desc
    nuevo_total=nuevo_total+[str(desc)]
    nuevo_total=nuevo_total+[str(temp)]
    return nuevo_total

#Funcion para verificar si un cliente está registrado.
def verificar_si_cliente_registrado():
    global Usuarios
    global registrado
    global cliente_venta
    global estaba
    print("\n")
    cliente=input("Ingrese la cédula del cliente: ")
    for i in Usuarios:
        if str(cliente) == str(i[1]):
            if str(i[4]) == str(0) or str(i[4]) == str(2):
                registrado='si'
                break
            else:
                registrado='no'
        else:
            registrado='no'
            
    if registrado=='no':
        estaba+=1
        print("\n")
        print("El cliente NO está registrado!!","\n")
        print("¿Registrar un nuevo cliente?","\n")
        print("1. Si")
        print("2. No","\n")
        opcion=input("Ingrese el número de la opción a escoger: ")
        while opcion!='1' and opcion!='2':
            print("\n")
            print("Opción no válida. Por favor ingrese una opción válida!!","\n")
            print("¿Registrar un nuevo cliente?","\n")
            print("1. Si")
            print("2. No","\n")
            opcion=input("Ingrese el número de la opción a escoger: ")
        if opcion=='1':
            Usuarios=registrar_cliente()
            verificar_si_cliente_registrado()
        elif opcion=='2':
            print("\n")
            menu_funcionario()
    if registrado=='si':
        cliente_venta=[cliente]
        venta()

#Funcion para registrar a un cliente.
def registrar_cliente():
    global Usuarios
    nuevo_cliente=[]
    print("\n")
    cod_ciudad=input("Ingrese el cod de ciudad: ")
    nuevo_cliente.append(cod_ciudad)
    cedula=input("Ingrese el numero de cedula: ")
    nuevo_cliente.append(cedula)
    nombre=input("Ingrese el nombre: ")
    nuevo_cliente.append(nombre)
    telefono=input("Ingrese el número de telefono: ")
    nuevo_cliente.append(telefono)
    print("\n")
    print("Ingrese el nivel de permiso.","\n")
    print("0. Cliente.")
    print("1. Funcionario.")
    print("2. Ambos.","\n")
    permiso=input("Ingrese la opcion: ")
    nuevo_cliente.append(permiso)
    Usuarios.append(nuevo_cliente)
    return Usuarios


#Funcion para agregar un nuevo producto al inventario.
def agregar_producto():
    global registrado
    global Inventario
    nuevo_producto=[]
    print("\n")
    cod_super=input("Ingrese el codigo del supermercado: ")
    nuevo_producto.append(cod_super)
    cod_producto=input("Ingrese el código del producto: ")
    nuevo_producto.append(cod_producto)
    cantidad=input("Ingrese la cantidad de unidades: ")
    nuevo_producto.append(cantidad)
    precio=input("Ingrese el precio del producto: ")
    nuevo_producto.append(precio)
    print("\n")
    prod_registrado(cod_super,cod_producto)
    if registrado=='si':
        for i in Inventario:
                if cod_super==i[0] and cod_producto==i[1]:
                    a=int(i[2])
                    b=int(cantidad)
                    c=str(a+b)
                    i[2]=c
        registrado=='no'
    else:
        Inventario.append(nuevo_producto)
    return Inventario


#Funcion para eliminar un producto.
def eliminar_producto():
    global registrado
    global Inventario
    respuesta='si'
    while respuesta=='si':
        print("\n")
        print('Eliminando producto!!',"\n")
        cod_super=input("Ingrese el codigo del supermercado: ")
        cod_producto=input("Ingrese el código del producto: ")
        prod_registrado(cod_super,cod_producto)
        if registrado=='si':
            for i in Inventario:
                if cod_super==i[0] and cod_producto==i[1]:
                    print('Producto eliminado exitosamente!!!',"\n")
                    Inventario.remove(i)
            print("\n")
            print('Desea eliminar otro producto? (Ingrese: si o no)',"\n")
            respuesta=input("Ingrese la opcion: ")
        elif registrado=='no':
            print('El codigo es incorrecto, ingrese el codigo de un producto!!!')
            eliminar_producto()
    menu_funcionario()

def prod_registrado(cod_super,cod_producto):
    global Inventario
    global registrado
    esta=0
    print("\n")
    
    for i in Inventario:
        if cod_super==i[0] and cod_producto==i[1]:
            esta+=1
    if esta!=0:
        registrado='si'
    elif esta==0:
        registrado='no'

#Funcion para consultar el precio de un producto.
def consultar_precio():
    global Inventario
    respuesta='si'
    cont=0
    while respuesta=='si':
        print("\n")
        cod_super=input('Ingrese el código del supermercado: ')
        cod_producto=input('Ingrese el código del producto para desplegar el precio: ')
        print("\n")
        for i in Inventario:
            if cod_super==i[0] and cod_producto==i[1]:
                print('El precio del producto(',cod_producto,') es: ',i[3])
                cont+=1
                print("\n")
                print('Desea consultar el precio de otro producto? (ingrese si o no)',"\n")
                respuesta=input("Ingrese la opcion: ")
        if cont==0:
                print('El código es incorrecto, ingrese el código de un producto!!')
                consultar_precio()
    menu_funcionario()



#Funcion para consultar los productos en el inventario.
def consultar_inventario():
    global Inventario
    respuesta='si'
    cont=0
    producto=[]
    while respuesta=='si':
        print("\n")
        cod_super=input('Ingrese el código del supermercado: ')
        print("\n")
        for i in Inventario:
            if cod_super==i[0]:
                cont+=1
                producto=producto+[i]
        if cont!=0:
            print('El producto disponible en inventario es: ',producto,"\n")
            respuesta=input('Presione enter para salir!!')
        elif cont==0:
            print('El código es incorrecto, ingrese el código solicitado!!!')
            consultar_inventario
    menu_funcionario()


    
#######################################################################

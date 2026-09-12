productos_supermercado=[]

def mostrar_menu():
    # Indentar = 4 espacios al inicio de cada línea que pertenece a una función, if, while,
    print("Elija una opcion:")
    print("1 Agregar producto")
    print("2 Eliminar producto")
    print("3 Buscar producto")
    print("4 Ordenar productos")
    print("5 Ver todos lo productos")
    print("6 Ver cantidad de productos")
    print("7 Salir")

def agregar_producto():
    producto= input("Ingrese el nombre del producto que desea agregar:").lower()
    if producto == "":
        print("No se puede agregar un producto vacio")
    elif not producto.replace(" ", "").isalpha():
        print("El dato que ingreso no es valido, solo se aceptan letras")
    elif producto in productos_supermercado:
        print("El producto ya existe en la lista")
    else:
        productos_supermercado.append(producto)
        print(f"Se ha agregado {producto} a la lista de productos")

def eliminar_producto():
    if len(productos_supermercado)==0:
        print("La lista esta vacia no se puede eliminar")
    else:
        print("Productos disponibles:")
        for lista in productos_supermercado:
            print(f"-{lista}")
        eliminado= input("Ingrese el producto que quisiera eliminar:").lower()
        if eliminado == "":
            print("No puede ingresar un producto vacio")
        elif not eliminado.replace(" ", "").isalpha():
            print("El dato que ingreso no es valido, solo se aceptan letras")
        elif eliminado not in productos_supermercado:
            print("El producto no existe en la lista")
        else:
            productos_supermercado.remove(eliminado)
            print(f"Se ha eliminado {eliminado} de la lista")

def buscar_producto():
    encontrado = input("Ingrese el nombre del producto a buscar:").lower()
    if encontrado == "":
        print("No puede ingresar un producto vacio")
    elif not encontrado.replace(" ","").isalpha():
        print("El dato que ingreso no es valido, solo se aceptan letras")
    elif encontrado in productos_supermercado:
        print(f"El producto {encontrado} se encuentra en la lista")
    else:
        print(f"El producto {encontrado} no se encuentra en la lista")

def ordenar_productos():
    if len(productos_supermercado)==0:
        print("La lista esta vacia no se puede ordenar")
    else:
        print("Productos ordenados:")
        productos_supermercado.sort()
        for ordenado in productos_supermercado:
            print(f"-{ordenado}")

def ver_todos():
    if len(productos_supermercado)==0:
        print("La lista esta vacia no se puede mostrar")
    else:
        for lista_completa in productos_supermercado:
            print(f"-{lista_completa}")

def ver_cantidad():
    if len(productos_supermercado)==0:
        print("La lista esta vacia,no se puede ver la cantidad")
    elif len(productos_supermercado) == 1:
        print(f"Hay 1 producto en la lista")
        for productos in productos_supermercado:
            print(productos)
    else:
        print(f"Hay {len(productos_supermercado)} productos en la lista:")
        for productos in productos_supermercado:
            print(productos)

while True:
    nombre_usuario = input("Ingrese su nombre de usuario:")
    if nombre_usuario == "":
        print("No puede ingresar un nombre de usuario vacio")
    elif not nombre_usuario.replace(" ", "").isalpha():
        print("El nombre de usuario solo acepta letras")
    else:
        print(f"Listo {nombre_usuario}, empieza a usar el menu de nuestro supermercado:")
        break



while True:
    mostrar_menu()
    opcion= input("Elija una de las 7 opciones:").strip()
    if opcion== "1":
        agregar_producto()
    elif opcion== "2":
        eliminar_producto()
    elif opcion== "3":
        buscar_producto()
    elif opcion== "4":
        ordenar_productos()
    elif opcion== "5":
        ver_todos()
    elif opcion == "6":
        ver_cantidad()
    elif opcion== "7":
        print(f"Hasta luego {nombre_usuario}, que tenga un buen dia!")
        break
    else:
        print("Ingrese una opcion valida")
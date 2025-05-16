from datetime import datetime

print("********************************")
print("********Tulipanes Store*********")
print("**Arreglos florales exclusivos**")
print("********************************")

print("introduzca su nombre por favor:")
nombre = input().capitalize()

print("introduzca su apellido por favor:")
apellido = input().capitalize()

nombre_completo = nombre + " " + apellido
print("Hola", nombre_completo, "!Gracias por visitar Tulipanes Store!")

compras = []

inventario = {
    "Rosas": 12,
    "Tulipanes": 42,
    "Lirios": 54,
    "Margaritas": 32,
    "Peonias": 37,
    "Orquideas": 12,
    "Girasoles": 58,
    "Astromelias": 5,
    "Hortensias": 23,
    "Freesias": 18,
}

precio = 23

flores_totales = 0
for val in inventario.values():
    flores_totales += val

def mostrar_inventario():
    print("Tenemos arreglos monoflorales de: ")
    for llave, valor in inventario.items():
        print(f"   {llave}: {valor}")
    print(f" En total tenemos: {flores_totales} arreglos monoflorales. Cada uno tiene un valor de {precio}€" )

def comprar_arreglo():
    carrito = []

    while True:
        print("¿Que arreglo floral deseas comprar? Sólo puedes elegir uno de cada tipo")
        print("Escribe F para terminar la lista o V para ver tu carrito")
        arreglo = input().capitalize()

        if arreglo == "F":
            break

        if arreglo == "V":
            print("Tu carrito de compras contiene los siguientes arreglos:")
            for item in carrito:
                print(item)
            continue

        if arreglo not in inventario:
            print(f" Lo sentimos, no contamos con el arreglo de {arreglo}")
        elif inventario[arreglo] == 0:
            print(f"Lo sentimos, no tenemos en existencia el arreglo con {arreglo}")
        elif arreglo not in carrito:
            carrito.append(arreglo)
        else:
            print("Ese arreglo ya esta en tu carrito")

    print("Tu carrito de compra tiene los siguientes arreglos florales:")
    for arreglo in carrito:
        print("  ", arreglo)
        inventario[arreglo] -= 1
        # AGREGAR COMPRA AL CARRITO DE COMPRAS

    fecha = datetime.now()
    fecha_formateada = fecha.strftime("%d-%m-%Y a las %H:%M")
    compras.append((nombre, fecha_formateada, carrito))  # esto es una tupla!!!


def mostrar_compras():
    print("")
    print("**** COMPRAS REALIZADAS ****")
    for compra in compras:
        nombre_cliente = compra[0]
        fecha = compra[1]
        carrito = compra[2]
        total = len(carrito) * precio

        print(
            f"{nombre_cliente} el {fecha} compraste los siguientes arreglos monoflorales:"
        )
        for arreglo in carrito:
            print(f"   - {arreglo}")
        print(f"Total a pagar: {total}€")
        print("-" * precio)
        
        
def mostrar_menu():
    print("")
    print("===================================")
    print("")
    print("Selecciona la opcion que deseas: ")
    print("1: Conocer que tipo de flores tenemos en stock")
    print("2: Comprar un arreglo de flores")
    print("3: mostrar compras")
    print("4: Salir")

while True:
    mostrar_menu()
    respuesta = int(input())

    if respuesta == 1:
        mostrar_inventario()
    elif respuesta == 2:
        comprar_arreglo()
    elif respuesta == 3:
        mostrar_compras()
    elif respuesta == 4:
        print("Adios", nombre_completo, "Esperamos vuelva a nuestra tienda!")
        break  # sentencia para dar salida a un ciclo infinito

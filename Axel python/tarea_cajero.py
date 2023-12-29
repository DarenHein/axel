


#cajero 


def ciclo(): 
    while True : 
        menu()



def menu(): 
    saldo = 1000 # entero 
    nombre = "Luis"
    print("""
hola mi cajero pedoro 
      1 ver saldo 
      2 retirar 
      3 ingresar 
    """)
    opcion = input("->")
    opcion = int(opcion)

    if opcion == 1 : 
        print("ver saldo")
        print("su saldo actual es de -> ",saldo)
    elif opcion == 2 : 
        print("retiro")
        print("Su saldo actual es de -> " , saldo)
        resto = input("ingresa la cantidada a sacar -> ")
        resto = int(resto)
        saldo =saldo -  resto 
        print("Su saldo es -> " , saldo)
    elif opcion == 3 : 
        print("ingresar ")
    else : 
        print("opcion invalida")

ciclo()
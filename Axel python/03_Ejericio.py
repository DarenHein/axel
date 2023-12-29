# dada una lusta de numeros saber cual es par y cual no 

#quiero hacer un programa que me diga si el numero es par o inpar 
numero = int (input("Ibgresar  un numero -> ")) # es pedirle aal usuario un numero 
operacion = numero % 2 # hacer la operacion 0
# verificar si el numerp lo es 
if operacion == 0 : # es par 
    print("el numero es par -> " , operacion)
else : # es inpar 
    print("el nuermo es inpar " , operacion)
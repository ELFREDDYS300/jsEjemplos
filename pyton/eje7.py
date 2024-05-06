#Dados 6 números reales, informar el promedio de los mismos.
def Suma(): 
    n1 = int(input("Ingrese un numero entero"))
    n2 = int(input("Ingrese el segundo numero entero"))
    n3 = int(input("Ingrese el tercer numero entero"))
    n4 = int(input("Ingrese otro numero"))
    n5 = int(input("Ingrese otro numero"))
    n6 = int(input("Ingrese el ultimo numero"))
    
    resultado = n1 + n2 + n3 + n4 + n5 + n6
    resultadofinal = resultado / 6

    print("El resultado es", resultadofinal)

Suma()
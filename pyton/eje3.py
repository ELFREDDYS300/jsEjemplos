#Dados 2 números enteros, que representan los lados de un rectángulo se pide informar la superficie del mismo.
def Suma(): 
    n1 = int(input("Ingrese la altura del rectangulo en cm"))
    n2 = int(input("Ingrese el ancho del rectangulo en cm"))

    resultado = n1 * n2
    print("El resultado es", resultado, "cm")

Suma()
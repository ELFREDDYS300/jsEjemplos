#Dados 2 números enteros, que representan una cantidad parcial y total se pide: Calcular e informar el
#porcentaje que representa la primera de la segunda. ¿Qué tipo de datos son los recomendados para este
#algoritmo?
def Suma(): 
    n1 = int(input("Ingrese la cantidad parcial: "))
    n2 = int(input("Ingrese la cantidad total: "))

    porcentaje = (n1 / n2) * 100

    print("El resultado es de", porcentaje, "% ")

Suma()
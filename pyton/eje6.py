#Se necesita calcular la superficie de un triángulo, y se dispone solamente de los valores de su base y altura.
#Definir también que tipo de valor es aconsejable para las variables con la información que se tiene.
#**No se podrá usar valores fijos en las fórmulas del algoritmo. Solo variables y/o constantes.**
def Suma(): 
    altura = float(input("Ingrese la altura del triangulo en cm"))
    base = float(input("Ingrese la base en cm"))

    superficie = 0.5 * altura * base
    print("El resultado es", superficie, "cm")

Suma()
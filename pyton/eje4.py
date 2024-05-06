#Dado 1 número con decimales, que representa el lado de un cuadrado se pide informar la superficie del mismo.
def Suma(): 
    lado = float(input("Ingrese la longitud del lado del cuadrado: ")) 

    superficie = lado ** 2
    print("La superficie del cuadrado es:", superficie)
Suma()
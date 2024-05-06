#Se ingresa 3 números que representan horas, minutos y segundos. Se pide informar el resultado expresado en
#segundos. Determinar qué tipo de valor es el aconsejable para los datos solicitados
def Suma(): 
    horas = float(input("Ingrese horas ")) 
    minutos = float(input("Ingrese minutos ")) 
    segundos = float(input("Ingrese segundos ")) 

    horas = horas * 3600
    minutos = minutos * 60

    resultado = horas + minutos + segundos 
    print("El resultado es", resultado, "segundos")
Suma()
#Dada una fecha que se lee en formato numérico DDMMAAAA (dos números para el día, dos para el mes, cuatro
#para el año), se solicita obtener el día el mes y año por separado en tres variables. (usar descomposición
#matemática)
def Suma(): 
    fecha = int(input("Ingrese la fecha en formato DDMMAAAA: "))

    año = fecha % 10000
    mes_dia = fecha // 10000 # Doble // para solo obtener la parte entera
    mes = mes_dia % 100
    dia = mes_dia // 100

    print("Dia:", dia)
    print("Mes:", mes)
    print("Año:", año)

Suma()
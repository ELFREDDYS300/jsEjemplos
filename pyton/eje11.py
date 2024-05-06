#Una concesionaria de autos paga a su personal, un salario de 5500 pesos por mes, mas una comisión del 200
#pesos por cada auto vendido y un adicional del 5% del valor del auto vendido. Diseñar un algoritmo para calcular
#el salario total del vendedor. Conociendo solamente el número de autos vendidos y el valor de venta de la
#unidad.
def Suma(): 
    salario = 5500
    comision = 200

    autosVendidos = int(input("Ingrese el número de autos vendidos: "))
    valorPorAuto = float(input("Ingrese el precio de venta de cada auto: "))

    comisionTotal = autosVendidos * comision

    adicional = autosVendidos * (valorPorAuto * 0.05)

    salarioTotal = salario + comisionTotal + adicional

    print("El salario total del vendedor es:", salarioTotal, "pesos")
Suma()
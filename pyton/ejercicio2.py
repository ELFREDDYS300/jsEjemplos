#
# A partir del siguiente array que se proporciona: var valores = [true, 5, false, "hola", "adios",
#2];
#Determinar cual de los dos elementos de texto es mayor
#Utilizando exclusivamente los dos valores booleanos del array, determinar los operadores
#necesarios para obtener un resultado true y otro resultado false
#Determinar el resultado de las cinco operaciones matemáticas realizadas con los dos
#elementos numéricos

valores = [True, 5, False, "hola", "adios", 2] 
if len(valores[3]) < len(valores[4]):
    print("adios es mas grande que hola")
    print(valores[0])
else:
    print("hola es mas chico que adios")
    print(valores[2])
    print(valores[1]+valores[5])
    print(valores[1]- valores[5])
    print(valores[1]*valores[5])
    print(valores[1]/valores[5])

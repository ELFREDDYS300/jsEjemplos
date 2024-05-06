#En un curso de ciencias de la computación la calificación final del estudiante se determina a partir del
#rendimiento en tres aspectos del trabajo. A) Existe una calificación por los exámenes parciales que representa el
#30% del valor total de la nota final. B) la calificación por los trabajos prácticos corresponde al 20% del valor de la
#nota final. C) el examen integrador que corresponde al 50% restante. (los valores de las notas pueden ir de 0 a
#10)
def Suma(): 
    parciales = float(input("Ingrese la calificacion de los examenes parciales (0-10): "))
    practicos = float(input("Ingrese la calificacion de los trabajos practicos (0-10): "))
    integrador = float(input("Ingrese la calificacion del examen integrador (0-10): "))

    Porcentajeparciales = parciales * 0.3
    Porcentajepracticos = practicos * 0.2
    Porcentajeintegrador = integrador * 0.5

    Notafinal = Porcentajeparciales + Porcentajepracticos + Porcentajeintegrador

    print("La calificación final es de", Notafinal)

Suma()
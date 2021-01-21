"""Departamento de ac - 1
    1 año - 6 dias
    2 a 6 - 14 dias
    7 a mas - 20
Departamento de log - 2
    1 año - 7 dias
    2 a 6 - 15 dias
    7 a mas - 22 dias 
Gerencia - 3
    1 - 10
    2 a 6 - 20
    7 a mas - 30

Sistemas debe solicitar nombre deel trabajador y clave de departamento
Sitema debe mostrar mensahe con el nombre y dias de vacaciones

"""

print(":::::::::::::::::::::::::::::::")
print("Cuenta de dias de vacaciones.")
print(":::::::::::::::::::::::::::::::\n")

nombre = input("Nombre del trabajador. ")
clave = int(input("Introduce la clave deel departamento al que perteneces. "))
años = float(input("introdusca la cantidad de años que tiene trabajando en la empresa: "))

if clave == 1:
    if años == 1:
        print("Señor ",nombre, " Le corresponde 6 dias de vacaciones. ")
    elif años >= 2 and años <= 6:
        print("Señor ",nombre, " Le corresponde 14 dias de vacaciones. ")
    elif años >= 7:
        print("Señor ",nombre, " Le corresponde 20 dias de vacaciones. ")
    else:
        print("El empleado aun no tiene derecho a vacaciones. ")


elif clave == 2:
    if años == 1:
        print("Señor ",nombre, " Le corresponde 7 dias de vacaciones. ")
    elif años >= 2 and años <= 6:
        print("Señor ",nombre, " Le corresponde 15 dias de vacaciones. ")
    elif años >= 7:
        print("Señor ",nombre, " Le corresponde 22 dias de vacaciones. ")
    else:
        print("El empleado aun no tiene derecho a vacaciones. ")


elif clave == 3:
    if años == 1:
        print("Señor ",nombre, " Le corresponde 10 dias de vacaciones. ")
    elif años >= 2 and años <= 6:
        print("Señor ",nombre, " Le corresponde 20 dias de vacaciones. ")
    elif años >= 7:
        print("Señor ",nombre, " Le corresponde 30 dias de vacaciones. ")
    else:
        print("El empleado aun no tiene derecho a vacaciones. ")

else:
    print("Señor ", nombre, " la clave de departamento no existe. ")





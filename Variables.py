#-------------------------------------------------------------------------------
# Created:     11-05-2020
# Copyright:   (c) Carlos Luco Montofré 2020
#
#-------------------------------------------------------------------------------

def inputFloat(mensaje):
    noValido = True
    while noValido:
        try:
            numero = float(input(mensaje))
            noValido = False
        except ValueError:
            print("Error, digite de nuevo")
    return numero
#--------------------------------------------

for k in range (2):
    nombre = input("Ingrese nombre")
    cantidadNotas = int(input("Ingrese cantidad de notas"))

    sumaNotas = 0

    for i in range (cantidadNotas):
        nota = inputFloat("Ingrese nota")

        sumaNotas = sumaNotas + nota

    promedio = sumaNotas / cantidadNotas
    print("El promedio de",nombre," es",promedio)







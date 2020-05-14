#-------------------------------------------------------------------------------
# Copyright:   (c) Carlos Luco Montofré 2020
#
#-------------------------------------------------------------------------------

largo = int(input("Ingrese el largo"))
ancho = int(input("Ingrese el ancho"))

if largo == ancho:
    print("Los datos corresponden a un cuadrado")
else:
    print("Los datos corresponden a un rectángulo")
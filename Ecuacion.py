#-------------------------------------------------------------------------------
# Copyright:   (c) Carlos Luco Montofré 2020
#
#-------------------------------------------------------------------------------
def inputInt(mensaje):
    noValido = True
    while noValido:
        try:
            numero = int(input(mensaje))
            noValido = False
        except ValueError:
            print("Error, digite de nuevo")
    return numero
#--------------------------------------------

A = inputInt("Ingrese Coeficiente  A")
B = inputInt("Ingrese Coeficiente  B")
C = inputInt("Ingrese Coeficiente  C")

factor = (B ** 2) - (4 * A * C)

if factor > 0:
    resultado1 = ((B * -1) + factor ** 0.5 ) / 2 * A
    resultado2 = ((B * -1) - factor ** 0.5 ) / 2 * A
    print("Solución 1 es ", resultado1)
    print("Solución 2 es ", resultado2)
elif factor == 0:
    resultado1 = (B * -1) / 2 * A
    print("Solución 1 es ", resultado1)
else:
    real = (B * -1) / 2 * A
    imaginaria = ((factor * -1) ** 0.5 ) / 2 * A
    print("Solución 1 es ", real, " + ",imaginaria, "i")
    print("Solución 2 es ", real, " - ",imaginaria, "i")








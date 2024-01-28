"""
Crear 3 variables: nombre, edad y distrito

Requisitos:
- Nombre: string, edad: int, distrito: string
- Concatenar ests 2 datos e indicar una oración como la siguiente:
José tiene X años y es de "Distrito"
-Obtener el módulo de su edad al usarlo con el número 5
"""

var_1 = "Gerardo"
var_2 = 22
var_3 = "San Isidro"

mod = var_2 % 5
print("{} tiene {} años y es de {}".format(var_1,var_2,var_3))
print("el modulo de su edad es: {}".format(mod))
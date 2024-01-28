

list1 = []
list2 = []

list1.append("Nicole")
list1.append( 18)
list1.append("Ingenieria")

list2.append("Alexandra")
list2.append( 19)
list2.append("Derecho")

suma_lista = list1 + list2
print("La suma es: ".format(suma_lista))

suma_lista.reverse()

print("Suma de las edades en orden inverso:{}".format(suma_lista))

del suma_lista[1]
del suma_lista[3]


print("Lista  después de eliminar las edades:", suma_lista)


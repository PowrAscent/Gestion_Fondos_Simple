entrada = input("Introduzca Sus Gastos Separados Por Coma: ")

partes = entrada.split(",")
gastos = []

for p in partes:
    p = int(p)
    gastos.append(p)

total = 0
cantidad = 0

for g in gastos:
    total += g
    cantidad += 1
        
promedio = total / cantidad


def gastos_personales():
    for r in range(len(gastos)):
        if r != len(gastos) - 1:
            print(gastos[r], end=", ")
        elif r == len(gastos) - 1:
            print(gastos[r])


print("---------- RESULTADOS ----------")
print("Gastos Personales: ", end="")
gastos_personales()
print("Total             : ", total)
print("Cantidad de Montos: ", cantidad)
print("Promedio          : ", promedio)
# B2_cantidades.py

from B1_customProcesorRemisiones import list_cantidad
from A1_getPaths import listPiezas

# Convierte las cantidades a enteros si son cadenas
list_cantidad = [int(cantidad) for cantidad in list_cantidad]
listPiezas = [int(piezas) for piezas in listPiezas]

# Lista de salida
resultadosCant = []

# Iteramos sobre los elementos de ambas listas
for piezas, cantidad in zip(listPiezas, list_cantidad):
    resultado_parcial = []
    while cantidad > 0:
        if cantidad >= piezas:
            resultado_parcial.append(piezas)
            cantidad -= piezas
        else:
            resultado_parcial.append(cantidad)
            cantidad = 0
    resultadosCant.append(resultado_parcial)

# Imprimimos la lista de listas resultante
print(resultadosCant)

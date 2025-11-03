"""
1) Crear una lista con las notas de 10 estudiantes.
• Mostrar la lista completa.
• Calcular y mostrar el promedio.
• Indicar la nota más alta y la más baja.
"""
nota_estudiantes = [1,2,3,4,5,6,7,8,9,10]
suma_notas = 0
contador = 0
for i in nota_estudiantes:
    suma_notas = suma_notas + i
    contador = contador + 1
media = suma_notas / contador
nota_vaja = min(nota_estudiantes)
nota_alta = max(nota_estudiantes)
print("el promedio de las notas es de: ", media)
print("la nota mas vaja es: ", nota_vaja)
print("la nota mas alta es: ", nota_alta)
"""
2) Pedir al usuario que cargue 5 productos en una lista.
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
• Preguntar al usuario qué producto desea eliminar y actualizar la lista.
"""
productos = []
for i in range(5):
    pro = input("ingrese un producto: ")
    productos.append(pro)

print("la lista ordenada es: ", sorted(productos))
print("que producto desea iliminar?")
print(sorted(productos))
eliminar = input("eliga una opcion: ")
if eliminar in productos:
    productos.remove(eliminar)
else:
    print("el producto no se encuentra en la lista")
print("la lista actualizada es: ", sorted(productos))
"""
3) Generar una lista con 15 números enteros al azar entre 1 y 100.
• Crear una lista con los pares y otra con los impares.
• Mostrar cuántos números tiene cada lista.
"""
import random
num_alazar = [random.randint(1,100) for i in range(15)]
lista_pares = []
lista_impares = []
for num in num_alazar:
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
print("la primera lista de numeros: ", num_alazar)
print("la lista de numeros pares es de: ", lista_pares)
print("la lista de numeros impares es de: ", lista_impares)
"""
4) Dada una lista con valores repetidos:
• Crear una nueva lista sin elementos repetidos.
• Mostrar el resultado.
"""
lista_valores = [2,4,3,5,6,8,5,7,3,9]
lista_valores_2 = list(set(lista_valores))
print("mi primera lista: ", lista_valores)
print("mi segunda lista sin repitir: ", lista_valores_2)
"""
5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
• Mostrar la lista final actualizada.
"""
lista_estudiantes = ["leo","sabrina","gustavo","alejandro","carla","juan","tatiana","marcos"] 
acciones = int(input("seleccione que opcion quiere hacer(1-agregar estudiante o 2-eliminar estudiante): "))
if acciones == 1:
    seleccion = int(input("ingrese el nombre del estudiante que desea agregar: "))
    lista_estudiantes.append(seleccion)
    print("la nueva lista es de: ", lista_estudiantes)
elif acciones == 2:
    print(lista_estudiantes)
    seleccion = input("seleccione al estudiante que desa eliminar: ")
    lista_estudiantes.remove(seleccion)
    print("la nueva lista es de: ", lista_estudiantes)
else:
    print("opcion invalida, y su lista queda igual: ", lista_estudiantes)
"""
6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
último pasa a ser el primero).
"""
lista_numeros = [1,2,3,4,5,6,7]
print("mi primera lista es: ", lista_numeros)
ultimo = lista_numeros[-1]
resto_numeros = lista_numeros[:-1]
lista_rotada = [ultimo] + resto_numeros
print("la nueva lista es: ", lista_rotada)
"""
7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
semana.
• Calcular el promedio de las mínimas y el de las máximas.
• Mostrar en qué día se registró la mayor amplitud térmica.
"""
dias = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
temperaturas = [
    [5, 23],
    [8, 20],
    [9, 18],
    [7, 22],
    [10, 25],
    [12, 28],
    [8, 19],
]
s_minimas = 0
s_maximas = 0
for fila in temperaturas:
    s_minimas += fila[0]
    s_maximas += fila[1]

promedio_min = s_minimas / 7.0
promedio_max = s_maximas / 7.0
mayor_amplitud = -1
indice_amplitud = -1
for i in range(7):
    min_dia = temperaturas [i][0]
    max_dia = temperaturas [i][1]

    amplitud = max_dia - min_dia
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        indice_amplitud = i
print("el promedio de la minimas es de: ", promedio_min)
print("el promedio de las maximas es de: ", promedio_max)
print("la mayor amplitud termica en el dia: ", dias[indice_amplitud], "es de: ", mayor_amplitud)

"""
8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
• Mostrar el promedio de cada estudiante.
• Mostrar el promedio de cada materia.
"""
estudiantes = ["miguel", "carlos", "maria", "juan", "sabri"]
materias = ["matematica", "lengua", "historia"]

notas = [
    [4, 3, 6],
    [3, 3, 4],
    [5, 2, 6],
    [9, 8, 4],
    [6, 8, 6]
]
for i in range(len(estudiantes)):
    print(estudiantes[i]+ ":", notas[i])
"""
9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
• Inicializarlo con guiones "-" representando casillas vacías.
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
• Mostrar el tablero después de cada jugada.
"""
"""
10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
• Mostrar el total vendido por cada producto.
• Mostrar el día con mayores ventas totales.
• Indicar cuál fue el producto más vendido en la semana.
"""
"""
1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
"""
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

"""
2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
"""
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

"""
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.
"""
solo_frutas = list(precios_frutas.keys())
print(solo_frutas)

"""
4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
"""
agenda = {}

for _ in range(5):
    nombre = input("Nombre del contacto: ").strip()
    numero = input("Número telefónico: ").strip()
    agenda[nombre] = numero

buscar = input("¿A quién querés buscar?: ").strip()

if buscar in agenda:
    print("Número:", agenda[buscar])
else:
    print("Ese contacto no existe.")
"""
5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
"""
frase = input("Ingrese una frase: ").lower()

palabras = frase.split()

# palabras únicas
unicas = set(palabras)
print("Palabras únicas:", unicas)

# contar cada palabra
contador = {}
for p in palabras:
    if p in contador:
        contador[p] += 1
    else:
        contador[p] = 1

print("Frecuencia de palabras:", contador)

"""
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
"""
alumnos = {}

for _ in range(3):
    nombre = input("Nombre del alumno: ")
    print("Ingrese las 3 notas:")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    alumnos[nombre] = (n1, n2, n3)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"{nombre}: promedio = {promedio:.2f}")

"""
7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
"""
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

print("Aprobaron ambos:", parcial1 & parcial2)
print("Aprobaron solo uno:", parcial1 ^ parcial2)
print("Aprobaron al menos uno:", parcial1 | parcial2)

"""
8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
"""
"""
9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permití consultar qué actividad hay en cierto día y hora.
"""
"""
10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.
"""
paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Perú": "Lima"
}

invertido = {}

for pais, capital in paises.items():
    invertido[capital] = pais

print(invertido)

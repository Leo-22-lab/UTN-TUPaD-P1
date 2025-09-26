"""
1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
"""
print("actividad 1")
edad = int(input("ingrese su edad: "))
if edad >= 18:
    print("es mayor de edad")
else:
    print("no es mayor de edad")
print("________________________________________________________________________________________")
"""
2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”.
"""
print("actividad 2")
nota = int(input("ingrese su nota: "))
if nota >= 6:
    print("“Aprobado”")
else:
    print("“Desaprobado”")
print("________________________________________________________________________________________")
"""
3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar.
"""
print("actividad 3")
numero = int(input("ingrese un numero(par si es posible): "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
print("________________________________________________________________________________________")
"""
4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.
"""
print("actividad 4")
edad_u = int(input("ingrese su edad: "))
if edad_u < 12:
    print("es Niño/a")
elif edad_u >= 12 and edad_u < 18:
    print("es Adolescente")
elif edad_u >= 18 and edad_u < 30:
    print("es Adulto/a joven")
elif edad_u >= 30:
    print("es Adulto/a")
else:
    print("edad incorrecta")
print("________________________________________________________________________________________")
"""
5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string.
"""
print("actividad 5")
contraceña = input("ingrese una contraceña: ")
if len(contraceña) >= 8 and len(contraceña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
print("________________________________________________________________________________________")
"""
6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
siguiente:
from statistics import mode, median, mean
mi_lista = [1,2,5,5,3]
mean(mi_lista)
En la documentación oficial se puede encontrar más información sobre este paquete:
https://docs.python.org/es/3.8/library/statistics.html.
La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
mediana es mayor que la moda.
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
la mediana es menor que la moda.
● Sin sesgo: cuando la media, la mediana y la moda son iguales.
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
Definir la lista numeros_aleatorios de la siguiente forma:
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
forma aleatoria.
"""
print("actividad 6")
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
from statistics import mode, median, mean
print("lista de numeros: ")
print (numeros_aleatorios)
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if  media > mediana > moda:
    print("exixte un sesgo positivo")
elif media < mediana < moda:
    print("existe un sesgo negativo")
elif media == mediana == moda:
    print("no existe sesgo")
else:
    print("ubo un error")

print("________________________________________________________________________________________")
"""
7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla.
"""
print("actividad 7")
frase_usuario = input("ingrese una frace: ")
vocales = "aeiouAEIOU"
if frase_usuario[-1] in vocales:
    resultado = frase_usuario + "!"
else:
    resultado = frase_usuario
print(resultado)
print("________________________________________________________________________________________")
"""
8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas.
"""
print("actividad 8")
nom = input("ingrese su nombre: ")
opcion = int(input("seleccione una opcion(1, 2 o 3): "))
if opcion == 1:
    mayusculas = nom.upper()
    print("su nombre en mayusculas: ", mayusculas)
elif opcion == 2:
    minusculas = nom.lower()
    print("su nombre en minusculas: ", minusculas)
elif opcion == 3:
    primera_mayuscula = nom.title()
    print("su nombre con la primera letra en mayuscula: ", primera_mayuscula)
else:
    print("opcion no valida")
print("________________________________________________________________________________________")
"""
9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
"""
print("actividad 9")
magnitud_terremoto = int(input("ingrese la magnitud: "))
if magnitud_terremoto < 3:
    print("Muy leve")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print("Leve")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    print("Moderado")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print("Fuerte")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
    print("Muy Fuerte")
elif magnitud_terremoto >= 7:
    print("Extremo")
print("________________________________________________________________________________________")
"""
10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
____________________________________________________________________________________________
|Periodo del año          |Estación en el hemisferio norte  |  Estación en el hemisferio sur|
|_________________________|_________________________________|_______________________________|
|Desde el 21 de diciembre |                                 |                               |
|hasta el 20 de           |              Invierno           |            Verano             |
|marzo (incluidos)        |                                 |                               |
|_________________________|_________________________________|_______________________________|
|Desde el 21 de marzo     |                                 |                               |
|hasta el 20 de junio     |              Primavera          |             Otoño             |
|(incluidos)              |                                 |                               |
|_________________________|_________________________________|_______________________________|
|Desde el 21 de junio     |                                 |                               |
|hasta el 20 de           |              Verano             |             Invierno          |
|septiembre (incluidos)   |                                 |                               |
|_________________________|_________________________________|_______________________________|
|Desde el 21 de           |              Otoño              |                               |
|septiembre hasta el 20   |                                 |             Primavera         |
|de diciembre (incluidos) |                                 |                               |
|_________________________|_________________________________|_______________________________|
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano.
"""
print("actividad 10")
emisferio = input("ingrese el emisferio en donde se encuentra(N/S): ")
mes = input("ingrese el mes del año(1-12): ")
dia = int(input("ingrese el dia: "))
if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
    if emisferio == "N":
        print("esta en invierno")
    else:
        print("esta en verano")
elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
    if emisferio ==  "N":
        print("estas en primavera")
    else:
        print("estas en otoño")
elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
    if emisferio ==  "N":
        print("estas en verano")
    else:
        print("estas en Invierno")
elif (mes == 69 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
    if emisferio ==  "N":
        print("estas en Otoño")
    else:
        print("estas en Primavera")
else:
    print("hubo un error en las fechas")

print("________________________________________________________________________________________")
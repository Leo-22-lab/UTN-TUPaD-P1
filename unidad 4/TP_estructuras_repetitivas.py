"""
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
"""
print("actividad 1")
for i in range(0,101):
    print(i)
print("__________________________________________________________________________________")
"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
"""
print("actividad 2")
numero_entero = int(input("ingrese un numero entero: "))
contador = 0
while numero_entero > 0:
    numero_entero = numero_entero // 10
    contador += 1
print("el numero tiene: ", contador, "digitos")
print("__________________________________________________________________________________")
"""
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
"""
print("actividad 3")
val1 = int(input("ingrese el primer valor: "))
val2 = int(input("ingrese el segundo valor: "))
suma = 0
for i in range(val1, val2+1):
    suma = suma + i
print("la suma es: ", suma)
print("__________________________________________________________________________________")
"""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""
print("actividad 4")
num_u = int(input("ingrese un numero: "))
sumar = 0
while num_u != 0:
    num_u = int(input("ingrese otro numero: "))
    sumar = sumar + num_u
print("el total de la suma es de: ", sumar)
print("__________________________________________________________________________________")
"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""
print("actividad 5")
import random
adi = int(input("adivine el numero del 1 al 9: "))
intentos = 0
while adi != random.randint(0, 9):
    adi = int(input("intentelo nuevamente: ")) 
    intentos += 1
print("felizitaciones, la cantidad de intentos fueron de: ", intentos)
print("__________________________________________________________________________________")
"""
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
"""
print("actividad 6")
for i in range(100, -1,-2):
    print("los numeros son: ", i)
print("__________________________________________________________________________________")
"""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""
print("actividad 7")
n_u = int(input("ingrese un numero: "))
sum_act7 = 0
for i in range(0, n_u):
    sum_act7 = sum_act7 + i
print("la suma de los numeros es de: ", sum_act7)
print("__________________________________________________________________________________")
"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""
print("actividad 8")
con_positivos = 0
con_negativos = 0
con_pares = 0
con_impares = 0
for i in range(10):
    num_entero_act8 = int(input("ingrese un numero: "))
    if num_entero_act8 % 2 == 0:
        con_pares += 1
    else:
        con_impares += 1
    
    if num_entero_act8 > 0:
        con_positivos += 1
    else:
        con_negativos += 1
print("la cantidad de pares es de: ", con_pares)
print("la cantidad de impares es de: ", con_impares)
print("la cantidad de numeros positivos es de: ", con_positivos)
print("la cantidad de numeros negativos es de: ", con_negativos)
print("__________________________________________________________________________________")
"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""
print("actividad 9")
suma_numeros = 0
cantidad = 0
for i in range(20):
    numeros = int(input("ingrese un numero: "))
    suma_numeros = suma_numeros + numeros
    cantidad = cantidad + 1

media = suma_numeros / cantidad
print("la media de la cantidad de numeros es de: ", media)
print("__________________________________________________________________________________")
"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""
print("actividad 10")
numero_de_usuario = int(input("ingrese un numero: "))
numero_invertido = 0
while numero_de_usuario != 0:
    residuos = numero_de_usuario % 10
    numero_invertido = numero_invertido * 10 + residuos
    numero_de_usuario = numero_de_usuario // 10

print("el numero invertido es: ", numero_invertido)
print("__________________________________________________________________________________")
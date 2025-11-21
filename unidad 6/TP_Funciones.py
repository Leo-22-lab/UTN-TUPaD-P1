"""
1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
"""
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()
"""
2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
"""
def saludar_usuario(nombre):
    print("Hola", nombre)

saludar_usuario("Marcos")
"""
3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
 Pedir los datos al usuario y llamar a esta función con los valores ingresados.
"""
def informacion_personal(nombre, apellido,edad, residencia):
    print("soy", nombre, apellido, "tengo", edad, "años y vivo en", residencia)

nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad = int(input("ingrese su edad: "))
residencia = input("ingrese su recidencia: ")
informacion_personal(nombre, apellido, edad, residencia)
"""
4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
"""
import math
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = int(input("ingrese el radio: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print("el area es: ", area)
print("el perimetro es: ", perimetro)
"""
5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
"""
def segundos_a_horas(segundos):
    return segundos/3600

segundos = int(input("ingrese los segundos: "))
horas = segundos_a_horas(segundos)
print("los segundos: ", segundos, "son igual a: ", horas, "horas")
"""
6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.
"""
def tabla_multiplicar(numero):
    for n in range(0,11):
        resultado = numero * n
        print("la tabla de multiplicar de ", numero, "es: ", resultado)
    
numero = int(input("ingrese un numero: "))
tabla_multiplicar(numero)
"""
7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos.
Mostrar los resultados de forma clara.
"""
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    divicion = a / b
    print("la suma de los numeros es: ", suma, "\nla resta de los numeros es: ", resta, 
        "\nla multiplicacion de los numeros es de: ", multiplicacion, "\nla divicion de los numeros es de: ", divicion)
    
a = int(input("ingrese el primer numero: "))
b = int(input("ingrese el segundo numero: "))
operaciones_basicas(a,b)
"""
8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
"""
def calcular_imc(peso, altura):
    cuadrado = altura**2
    resultado = peso/cuadrado
    print("el imc es de: ", resultado)

peso = int(input("ingrese el peso: "))
altura = float(input("ingrese la altura: "))
calcular_imc(peso,altura)
"""
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
"""
def celsius_a_fahrenheit(celsius):
    convercion = (1.8*celsius)+32
    print("los grados Celsius a Fahrenheit es de: ", convercion)

celcius = int(input("ingrese los grados celcius: "))
celsius_a_fahrenheit(celcius)
"""
10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
"""
def calcular_promedio(a, b, c):
    suma = a+b+c
    promedio = suma / 3
    print("el promedio de los tres numeros es: ", promedio)

a = int(input("ingrese el primer numero: "))
b = int(input("ingrese el segundo numero: "))
c = int(input("ingrese el tercer numero: "))
calcular_promedio(a,b,c)
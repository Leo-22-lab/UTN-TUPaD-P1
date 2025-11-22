def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Ingrese un número: "))

for i in range(1, num + 1):
    print(f"Factorial de {i} = {factorial(i)}")

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Ingrese una posición: "))

print("Serie de Fibonacci:")
for i in range(num + 1):
    print(fibonacci(i), end=" ")

def potencia(base, exp):
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)
 
b = int(input("Base: "))
e = int(input("Exponente: "))

print(f"{b}^{e} = {potencia(b, e)}")

def decimal_a_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"

    return decimal_a_binario(n // 2) + str(n % 2)
 
num = int(input("Ingrese número decimal: "))
print("Binario:", decimal_a_binario(num))

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])
 
texto = input("Ingrese una palabra: ").lower()
print(es_palindromo(texto))

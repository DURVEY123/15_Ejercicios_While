# Escribe un programa que solicite al usuario un número entero positivo y luego imprima la suma
# de los números de Fibonacci hasta ese número utilizando un bucle while.
num = int(input("INGRESAR UN NUMERO ENTERO POSITIVO: "))
suma = 0
d = 1
k = 0
if num <= 0: 
    print("INGRESAR UN NUMERO ENTERO POSITIVO.")
else:
    while k <= num:
        suma += k
        k, d = d, k + d
    print (f"LA SUMA DE LOS NUMEROS ES: {suma}")
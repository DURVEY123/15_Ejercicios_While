# Escribe un programa que solicite al usuario un número entero positivo y luego imprima el promedio
# de todos los números desde 1 hasta ese número utilizando un bucle while.
num = int(input("INGRESE EL NUMERO ENTERO POSITIVO: "))
suma = 0
contador = 0
n = 1
if num <= 0:
    print ("INGRESE UN NUMERO ENTERO POSITIVO.")
else:
 while n <= num:
    suma += n
    contador += 1
    n += 1
    promedio = suma / contador
 print( f"EL PROMEDIO DE LOS NUMEROS ES: {promedio}")
# Escribe un programa que solicite al usuario un número entero positivo y luego
# imprima los primeros n números impares utilizando un bucle while.
n = int(input("INGRESE EL NUMERO ENTERO POSITIVO: "))
if n <= 0:
    print("INGRESE UN NUMERO ENTERO POSITIVO.")
else:
    contador = 0     
    numero = 1
    while contador <= n:
        print (numero)
        numero += 2
        contador += 2
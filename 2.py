# Escribe un programa que solicite al usuario dos números enteros positivos
# y luego imprima todos los números entre ellos (inclusive) utilizando un bucle while.
num_1 = int(input("ESCRIBE EL PRIMER NUMERO ENTERO POSITIVO: "))
num_2 = int(input("ESCRIBE EL SEGUNDO NUMERO ENTERO POSITIVO: "))
if num_1 <= 0 or num_2 <= 0:
    print("ESCRIBE UN NUMERO ENTERO POSITIVO.")
else:
    if num_1 < num_2:
        menor = num_1
        mayor = num_2
    else:
        menor = num_2
        mayor = num_1
    contador = menor
    while contador <= mayor:
        print(contador)
        contador += 1
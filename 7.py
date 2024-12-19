# Escribe un programa que solicite al usuario un número entero positivo y luego imprima
# la suma de los primeros n números pares utilizando un bucle while.
num = int(input("INGRESAR UN NUMERO ENTERO POSITIVO: "))
suma = 0
contador = 0
numero = 0
if num <= 0: 
    print("INGRESA UN NUMERO ENTERO POSITIVO.")  
else:
 while contador < num:
    if numero % 2 == 0:
        suma += numero
        contador += 1
    numero += 1
print(f"LA SUMA DE LOS PRIMEROS NUMEROS PARES ES: {suma}")
# Escribe un programa que solicite al usuario dos números enteros positivos
# y luego imprima la suma de todos los números entre ellos (inclusive) utilizando un bucle while.
num_1 = int(input("INGRESA EL PRIMER NUMERO ENTERO POSITIVO: "))
num_2 = int(input("INGRESA EL SEGUNDO NUMERO ENTERO POSITIVO: "))
if num_1 <= 0 or num_2 <=0:
    print("INGRESA UN NUMERO ENTERO POSITIVO.")       
else:
 if num_1 > 0 or num_2 > 0:
    if num_1 > num_2:
         num_1, num_2 = num_1, num_2
    suma = 0
    actual = num_1
    while actual <= num_2:
          suma += actual
          actual += 1
    print(f"LA SUMA DE LOS NUMEROS ES: {suma}")       
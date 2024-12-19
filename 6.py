# Escribe un programa que solicite al usuario un número entero positivo y luego imprima
# la suma de los cuadrados de todos los números desde 1 hasta ese número utilizando un bucle while.
num = int(input("INGRESAR UN NUMERO ENTERO POSITIVO: "))
n = 1
suma = 0
if num <= 0:
    print ("INGRESAR UN NUMERO ENTERO POSITIVO.")
else:
 while n <= num:
      suma += n ** 2
      n += 1
 print(f"LA SUMA DE LOS CUADRADOS DE TODOS LOS NUMEROS ES: {suma}")
# Escribe un programa que solicite al usuario un número entero positivo y luego calcule la suma de todos los números
# divisibles por 3 desde 1 hasta ese número utilizando un bucle while.
num = int(input("ESCRIBA UN NUMERO ENTERO POSITIVO: "))
suma = 0
n = 1
if num <= 0:
   print("ESCRIBA UN NUMERO ENTERO POSITIVO.")
else:
   while n <= num:
      if n % 3 == 0:
          suma += n
      n += 1
   print (F"LA SUMA DE TODOS LOS NUMEROS ES: {suma}")
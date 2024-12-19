# Escribe un programa que solicite al usuario un número entero positivo y luego imprima todos los números
# entre 1 y ese número que sean múltiplos de 7 utilizando un bucle while.
num = int(input("ESCRIBA EL NUMERO ENTERO POSITIVO: "))
if num <= 0:
   print("ESCRIBA UN NUMERO ENTERO POSITIVO.")
else:
 i = 1
 while i <= num:
    if i % 7 == 0:
       print (i)
    i += 1
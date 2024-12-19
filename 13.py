# Escribe un programa que solicite al usuario dos números enteros positivos y luego imprima
# la tabla de multiplicar del primer número hasta el segundo número utilizando un bucle while.
num_1 = int(input("INGRESE EL PRIMER NUMERO ENTERO POSITIVO: "))
num_2 = int(input("INGRESE EL SEGUNDO NUMERO ENTERO POSITIVO: "))
if num_1 <= 0 or num_2 <= 0:
    print ("INGRESE UN NUMERO ENTERO POSITIVO.")
else:   
 if num_1 > num_2:
     num_1, num_2 = num_2, num_1
i = 1
while i <= 10:
    j = num_1
    while j <= num_2:
        print (f"LA TABLA DE MULTIPLICAR DESDE EL PRIMER NUMERO HASTA EL SEGUNDO ES: {j} X {i} = {j * i} ")
        j += 1
    print ()
    i += 1 
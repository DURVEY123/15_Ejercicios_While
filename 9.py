# Escribe un programa que solicite al usuario un número entero positivo y luego imprima todos los números
# entre 1 y ese número en orden inverso utilizando un bucle while.
numero = int(input("INGRESE UN NUMERO ENTRERO POSITIVO: "))
if numero <= 0: 
    print("INGRESE UN NUMERO ENTERO POSITIVO.")
else:    
    while numero >= 1:
        print (numero)
        numero-=1
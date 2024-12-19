# Escribe un programa que solicite al usuario un número entero positivo
# y luego imprima todos los números entre 1 y ese número que sean múltiplos de 5 utilizando un bucle while.    
numero = int(input("INGRESE UN NUMERO ENTERO POSITIVO: "))
if numero <= 0:
    print("POR FAVOR INGRESA UN NUMERO ENTERO POSITIVO.")
else:
    contador = 1
    while contador <= numero:
        if contador % 5 == 0:
            print(contador)  
        contador += 1  
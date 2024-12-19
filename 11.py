# Escribe un programa que solicite al usuario un número entero positivo y
# luego calcule la cantidad de dígitos del número utilizando un bucle while.
numero = int(input("INGRESA EL NUMERO ENTERO POSITIVO: "))
contador = 0
if numero <= 0:
      print ("INGRESA UN NUMERO ENTERO POSITIVO. ")
else:
 while numero > 0 :
    numero = numero // 10
    contador += 1
 print (f"el numero tiene {contador} digitos")
# Escribe un programa que solicite al usuario un número entero positivo y luego
# imprima si el número es un número de Armstrong utilizando un bucle while.
num = int(input("INGRESA UN NUMERO ENTERO POSITIVO: "))
if num <= 0: 
    print("INGRESA UN NUMERO ENTERO POSITIVO.")
else:
 n = num
 contador = 0
 num_digitos = len(str(num))
 while num > 0:
    digito = num % 10  
    contador += digito ** num_digitos  
    num //= 10  
 if contador == n:
    print(f"{n} ES UN NUMERO ARMSTRONG.")
 else:
    print(f"{n} NO ES UN NUMERO ARMSTRONG.")
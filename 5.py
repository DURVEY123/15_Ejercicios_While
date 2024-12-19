# Escribe un programa que solicite al usuario un número entero positivo y luego imprima todos los números
# primos menores o iguales a ese número utilizando un bucle while.
num = int(input("INGRESAR UN NUMERO ENTERO POSITIVO: "))
n = 2
if num <= 0 :
    print("INGRESAR UN NUMERO ENTERO POSITIVO.")
else:
    while n <= num:
        ES_PRIMO = True
        m = 2
        while m < n:
            if n % m ==0:
                ES_PRIMO = False
            m += 1
        if ES_PRIMO:
            print(m)
        n += 1    
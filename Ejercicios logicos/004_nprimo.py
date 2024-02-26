# 4 ¿Es un número primo?

'''
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
'''

# Esto está fatal madre mía

# Pero funciona :)

for n in range(0, 101):
    primos = {2, 3, 5, 7}
    if int(n) == 0 or int(n) == 1:
        print(f'{n} no es primo')
    elif int(n) % 2 == 0 and int(n) != 2: 
        print(f'{n} no es primo')
    elif int(n) % 3 == 0 and int(n) != 3: 
        print(f'{n} no es primo')
    elif int(n) % 5 == 0 and int(n) != 5: 
        print(f'{n} no es primo')
    elif int(n) % 7 == 0 and int(n) != 7:
        print(f'{n} no es primo')
    else:
        print(f'{n} es primo')
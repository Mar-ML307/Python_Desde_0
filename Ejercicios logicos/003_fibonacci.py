# 3 La sucesión de Fibonacci

'''
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
   la que el siguiente siempre es la suma de los dos anteriores.
   0, 1, 1, 2, 3, 5, 8, 13...
'''
#forma recursiva
def fib_r(n): 
    if n < 2: 
        return n
    return fib_r(n-1) + fib_r(n-2) 

for x in range(5):
   print(fib_r(x)) 

print('este es el primero')

#forma reiterativa
def fib(n):
    a = 0
    b = 1

    for k in range(n):
        c = a + b
        a = b
        b = c
        
    return b

for x in range(50):
    print(fib(x))



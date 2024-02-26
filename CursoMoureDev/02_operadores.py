### Operadores ###

# Es como hacer mates

print('Suma de 3 + 4')
print(3 + 4)
print('Resta de 3 + 4')
print(3 - 4)
print('Multiplicación de 3 + 4')
print(3 * 4)
print('División de 10 + 3')
print(10 / 3)

print('Operador de módulo, para saber lo que queda de resto ¿?')
print('10 % 3 = 3 +', 10 % 3)
print('Aparece 1 como resultado porque la operación sería 10/3 = 3 + 1')
print('10 % 2 = 5 +', 10 % 2)

# Otras operaciones más complejas que se pueden hacer con python
print(10 // 3) # aproxima la división, siempre da un número entero
print(2 ** 3) #exponente

# También se pueden sumar cadenas de texto (concatenación)
print('Hola' + ' Python' + ' ¿Qué tal?')

# No se pueden mezclar tipos diferentes, como por ejemplo str + int
numero = 5
print('Hola ' + str(numero))


'''
Ejemplo
suma = 5 + 3

respuesta = input('¿Cuánto es 5 + 3?  ')

if int(respuesta) == 8:
    print('Muy bien')
else:
    print('No, la solución es ' + str(suma))
'''

#Aunque sí funciona:
print('Hola' * 5)

### Operadores comparativos ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

#Comparar ordenación alfabética por ASCII
print('hola' > 'python')
print('hola' < 'python')
print('hola' <= 'python')
print(len('hola') >= len('python'))
print('hola' == 'python')
print('hola' != 'python')


### Operadores lógicos; lógica booleana ###
print(3 > 4 and 'hola' < 'python')
print(3 > 4 or 'hola' > 'python')
print(not(3 > 4))
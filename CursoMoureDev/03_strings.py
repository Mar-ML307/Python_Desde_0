### Strings ###

my_string = 'Mi string'
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + ' ' + my_other_string)

my_new_line_string = 'Este es un string\ncon salto de línea'
print(my_new_line_string)

my_new_tab_string = '\tEste es un string\n\tcon tabulación'
print(my_new_tab_string)

my_scape_string = '\tEste es un string \n escapado'
print(my_scape_string)


# Formateo 

name, surname, age = 'Mar', 'Mascarell', 22


print('Mi nombre es {} {} y mi edad es {} años'.format(name, surname, age)) # el primer texto formateado lo va a meter donde el %
print('Mi nombre es %s %s y mi edad es %d años' %(name, surname, age))
print(f'Mi nombre es {name} {surname} y mi edad es {age} años') #inferencuia de datos

'''
Se podría hacer concatenando, pero al final queda un código muy engorroso. 
Es más rápido y limpio hacerlo de la otra forma.
La opción de los % es mejor para formatear porque así te aseguras de que sea el 
tipo de variable correcto: %s para string, %d para int...
Si no, mejor la 3era forma.
'''

# Desempaquetado de caracteres

language = 'python'

a, b, c, d, e, f = language

print(a) 
print(b)


# División 

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)


# Reverse

reversed_language = language[::-1]
print(reversed_language)


# Funciones

print(language.capitalize())
print(language.upper())
print(language.count('t'))
print(language.isnumeric())
print('1'.isnumeric())
print(language.upper().isupper())
print(language.startswith('y'))
### Diccionarios ### 

my_dict = dict()
my_other_dict = {}

my_other_dict = {'Nombre': 'Mar', 'Apellidos': 'Mascarell', 'Edad': 22, 1: 'Python'}

my_dict = {
    'Nombre':'Mar', 
    'Apellidos':'Mascarell', 
    'Edad':22, 
    'Lenguajes':{'Python', 'Swift', 'Kotlin'},
    1:1.55
    }

print(my_dict)
print(my_other_dict)

'''
Permite almacenar datos de tipo clave valor
'''

print(len(my_other_dict))
print(len(my_dict))

print(my_other_dict['Nombre']) # Facilidad para acceder a un elemento

my_dict['Nombre'] = 'Sergio'
print(my_dict['Nombre'])

print(my_dict[1])

my_dict['Calle'] = 'Calle Mar y Sergio'
print(my_dict)

del my_dict['Calle']
print(my_dict)

print('Apellidos' in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())


my_new_dict = dict.fromkeys(('Nombre', 1, 'Piso'))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict )
print(my_new_dict)


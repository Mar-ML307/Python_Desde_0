### Tuples ###

# Una tupla es un conjunto de valores, como una lista pero no del todo:

my_tuple = tuple()

my_other_tuple = ()

my_tuple = (35, 1.55, 'Mar', 'Mascarell')
print(type(my_tuple))

print(my_tuple[-1])


# Las únicas dos funciones que tiene son estas. Son valores CONSTANTES, 
# no variables:

print(my_tuple.count('Mar'))
print(my_tuple.index('Mar'))

#my_tuple[1] = 1.8 TypeError: 'tuple' object does not support item assignment

del my_tuple  # la borra

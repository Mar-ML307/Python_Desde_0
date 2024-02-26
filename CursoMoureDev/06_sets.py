### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Incialmente es un dict

my_other_set = {'Mar', 'Mascarell', 22}
print(type(my_other_set))

print(len(my_other_set))

# print(my_other_set[0]) TypeError: 'set' object is not subscriptable

my_other_set.add('ocean307')
print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add('ocean307') # Un set no admite repetidos
print(my_other_set) 

print('Mascarell' in my_other_set)
print('Mascarel' in my_other_set)

my_other_set.remove('Mascarell')
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

my_set = {'Mar', 'Mascarell', 22, 34, 44, 4545, 423}
my_list = list(my_set)
print(my_list[0])

my_new_set = my_set.union(my_other_set)
print(my_new_set)
### Listas ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [22, 1.55, 'Mar', 'Mascarell']

print(type(my_other_list)) 

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list.count('Mar')) 

age, height, name, surname = my_other_list
print(name)

print(my_list + my_other_list)

my_other_list.append('Biotecnóloga')
my_other_list.insert(0, 'verde')
print(my_other_list)
my_other_list[0] = 'rojo'
#my_other_list.remove('verde')
print(my_other_list)

my_list.pop(2) # eliminar un valor, si no se especifica, el último
print(my_list)
my_pop_element = my_list.pop(2)
print(my_pop_element)

my_new_list = my_list.copy
my_list.clear

print(my_new_list)
print(my_new_list)
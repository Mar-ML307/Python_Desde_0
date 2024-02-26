### Functions ###

'''
Una función va a intentar resolver un problema muy concreto en 
un único lugar.
Para crear una función se utiliza la palabra def
'''

def my_function (): 
    print('Esto es una función')

my_function ()

''''
Pillar trocitos de código y agruparlos
'''

def sum_two_values (first_number, second_number):
    print(first_number + second_number)

sum_two_values (20, 30)
sum_two_values (453245, 30)
sum_two_values (20, 5468)
sum_two_values (245, 456)

def sum_two_values_with_return (first_number, second_number):
    my_sum = first_number + second_number
    return my_sum

my_result = sum_two_values_with_return(20, 30)
print(my_result)

def print_name (name, surname):
    print(f'{name} {surname}')

print_name(surname = 'Mascarell', name = 'Mar')

def print_name_with_default (name, surname, alias = 'sin alias'):
    print(f'{name} {surname}, {alias}')

print_name_with_default('Mar', 'Mascarell')
print_name_with_default('Mar', 'Mascarell', 'oce')

def print_texts(*texts):
    for text in texts:
        print(text.upper())

print_texts('hola', 'qué tal', 'me llamo mar')
### Loops ###

# while

my_condition = 1

while my_condition < 11:
    print(my_condition)
    my_condition += 1
else: # es opcional
    print('Mi condición es mayor o igual que 11')

while my_condition < 20:
    my_condition +=1
    if my_condition == 15:
        print('Mi condición es igual a 15')
        break
    print(my_condition)


# For
    
my_list = {35, 'mar', 62, 'clase', 30, 30, 17} # funciona para listas, sets, tuplas, diccionarios

for element in my_list:
    print(element)
else: 
    print('El bucle for ha finalizado')

for i in range(1, 101):
    #if i == 32:
    #    break
    print(i)
else: 
    print('El bucle for ha finalizado')
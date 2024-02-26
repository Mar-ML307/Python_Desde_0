# 2 ¿Es un anagrama?

'''
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.

'''
set_1 = {}
set_2 = {}
string_1 = input('Primera palabra:  ')
string_2 = input('Segunda palabra:  ')

if len(string_1) != len(string_2):
    print('No es un anagrama, no tienen el mismo número de letras')
elif string_1 == string_2:
    print('Una palabra no es anagrama de sí misma')
else:
    set_1 = list(string_1)
    set_2 = list(string_2)
    if sorted(set_1) == sorted(set_2):
        print(f'{string_1} es anagrama de {string_2}')
    else:
        print(f'{string_1} no es anagrama de {string_2}')

    

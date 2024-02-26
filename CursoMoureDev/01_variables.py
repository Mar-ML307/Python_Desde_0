
# En python habitualmente las variables se nombran sólo con texto
# y en minúsculas. Se pueden usar guiones bajos(_).
# Da un poco igual cómo lo hagas en verdad, pero mala idea hacerlo 
# de otra forma.

print('Voy a usar una variable string:')
mivariable = "Mi variable string"
print(mivariable)

print('Voy a usar una variable integer:')
my_int_variable = 25
print(my_int_variable)

print('Voy a usar una variable boolean:')
my_bool_varibale = False
print(my_bool_varibale)
print('False en este caso sería', type(my_bool_varibale))

# print puede llevar varios argumentos (concatenación de variables en un print)

print(mivariable,",", my_int_variable,",", my_bool_varibale)

my_int_to_str_variable = str(my_int_variable) # función str() para cambiar el tipo de variable a str
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))
print(type(my_int_variable))

print(type(print(mivariable,",", my_int_variable,",", my_bool_varibale))) # Tipo 'NoneType'

print('Este es el valor de my bool variable:', my_bool_varibale)



#Función len(), cuenta caracteres incluidos espacios
print(len(my_int_to_str_variable))

# Variables en una sola línea. No es la mejor de las ideas
# Puede ser un foco muy grande de errores
name, surname, alias, edad = "Mar", "Mascarell", "Oce", float(22)
print('Me llamo:', name, surname, '. Tengo ', edad, 'años. ' 'Y mi alias es', alias)

# Respecto a los inputs, me invento un jueguito:
 
firstname = input('¿Cómo te llamas linda/o?:  ')
lastname = input('¿Y tus apellidos, guape?:  ')
age = input('¿Cuántos años tienes?:  ')
afirmacion = 'Encantada de conocerte'
negacion = 'Vaya, no sé que me pasa hoy'
incomprension = 'No te he entendido, respóndeme otra vez'
bucle = 0

print(f'Ahh, así que te llamas {firstname} {lastname} y tienes {age} años, ¿no?')
respuesta = input('¿Estoy en lo cierto? ')

while bucle == 0:
    if respuesta == "sí" or respuesta == "Sí" or respuesta == "si" or respuesta == "Si":
        print(afirmacion)
        bucle = +1
    elif respuesta == "no" or respuesta == "No":
        print(negacion)
        bucle = +1
    else:
        print(incomprension)
        respuesta = input('¿Estoy en lo cierto o no?  ')




### Classes ###

class MyEmptyPerson: # la primera en mayúscula
    pass # para evitar el error por la clase vacía

print(MyEmptyPerson)

class Person:
    def __init__(self, name, surname, alias = 'sin alias') -> None:
        self.___name = name 
        self.___surname = surname
        self.full_name = f'{self.name} {surname}, {alias}'
    def get_name (self):
        return self.__name
    def walk(self):
        print(f'{self.name} está caminando')

my_person = Person('Mar', 'Mascarell')
print(f'{my_person.name} {my_person.surname}')
my_person.walk()

my_other_person = Person('Brais', 'Moure', 'Mouredev')
print(my_other_person.full_name)
my_other_person.walk()

sin_alias = Person('Héctor', 'Sánchez')
print(sin_alias.full_name)
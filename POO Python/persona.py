'''
class Persona():

    def __init__(self, nombre, apelido, edad):
        self.nombre = nombre
        self.apellido = apelido
        self.edad = edad

    def __str__(self):
        return f'{self.nombre} {self.apellido} tiene {self.edad} años'

    def es_mayor(self):
        return self.edad >= 18

    def es_menor(self):
        return not self.es_mayor()
    
andres = Persona('Andres', 'Garcia', 25)

print(andres.apellido)
'''

class Vector():
    def __init__(self, data):
        self._data = data

    def __str__(self):
        return f'{self._data}'
    
    def __len__(self):
        return len(self._data)

v = Vector([1, 2, 3, 4, 5])
print(len(v))
"""
Collections - Named Tuple
Túpla nomeada - São tuplas onde especificamos umnome e também parâmetros

"""

from collections import namedtuple

#1 - Definir o nome parâmetros
cachorro = namedtuple('cachorro', 'idade raça nome')

#2 - Definir o nome parâmetros
cachorro = namedtuple('cachorro', 'idade, raça, nome')

#3 - Definir o nome parâmetros
cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])

dog = cachorro(idade=2, raça='Poddle', nome='Pretinha')

print(dog)

print(dog[0])
print(dog[1])
print(dog[2])

print(dog.idade)
print(dog.raça)
print(dog.nome)

print(dog.index('Poddle'))
print(dog.count('Poddle'))

"""
Collections - Ordered Dict:

É um dicionário Garante a ordem de inserção

"""

dicionario = {'a':8, 'c':2, 'b':3, 'd':4} # Ordem de inserção dos elementos não é garantida
print(dicionario)

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')


from collections import OrderedDict

dicionario1 =  OrderedDict({'a':45, 'b':21, 'c':33, 'd':13})

print(dicionario1)

for chave, valor in dicionario1.items():
    print(f'chave={chave}:valor={valor}')



dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})
print(odict1 == odict2)

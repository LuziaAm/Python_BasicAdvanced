"""
Operadores unários:  not

Operadores binários: and, or, is (comparação)

Uso do Not para negação

"""

ativo = True
logado = False

if ativo and logado:
    print('Bem vindo')
else:
    print('Faça o Login')

print(not ativo)
print(not logado)
print(ativo is True)
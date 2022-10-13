"""
Recebendo dados do usuário
"""

# Entrada
# print('Qual seu nome?')
# nome = input()  # entrada
nome = input('Qual seu nome?')
# print antigo
# print('Seja bem vindo(a) %s' % nome)
# Print moderno
# print('Seja bem vindo(a) {0}' .format(nome))
# print atual
print(f'Seja bem vindo(a) {nome}')
# print('Qual é sua idade?')
idade = int(input('Qual é sua idade?'))

# Processamento

# Saída
# print antigo
# print('A %s tem %s anos' % (nome, idade))
# Print moderno
# print('A {0} tem {1} anos' .format(nome, idade))
# print atual
print(f'A {nome} tem {idade} anos')

# exemplo de cast -> conversão de um tipo de dados para outro
# int(idade) -> É um Cast
print(f'A {nome} nasceu em {2022 - idade}')

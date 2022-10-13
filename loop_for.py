"""
For - Utilizamos para iterar sobre sequências ou valores iteráveis

"""

nome = 'Luzia Amorim'
lista = [1, 2, 3, 4, 5]
numeros = range(1,10) #Temos que transformar em lista

# Iterando em um string
for letra in nome:
    print(letra)

# Iterando sobre um lista
for numero in lista:
    print(numero)

# Range
for numero in range(1, 10):
    print(numero)

# Percorrer matriz
lista1 = ['Abacaxi', 'Maçã', 'Laranja', 'Uva']
lista2 = [1, 2, 3, 4]

for i in lista1:
    for j in lista2:
        print(lista2 + lista1)

# Enumerate - gera uma tupla (indice e letra)

for indice, letra in enumerate(nome):
    print(letra)

# Uso do _ para descartar valores
# end='' retira o /n padrao do python

for _, letra in enumerate(nome):
    print(letra, end='')

# Acesso ao valores do enumerate

for valor in enumerate(nome):
    print(valor)

# Range
# for i in range(len(lista)):
#     print(lista[i])

# qtd = int(input('QUantas vezes o loop deve rodar '))
# soma = 0
# for n in range(1, qtd+1):
#     num = int(input(f'Informe o {n}/{qtd} valor: '))
#     soma = soma + num
# print(f'A soma é {soma}')

# Tabela emojis https://apps.timwhitlock.info/emoji/tables/unicode

unicode = 'U+1F601'
midificado = 'U0001F60D'
for num in range(1, 11):
    print('\U0001F60D' * num)
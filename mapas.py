"""
Mapas são conhecidos como dicionários

Dicionários são representados por chave e valor

"""

receita = {'jan': 100, 'fev': 120, 'mar':300}
print(receita)
print(receita.keys())

# Iterar sobre dicinário
# for chave in receita:
#     print(chave)

# for chave in receita:
#     print(receita[chave])

# for chave in receita:
#     print(f'Em {chave} recebi R$ {receita[chave]}')

for chave in receita.keys(): # Recomendado
    print(receita[chave])

# Acessando os valores
print(receita.values())
for valor in receita.values(): # Recomendado
    print(valor)

print(receita.items()) # Gera um tupla chave e valor

# Desempacotamento de dicionários
for chave, valor in receita.items():
    print(f'Chave={chave} e valor={valor}')

# Soma*, valor max, valor min, tamanho ->> Se os valores forem todos inteiros ou reais
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

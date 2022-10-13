"""
Dicionário em outras linguagem são conhecidos como mapas. 

- São coleções do tipo Chave e Valor = 'chave:valor'
- São representados por {}
- Chave-Valor aceitam qualquer tipoo de dados
- Dicionário não são indexados
- Dicionário não podemos ter chaves repetidas

"""

from numpy import rec


paises = {'br': 'Brasil', 'eu': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai') # Menos de usar como dicionário
print(paises)
print(type(paises))

# Acessando elementos via Chave
print(paises['br'])
#print(paises['ru']) # Elemento não existe Keyerror
print(type(paises['br']))

# Acessando elementos via GET
print(paises.get('br'))
print(paises.get('ru')) # O tipo None sempre vai ser FALSO no python
print(type(paises.get('br')))

pais = paises.get('py')
if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

pais = paises.get('py', 'Não encontrei o país') # Podemos definir um valor padrão
print(pais)

pais = paises.get('ru', 'Não encontrei o país') # Se não encontrar o país coloca 'Não encontrei o país' no lugar
print(pais)

#Verificar se uma chave está no dicionário
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado(int, float, string,boolean), inclusive listas, tupla dicionario
# Tuplas podem ser usar como chaves de dicionário, por serem imutáveis
localidades = {
    (23.25888, 39.7898): 'Escritorio Brazil',
    (23.25888, 38.9898): 'Escritorio Canadá',
    (23.25888, 48.9898): 'Escritorio Estados Unidos',
}
print(localidades)
print(type(localidades))

# Adicionar elementos em um Dicionário

receita = {'jan': 100, 'fev': 120, 'mar':300}

print(receita)
print(type(receita))

# Forma mais comum
receita['abr'] = 350
print(receita)

# Update
novo_dado = {'mai': 500}
receita.update(novo_dado) # Igual a -> receita.update({'mai': 500})
print(receita)

# Atualizar valor
receita['mai'] = 550
print(receita)

# Atualizar valor como update
novo_dado = {'mai': 600}
receita.update(novo_dado) # Igual a -> receita.update({'mai': 500})
print(receita)


# REMOVER dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar':300}

#Forma1 - Remover com a chave.
#Quando remove o valor é retornado

ret = receita.pop('mar')
print(ret) #retorno do valor
print(receita)

#Forma2 - Remover com a del.

del receita['fev']
print(receita)

# KeyError
# del receita['fev']
# print(receita)

# COMPRAS

carrinho = []
produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('Jogo Ninja Lego', 1, 212.00)

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Usando TUPLAS
produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('Jogo Ninja Lego', 1, 212.00)

carrinho = (produto1, produto2)
print(carrinho)

# Teriamos que saber qual o indice de cada informação no produto

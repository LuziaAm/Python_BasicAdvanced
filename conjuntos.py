"""
Conjuntos - teoria dos conjuntos

Conjuntos em python são chamados de sets (não indexados)

Set não possuem valores duplicados, ordenados
Elementos não são acessados via índice

Armazena elementos sem precisar ordenar

Conjuntos vem entre {}

Diferença entra Set e Mapas

Mapas = {Chave:Valor}
Sets = {Valor}

Sets aceitando dados misturados

"""
# Forma 1

s = set({1, 2, 3, 4, 5, 6, 7, 8, 2}) # Com valor repetido

print(s)
print(type(s))

# Forma 2

s = set({1, 2, 2, 5, 5, 6, 7})
print(s)
print(type(s))

stringSet = set('Luzia Amorim')
print(stringSet)

listaToSet = [1, 1, 2, 4, 5, 6, 7, 7,7]

print(set(listaToSet))

if 3 in s:
    print("Tem o 3")
else:
    print('Não tem o 3')

# Set - sem valor duplicado e sem ordem
# dados = [99, 101, 2, 2, 55]
# print(dados)
# print(type(dados))

listaSet = [99, 101, 2, 2, 55]
print(f'Lista: {listaSet} com {len(listaSet)}')

tupla = 99, 101, 2, 2, 55
print(f'Tupla:{tupla} com {len(tupla)}')

dicionario ={}.fromkeys([99, 101, 2, 2, 55], 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)}')

conjunto = {99, 101, 2, 2, 55} # Ordena por ele mesmo
print(f'Conjunto: {conjunto} com {len(conjunto)}')

# Misturando tipos de dados

setMix = {1, 'a', True, 34.12, 44}
print(f'Set Mix: {setMix}')

for valor in setMix:
    print(valor)

# Manipular elementos repetidos na Lista

cidade = ['Belo Horizonte', 'São Paulo', 'Manaus', 'Cuiaba', 'Manaus', 'Curitiba', 'Curitiba']

print(f'Cidades: {cidade}')
print(f'Quantidade de Visitantes: {len(cidade)}')
print(f'Quantidade de Cidade: {(len(set(cidade)))}')

s =  {1, 2, 3}
s.add(4) # Não adciona duplicidade, e não gera erro
print(s)

# Remover
s.remove(3) # Remove valor, não indice, conjuntos não são indexados. Nenhum valor é retornado
print(s) # Caso o valor não exista gera KeyError

# Remover com Discard
s.discard(2) # Se o valor não exitir nenhum erro é gerado
print(s)

# Copiando um conjunto para outro

# Deep copy
novo = s.copy()
print(novo)

novo.add(3)
print(novo)

# Shelow copy

novo = s
novo.add(5)
print(novo)
print(s)

# Remover todos os item do conjunto
s.clear()
print(s)

s =  {1, 2, 3}
print(s)

# Metódos matemáticos de conjuntos
# Cconuntos

estudantes_cursopython = {'Luzia', 'Julia', 'Kamila', 'Joao', 'Maria'}

estudantes_java = {'Luzia', 'Julia', 'Mira', 'Pedro', 'Priscila', 'Carlos'}

#Utilizando - Union (Recomendado)

unicos1 =  estudantes_cursopython.union(estudantes_java)
unicos2 =  estudantes_java.union(estudantes_cursopython)
print(unicos1)
print(unicos2)

#Utilizando o Caractere | Pipe
unicos1 =  estudantes_cursopython | estudantes_java
unicos2 =  estudantes_java | estudantes_cursopython
print(unicos1)
print(unicos2)

# Gerar conjunto de estudantes que estão em ambos os grupos
# Utilizando Intersection

ambos1 = estudantes_cursopython.intersection(estudantes_java)
print(ambos1)
ambos2 = estudantes_cursopython & estudantes_java
print(ambos2)

# Gerar conjunto de estudantes que não estão no outro curso

so_python = estudantes_cursopython.difference(estudantes_java)
print(so_python)
so_java = estudantes_java.difference(estudantes_cursopython)
print(so_java)

# Soma, Max, Min, tamanho
s = {1, 2, 3, 4, 5, 6, 7}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))




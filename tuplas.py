"""
Tuplas (tuple): Tuplas são utilizada sempre que não for preciso modificar dados de uma coleção
- Tuplas usam ()
- São imutáveis
- São mais rápidas do que listas
- Deixam o código mais seguro, por ter elementos imuntáveis

"""
print(type(()))

#CUIDADO:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))


tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

#CUIDADO 2:
tupla3 = (4) #NÃO É UMA TUPLA
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # É UMA TUPLA
print(tupla4)
print(type(tupla4))

tupla5 = 4, # É UMA TUPLA
print(tupla5)
print(type(tupla5))

# RANGE
tupla_range = tuple(range(11))
print(tupla_range)
print(type(tupla_range))

# DESEMPACOTAMENTO
tupla = ('Luzia', 'Amorim')
escola, curso = tupla
print(escola)
print(curso)

# Manipulação permitida em tuplas
print(sum(tupla1))
print(max(tupla1))
print(min(tupla1))
print(len(tupla1))

#Concatenção
tupla_conca1 = (1, 2, 3)
tupla_conca2 = (4, 5, 6)
tupla_junta = tupla_conca1 + tupla_conca2
print(tupla_conca1 + tupla_conca2)
print(tupla_conca1)
print(tupla_conca2)
print(tupla_junta)
tupla_conca1 = tupla_conca1 + tupla_conca2 # Sobrescrevendo
print(tupla_conca1)

# Verificar elementos
print(3 in tupla1) # True
print(33 in tupla1)# False

# Iterando em tuplas
for n in tupla1:
    print(n)

for indice, valor in enumerate(tupla1):
    print(indice, valor)

# Contando elementos
tupla_string = ('a', 'b', 'c', 'a', 'a')
print(tupla_string.count('a'))

# Tupla de uma string
nome = tuple('Luzia Amorim')
print(nome)

print(nome.count('a'))

# Coleção que não precisa mudar
meses = ('Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun')
print(meses[5])

# Iterar com while
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificar o indice

print(meses.index('Mai'))

# Slicing
# tupa[inicio:fim:passo]

print(meses[2:5])

print(dir(tupla))
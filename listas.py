"""
Listas - Fincionam como vetores, matrizes(Array)
Dinâmicos e pode-se trabalhar qualquer tipo de dados

Representada entre colchetes []


"""

# lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

# lista2 = ['L', 'u', 'z', 'i', 'a']

# lista3 = []

# lista4 = list(range(11))

# lista5 = list('Luzia Amorim')

# num = 8

# if num in lista4:
#     print(f'Encontrei o número {num}')
# else:
#     print(f'Não encontrei o número {num}')

# # Ordenar Lista

# lista1.sort()
# print(lista1)

# # Contar ocorrÊncias na lista

# print(lista1.count(1))
# print(lista5.count('A'))

# # Adicionar elementos em uma lista
# # Append adiciona um elemento por vez
# # lista1.append(12, 34, 56) # Erro
# lista1.append(42)
# print(lista1)

# # Adicionar lista dentro de lista ou apenas um valor por vez
# lista1.append([8, 3, 7])
# print(lista1)

# if [8, 3, 7] in lista1:
#     print('Encontrei')
# else:
#     print('Não encontrei')

# # Extend - Insere mais de um valor e o valor é deslocado para a direita
# lista1.extend([123, 44, 67])
# print(lista1)

# #Insert - insere um valor em uma determinada posição

# lista1.insert(2, 'Novo')
# print(lista1)

# #JUntar duas listas

# lista6 = lista1 + lista2
# print(lista6)

# lista4.extend(lista5)
# print(lista4)

# # Lista inversa com reverse

# lista1.reverse() # Outra forma: lista1[::-1 ]
# print(lista1)

# # Copiar uma lista
# lista7 = lista4.copy()
# print(lista7)

# print('Tamanho', len(lista1))

# #Remover o ultimo iten da lista
# print(lista1)
# print(lista1.pop()) # retona o elemento retirado
# print(lista1)

# # Remover pelo indice 
# # Elementos deslocados para esquerda
# print(lista5)
# lista5.pop(2) 05p# print(lista5)

# #Limpar uma Lista
# print(lista5)
# lista5.clear()
# print(lista5)

# # repetir elemento de uma Lista em outra lista
# nova = lista2 * 3
# print(nova)

# # Transformando strings em uma lista
# # Split por padão é o ''. Mas vc pode separar por ','
# curso = 'Curso Python'
# print(curso)
# curso =  curso.split()
# print(curso)

# # Converter lista em strig

# curso = ' '.join(curso)
# print(curso)

# # Join
# curso =  curso.split()
# curso = '$'.join(curso)
# print(curso)


# # Iterando

# for elemento in lista1:
#     print(elemento)

# # Utilizandoo while

# carrinho = []
# produto = ''

# while produto != 'sair':
#     print("Adicione um produto ou digite 'sair' para Sair")
#     produto =  input()
#     if produto != 'sair':
#         carrinho.append(produto)

# for produto in carrinho:
#     print(produto)

cores = ['verde', 'amarelo', 'azul', 'branco']

lista_cores = list(enumerate(cores))
print(lista_cores)
for indice, cor in enumerate(cores):
    print(indice, cor)

#Listas aceitam valores repetidos

lista = []
lista.append(42)
lista.append(42)
print(lista)

# Encontra indice em ula lista

numeros = [5, 6, 7, 8, 5]

print(numeros.index(7)) # Caso não tenha um erro é retornado valueErro

print(numeros.index(5)) # Retorna o indice do primeiro valor encontrada


#Busca dentro de um range
print(numeros.index(5, 1))# Busca a partir do indice 1

#Busca dentro de um range, inicio/fim
print(numeros.index(5, 1, 5)) #Busca o valor 5 entre os indices 1 e 5

#lista[inicio:fim:passo]
#range[inicio:fim:passo]
# ----SILICES
lista = [1, 2, 3 , 4, 5]
print(lista[1::]) # não pega o primeiro (apartir do ince 1)
print(lista[-1:])
print(lista[-3:])
print(lista[-2])
print(lista[1::2]) # De dois em dois
print(lista[::-1])

meunome = ['Luzia', 'Amorim']
meunome.reverse()
print(meunome)


#Soma, max, min, tamanho

print('Soma', sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

#Transfomar uma lista em tupla

vet = [4, 6, 7]
print(vet)
print(type(vet))

tupla = tuple(vet)
print(tupla)
print(type(tupla))

# Desempacotar listas - Observar o numero de valores da lista com o numero de variaveis para receber

num1, num2, num3 = vet
print(num1)
print(num2)
print(num3)

# Cópia de lista (Shallow Copy e Deep Copy)
nova = lista.copy()
print(nova)
nova.append(6)
print(lista)
print(nova) #não altera a lista copiada Deep Copy

lista = [ 0, 9, 8]
print(lista)

nova = lista #Cópia
print(nova)

nova.append(7)
print(nova)
print(lista)# o Append na nova lista tbm foi adicionado na lista antiga, ambas ficaram como mesmo valor isso é Shallow Copy










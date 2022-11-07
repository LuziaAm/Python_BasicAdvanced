"""
Com parâmetro de entrada

Recebem dados para serem processadas dentro da mesma.

Funções:

- Não possuem entrada
- Não possuem saída
- Possuem entrada mas não possuem saída
- Não possuem entrada mas possuem saída
- Possui entrada e saída

"""

from traceback import print_tb
from FUNCOES.funcoes_com_retorno import quadrado_de_sete


def quadrado(numero):
    #return numero * numero
    return numero ** 2, numero ** 3

print(quadrado(7))
print(quadrado(8))

def diz_oi(nome):
    print(f'Oi {nome}')

#Chamada da Função
diz_oi('Luzia')

# Funções aceitam vários parâmetro de entrada
def soma(a, b):
    return a + b

def multiplca(a, b):
    return a * b

def outra(idade, msg, nome):
    return f'Olá {nome}, {msg} sua idade é {idade}'

print(soma(4, 6))
print(multiplca(8, 8))
print(outra(40, 'Bom dia!', 'Luzia'))

#print(soma(2)) #Typeerror

#Nomeando parâmetros
def nome_completo(nome, sobrenome):
    return f'Seu nome completo {nome} {sobrenome}'

print(nome_completo('Luzia', 'Amorim'))

# Parâmetro - São variáveis declaradas na definição de uma função;
# Agumentos - São dados passados durante a execução de uma função;
# A ordem dos argumento importa na hora da execução

# Agumentos nomeados (keywords Arguments)
print(nome_completo(nome='Luzia', sobrenome='Castro Amorim'))

nome =  'Priscila'
sobrenome = 'Amorim'

print(nome_completo(nome=nome, sobrenome=sobrenome))
# Modificando a ordem
print(nome_completo(sobrenome='Castro Amorim', nome='Luzia'))

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista_num = [1,2, 3, 4, 5, 6, 7]
print(soma_impares(lista_num))

tupla_num = 1, 2, 3, 4, 5, 6, 7
print(soma_impares(tupla_num))





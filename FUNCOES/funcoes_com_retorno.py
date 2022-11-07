"""
Funções com retorno

Não precisa necessariamente criar uma variável para receber o retorno de uma função. Podemos passar a execução da função para outra função.

Palavra reservada return
1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos em uma função retornar qualquer tipo de dados, e também multiplos valores.

"""
from random import random
from tkinter import N
from traceback import print_tb


numeros = [1, 2, 3, 4]
ret_pop = numeros.pop()
print(f'Retorno de pop: {ret_pop}')
print(numeros)

#Em python quando não retorna valores == None
#Refatorar a função
def quadrado_de_sete():
    #print(7*7)
    resultado = 7 * 7
    return resultado

#Variável que recebe o retorno da função]
ret = quadrado_de_sete()
print(f'Retorno: {quadrado_de_sete()}')
print(ret)

def diz_oi():
    print('Antes')
    return 'Oi '
    print('Depois')


alguem =  'Pedro!'
print(diz_oi() + alguem)

#Varios retornos
def nova_funcao():
    variavel = False #True, None, False.
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

#Retorno de multiplos valores
def outra_func():
    return 2, 3, 4

print(outra_func()) 
#Imprime no formato de Tupla
print(type(outra_func()))

# Jogo da Moeda
def joga_moeda():
    # Gera random entre 0 e 1
    #valor = random()
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

def eh_impar():
    numero = 6
    if numero % 2 !=0:
        return True
    # else:
    #     return False
    return False

print(eh_impar())
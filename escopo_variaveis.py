"""
Variáveis Globais -> Seu escopo pode ser utilizada em todo o programa

Variáveis Locais -> Seu escopo está limitada ao bloco que foi declarada

Uma variável em Python:

nome_da_variavel = valor_da_variavel

Python é de tipagem dinâmica - não é declado o tipo de dado:

Linguagem C:
int a = 20; (não necessita do int em Python)

"""

numero = 42
print(numero)
print(type(numero))

numero = 'Luzia'
print(numero)
print(type(numero))

# Variável global e Local

numero = 38 #Global

if numero > 10:
    novo = numero + 10 # Local
    print(novo)

print(novo)
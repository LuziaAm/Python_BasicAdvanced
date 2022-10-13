"""
PEP9 -Python Enhancement Proposal

São propostas de melhoria para a linguagem Python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica'

[1] - Utilize Camel Case para nomes de classes - Ex: CalculadoraCientifica

[2] - Utilize nomes em minúsculo, separados  por  underline  para funções ou variáveis

def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

[3] - Utilize 4 espaços para identação!!! Não é recomendado usar o TAB

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco são duas entre as classes e entre funções
    - Metodos em uma classe devem ser separados com uma unica linha em branco

[5] - imports devem ser sempre feitos em linhas separada,
    - Devem qser colocados no topo do arquivo, logo depois de quaisquer comentário ou docstring e antes de contantes ou variavéis.
Ex:

imports sys
imports os

from types import StringType, ListType

muitos:
from types import (
    StringType,
    ListType
)

[6] - Espaços em expressões e instruções

não faça:
funcao( algo[ 1 ], { outro: 2 } )

faça:
funcao(algo[1], {outro:2})

[7] -  Termine sempre um intrução com uma nova linha em branco
"""


class Calculadora:
    pass

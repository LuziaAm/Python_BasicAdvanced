"""
Collections - Default Dict:

Cria umm dicionário com um valor default
Pode ser usado o Lambda
Este valor será usado sempre que não houver um valor definido.
Caso tenhamos qu eacessar uma chave que não existe, essa chave será criada e o valor defaut atribuido.

Lambdas são funções sem nome, que podem ou não receber parâmetro de entrada e retornar valores.
"""

dicionario = {'curso':'Desemvovimento de Sistemas'}

print(dicionario)
print(dicionario['curso'])
#print(dicionario['outro']) # apresenta KeyError

from collections import defaultdict

dicionario = defaultdict(lambda: 0) # Lambda não recebe entrada e retorna 0
dicionario['curso'] =  'Python'

print(dicionario)

print(dicionario['outro'])

print(dicionario) # Adcionouo outro no dicionário



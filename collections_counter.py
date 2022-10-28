"""
Collections - Counter

High performance Container Datatypes

Counter -> recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um dicionário, contendo como chave
o elemento da lista passada como paraêmetroe como valor a quantidade de ocorrÊncias desse elemento.


"""
#Utilizando counter
from collections import Counter

lista = [1,1,1,1,2,2,2,3,3,3,4,5,5,6,6,7,7,8,8] # Pode utilizar qualque iterável(Tupla, Conjunto...)

#Utilizando o Counter
res = Counter(lista)
print(type(res))
print(res) #Chave e quantidade de ocorrências

#Utilizando String
print(Counter('Luzia de Castro Amorim'))

#Counter com texto

texto = "Inchado é o particípio do verbo inchar. Este verbo é muito utilizado pelos falantes do português, se referindo principalmente ao ato de aumentar de volume e ao ato de ficar vaidoso e orgulhoso. Enxado é a forma do verbo enxadar conjugado na 1. ª pessoa do singular do presente do indicativo: eu enxado."

palavra = texto.split()

print(palavra)

res = Counter(palavra)
print(res)

#Encontrando as 5 palavras com mais ocorreência no texto
print(res.most_common(5))
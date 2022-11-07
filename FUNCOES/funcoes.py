"""
Funções são trechos de códigos que executam um função especifica
Podem receber entrada de dados
Executa tarefas repetidas
Funções devem ser simples


Funções, exemplos:

print()
len()

Definir Funções Python de forma geral: USA-SE def

def nome_da_funcao(paramretro):
    bloco da função

nome_da_funcao sempre em letras minúsculas, e se for nome composto separa por underline(Snake Case)

paramretro de entrada são opcionais, onde tendo mais de um separa-se por vírgulas

bloco da função - Chamado também de corpo da função ou implementação, é onde o processamento acontece. Podendo ter ou não retorno.

"""

cores = ['azul', 'amarelo', 'rosa', 'vermelho']
cor = 'preto'

#Função integrada (Built-in) do Python print() - Funções prontas
print(cores)

cores.append('roxo')
print(cores)
#cor.append('roxo') #AttributeError: Erro de atribuição. Só usa em Listas
print(cor)

#Função que não precisa de dados de entrada
cores.clear()
print(cores)

# DRY - Não repita seu código

#Função
def diz_oi():
    print('diz_oi')

#Chamada da Função
diz_oi()

#Usando no Range
for n in range(5):
    diz_oi()

oi = diz_oi
print('aqui')
oi()




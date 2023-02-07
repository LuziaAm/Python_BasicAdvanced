"""
Funções com parêmetro padrão:
- Nos permite ser mais flexíveis nas funções
- Evita erros cm parâmetro incorreto
- Permite trabalhar com exemplos mais legíveis de código

Quais tipos de dados podemos utilizar como valores default para parâmetros?
- Podemos usar qualquer tipo de dados
"""
# Parâmetro opcional
print('Luzia Amorim')
print()

# Parâmetro obrigatório

def quadrado(numero):
    return numero ** 2

print(quadrado(3))
#print(quadrado()) # TypeError: quadrado() missing 1 required positional argument: 'numero'

# Parâmetro opcional
def exponencial(numero = 4, expoente = 2): # Se colocar valor no parâmetro fica como Padrão
    return numero ** expoente

print(exponencial(2, 3))
print(exponencial(3, 2))

print(exponencial(3))
print(exponencial(2, 5))
print(exponencial())

#OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.

#ERRO!
def teste(potencia, num=2):
    return num ** potencia

print(teste(6))

#TypeError
def soma(num1=2, num2=6): #num1, num2 são obrigatórios
    return num1 + num2

print(soma(4,3))
print(soma(4))#TypeError | Para não dar erro deve-se colocar o valor default na função
print(soma())#TypeError

# Exemplo
def mostrar_info(nome="Luzia", instrutor=False):
    if nome == "Luzia" and instrutor:
        return 'Bem vindo instrutor'
    elif nome == 'luzia':
        return 'Eu pensei qu evc fosse instrutor'
    return f'Olá {nome}'

print(mostrar_info())
print(mostrar_info(instrutor=True))
print(mostrar_info(True))
print(mostrar_info('Kamila'))

# Funções como parêmetro

def soma(num1, num2):
    return a + b

def mat(num1, num2, fun=soma):
    return fun(num1,num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))




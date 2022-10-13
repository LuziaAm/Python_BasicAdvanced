"""
Tipo - Float
O separador de casas decimais é oponto e não a vírgula

Ao converter números floats para inteiro nós perdemos precisão
"""

# Exemplo
num_errado = 1,4
num_certo = 1.4
tupla1, tupla2 = 1, 44
complexo = 5j
print(type(complexo))
print(num_certo, " ", num_errado, " ", tupla1, tupla2)
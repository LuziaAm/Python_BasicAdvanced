"""
Saindo de loops com Break

Funciona da mesma forma que nas linguagens C e Java

Utilizamos para sair de loos de maneira projetada.

"""

for numero in range(1, 10):
    if numero == 6:
        break
    else:
        print(numero)
print('Sai do loop')

while True:
    comando = input('Digite sair para sair')
    if comando == 'sair':
        break

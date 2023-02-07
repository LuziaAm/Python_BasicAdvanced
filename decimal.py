numero = (input('Digite um número inteiro:'))

lista = list(numero)


if len(lista) == 1:
    decimal = 0
else:
    decimal = lista[-2]

print(f'O dígito das dezenas é {decimal}')
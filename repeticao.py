"""
Estrutura condicionais

"""
idade = 66
if idade < 18 and idade > 0:
    print("Menor de idade")
elif idade > 17 and idade < 64:
    print("Maior de idade")
elif idade < 1:
    print('Recem nascido')
elif idade > 64:
    print('Idoso')
else:
    print('Idade fora do range')


segundos = int(input('Por favor, entre com o número de segundos que deseja converter:'))

dia = int(segundos // 86400)
horas = int((segundos - (dia * 86400)) // 3600)
minutos = int((segundos - (dia * 86400) - (horas * 3600))//60)
segundo = (segundos - (dia * 86400) - (horas * 3600) - (minutos * 60))

print(f'{dia} dias, {horas} horas, {minutos} minutos e {segundo} segundos')

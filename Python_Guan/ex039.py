print('-=-'*20)
print('Preciso me alistar?')
print('-=-'*20)
print('')

from datetime import date

ano1 = int(input('quando você nasceu? '))
data = date.today()
ano2 = '{}'.format(data.year)
idade = int(ano2) - ano1

print('')
if idade > 18:
    print('Hora de se alistar!')
else:
    print('você ainda não precisa se alistar.')
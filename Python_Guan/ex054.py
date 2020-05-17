print('-=-'*20)
print('')
print('-=-'*20)
print('-=-')

from datetime import date

check = 7

for c in range(0, 7):
    a = int(input('digite o ano de nascimento: '))
    if date.today().year - a < 18:
        check -= 1

print('\nNúmero de pessoas maiores de idade nessa lista: {}'.format(check))
print('\nNúmero de pessoas menores de idade nessa lista: {}'.format(7 - check))

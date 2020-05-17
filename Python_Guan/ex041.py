print('-=-'*20)
print('     Categorias de natação')
print('-=-'*20)
print('')

from datetime import date

ano1 = int(input('ano de nascimento: '))
ano2 = date.today().year
idade = ano2 - ano1

if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 25:
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')

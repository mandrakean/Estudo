print('-=-'*20)
print('anãlise de tupla')
print('-=-'*20)
print('')

from random import randint

lista = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os números são: ', end=' ')
for n in lista:
    print(n, end='; ')

print(f'O maior número é {max(lista)}.')
print(f'O menor número é {min(lista)}.')

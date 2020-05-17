print('-=-'*20)
print('Verificador numérico 2')
print('-=-'*20)
print('')

lista = (int(input('digite um valor: ')),
         int(input('digite um valor: ')),
         int(input('digite um valor: ')),
         int(input('digite um valor: ')))

print('-=-'*20)

print(f'o número 9 aparece {lista.count(9)} vezes.')

if 3 in lista:
    print(f'O número 3 aparece na posição {lista.index(3)+1}.')

print('Os números pares são', end=': ')
for x in lista:
    if x % 2 == 0:
        print(x, end='; ')

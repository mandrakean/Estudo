print('-=-'*20)
print('Soma dos números pares')
print('-=-'*20)
print('')
s = 0

for c in range(0, 6):
    n = int(input('digite um número: '))
    if n % 2 == 0:
        s += n

print('\n', s)

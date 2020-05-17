print('-=-' * 20)
print('Números Primos')
print('-=-' * 20)
print('-=-')

num = int(input('digite um número: '))
check = True
print('')

for c in range(2, num):
    if num % c == 0:
        check = False

if check is False:
    print('não é primo')
else:
    print('é primo.')

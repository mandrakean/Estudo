print('-=-'*20)
print('Tabuadas')
print('-=-'*20)
print('')

while True:
    n = int(input('digite um número: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')

print('-=-'*20)
print('Fibonacci')
print('-=-'*20)
print('')

c = int(input('digite o número de elementos fibonacci que vc quer ver: '))
ant = 1
num = 0
prx = 0
while c == 0:
    c = int(input('zero é invalido. digite outro número: '))

if c == 1:
    print('resultado: 0')
else:
    c -= 1
    print('resultado: 0', end=' ')

    while c != 0:
        prx = num + ant
        print(prx, end=' ')
        ant = num
        num = prx
        c -= 1

print('-=-'*20)
print('Fatorial')
print('-=-'*20)
print('')

n = int(input('digite um número: '))
no = n
f = n

if n == 1 or n == 0:
    f = 1
else:
    while n != 1:
        f *= (n - 1)
        n -= 1
print("o fatorial de {} é {}".format(no, f))

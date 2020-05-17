print('-=-'*20)
print('contagem e soma')
print('-=-'*20)
print('')

t = 0
c = 0
som = 0

while t != 999:
    t = int(input('digite um número: '))
    if t != 999:
        som += t
        c += 1

print('você digitou {} termo(s) e a soma é igual a {}'.format(c, som))

print('-=-'*20)
print('Progressão aritmética')
print('-=-'*20)
print('-=-')

t = int(input('digite o primeiro termo: '))
r = int(input('digite a razão: '))

for c in range(0, 10):
    t += r
    print(t)

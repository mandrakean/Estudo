print('-=-'*20)
print('Progressão aritmética')
print('-=-'*20)
print('-=-')

t = int(input('digite o primeiro termo: '))
r = int(input('digite a razão: '))
c = 1

print(t, end=" ")
while c != 10:
    t += r
    print(t, end=' ')
    c += 1

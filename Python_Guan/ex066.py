print('-=-'*20)
print('Contador maluco')
print('-=-'*20)
print('')

s = c = 0

while True:
    n = int(input('digite um número: '))
    if n == 999:
        break
    s += n
    c += 1
print(f' foram digitados {c} números e a soma vale {s}')

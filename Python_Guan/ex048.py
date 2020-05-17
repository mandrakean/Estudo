print('-=-'*20)
print('soma de todos os impares multiplos de 3 entre 1 e 500')
print('-=-'*20)
print('')
s = 0
for c in range(1, 501):
    if c == 1 or c % 2 == 1:
        if c % 3 == 0:
            s += c
print(s)

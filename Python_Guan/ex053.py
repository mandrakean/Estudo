print('-=-'*20)
print('Testador de Palindromo')
print('-=-'*20)
print('-=-')

frase = str(input('digite uma frase: ')).strip().replace(" ", '')
inv = frase[::-1]
check = True
a = 0

for c in range(0, len(frase)):
    if frase[a] != inv[a]:
        check = False
        a += 1

if check is True:
    print('é um palindromo.')
else:
    print('não é um palindromo.')

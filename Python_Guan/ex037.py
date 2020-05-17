print('-=-'*20)
print('     conversor de bases')
print('-=-'*20)
num = int(input('\nEscreva um número inteiro: '))
base = int(input('Qual será a base de conversão?\n'
                 '1 para binário;\n'
                 '2 para octal\n'
                 '3 para hexadecimal\n'
                 '>>> '))

if base == 1:
    print ('O valor muda para {}'.format(bin(num).replace('0b', '')))
elif base == 2:
    print('O valor muda para {}'.format(oct(num).replace('0o', '')))
elif base == 3:
    print('O valor muda para {}'.format(hex(num).replace('0x', '')))
else:
    print('comando inválido.')
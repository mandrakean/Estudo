print('-=-'*20)
print('qual é maior?')
print('-=-'*20)
num1 = int(input('\nDigite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print('')

if num1 > num2:
    print('{} é maior que {}'.format(num1, num2))
elif num1 < num2:
    print('{} é menor que {}'.format(num1, num2))
else:
    print('os dois números são iguais.')

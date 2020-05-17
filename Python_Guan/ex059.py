print('-=-'*20)
print('calculadora')
print('-=-'*20)
print('')

a = int(input('digite o primeiro valor: '))
b = int(input('digite o segundo valor: '))
x = 0
while x != 5:
    x = int(input('''escolha uma opção:
[ 1 ] sommar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
'''))
    if x == 1:
        print('a soma é ', a + b)
    elif x == 2:
        print('o produto é ', a * b)
    elif x == 3:
        if a > b:
            print('{} é maior'.format(a))
        else:
            print('{} é maior'.format(b))
    elif x == 4:
        a = int(input('digite o primeiro valor: '))
        b = int(input('digite o segundo valor: '))
print('FIM')

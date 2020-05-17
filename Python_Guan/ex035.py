a = int(input('digite o cumprimento da primeira reta: '))
b = int(input('digite o cumprimento da segunda reta: '))
c = int(input('digite o cumprimento da terceira reta: '))

if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print('formam um triangulo')
else:
    print('não formam um triangulo')

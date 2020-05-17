a = int(input('digite o cumprimento da primeira reta: '))
b = int(input('digite o cumprimento da segunda reta: '))
c = int(input('digite o cumprimento da terceira reta: '))
tipo = 'isosceles'
if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    if a == b == c:
        tipo = 'equilátero'
    elif a != b != c != a:
        tipo = 'escaleno'
    print('formam um triangulo {}'.format(tipo))
else:
    print('não formam um triangulo')

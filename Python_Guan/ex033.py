num1= int(input('digite o primeiro número: '))
num2= int(input('digite o segundo número: '))
num3= int(input('digite o terceiro número número: '))

if num1 > num2 and num1 > num3:
    print('o maior número é o {}'.format(num1))
elif num2 > num3:
    print('o maior número é o {}'.format(num2))
else:
    print('o maior número é o {}'.format(num3))

if num1 < num2 and num1 < num3:
    print('o menor número é o {}'.format(num1))
elif num2 < num3:
    print('o menor número é o {}'.format(num2))
else:
    print('o menor número é o {}'.format(num3))
v = int(input('qual a sua velocidade? '))
multa = (v - 80)*7

if v > 80:
    print('você foi multado! sua multa é {}'.format(multa))
else:
    print('tudo ok.')
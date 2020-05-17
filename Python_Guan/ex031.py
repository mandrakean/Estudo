km = int(input('quantos km é a viagem? '))

if km > 201:
    print('o valor é {}'.format(0.45 * km))
else:
    print('o valor é {}'.format(0.5 * km))

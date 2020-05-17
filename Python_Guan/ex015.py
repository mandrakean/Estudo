a = float(input('digite a quantidade de quilômetros andados: '))
b = int(input('digite a quantidade de dias de aluguel: '))
c = 60*b + 0.15*a
print('você pagará {:.2f} R$'.format(c))

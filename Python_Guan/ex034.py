sal = float(input('digite seu salário: '))

if sal > 1250.00:
    sal = sal + (sal * 0.10)
else:
    sal = sal + (sal * 0.15)
print('o novo salário será: {}'.format(sal))

print('=+'*20)
print('CAIXA ELETRÔNICO')
print('=+'*20)
print('')

ced = 50
tot = 0

valor = int(input("qual valor a ser sacado? "))

while True:
    if valor >= ced:
        valor -= ced
        tot += 1
    else:
        if tot > 0:
            print(f'total de {tot} cédulas de {ced} R$')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot = 0
        if valor == 0:
            break

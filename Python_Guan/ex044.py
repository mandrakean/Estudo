val = float(input('Valor do produto: '))
din_chq = val - (val * 0.1)
vis_card = val - (val * 0.05)
card_x2 = val
card_x3 = val + (val * 0.2)

cond = int(input('''qual a forma de pagamento?
                 1 - Dinheiro ou cheque (a vista)
                 2 - a vista no cartão
                 3 - 2x no cartão
                 4 - 3x ou mais no cartão
                 Digite um dos números acima: '''))

if cond == 1:
    print('o valor total será de {} R$'.format(din_chq))
elif cond == 2:
    print('o valor total será de {} R$'.format(vis_card))
elif cond == 3:
    print('o valor total será de {} R$'.format(card_x2))
elif cond == 4:
    print('o valor total será de {} R$'.format(card_x3))
else:
    print('entrada inválida.')
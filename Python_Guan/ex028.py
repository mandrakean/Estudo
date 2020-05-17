import random
num = random.randint(0, 1)
tes = input('pensei em um número você consegue adivinhar qual? ')

if tes == num:
    print('parabéns! vc acertou!')
else:
    print('que pena, você errou! o número era {}'.format(num))

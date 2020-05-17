print('-=-'*20)
print('Jogo de adivinha')
print('-=-'*20)
print('')

import random

num = random.randint(0, 10)
tes = input('pensei em um número entre 0 e 10 você consegue adivinhar qual? ')
t = 1

while tes != num:
    print('que pena, você errou!')
    tes = int(input('tente de novo: '))
    t += 1
print('parabéns! vc acertou! o seu numero de tentativas foi {}'.format(t))

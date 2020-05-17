print('-=-'*20)
print('Comparador de pesos')
print('-=-'*20)
print('-=-')

mg = 0
mp = 0

for p in range(1, 6):
    peso = float(input('peso da {}º pessoa: '.format(p)))
    if p == 1:
        mg = peso
        mp = peso
    else:
        if peso > mg:
            mg = peso
        elif peso < mp:
            mp = peso

print('o maior peso lido foi {} Kg e o menor foi {} Kg.'.format(mg, mp))


from random import choice

print('Vamos jogar jokenpô?'
      '\n1 - Pedra'
      '\n2 - Papel'
      '\n3 - Tesoura')
p1 = int(input('escolha um número acima: '))
joken = [1, 2, 3]
pc = choice(joken)

print('')
if p1 == 1 and pc == 2:
    print('Você escolheu pedra...')
    print('Eu escolhi Papel...')
    print('Resultado: Eu venci! ^_^')
elif p1 == 1 and pc == 3:
    print('Você escolheu pedra...')
    print('Eu escolhi tesoura...')
    print('Resultado: você venceu!')
elif p1 == 2 and pc == 1:
    print('Você escolheu papel...')
    print('Eu escolhi pedra...')
    print('Resultado: você venceu!')
elif p1 == 2 and pc == 3:
    print('Você escolheu papel...')
    print('Eu escolhi tesoura...')
    print('Resultado: Eu venci! ^_^')
elif p1 == 3 and pc == 1:
    print('Você escolheu tesoura...')
    print('Eu escolhi pedra...')
    print('Resultado: Eu venci! ^_^')
elif p1 == 3 and pc == 2:
    print('Você escolheu tesoura...')
    print('Eu escolhi papel...')
    print('Resultado: você venceu!')
elif p1 == pc:
    print('opa! empatamos')
else:
    print('ops! algo de errado ocorreu')


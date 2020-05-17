print('-=-'*20)
print('Par ou impar')
print('-=-'*20)
print('')

from random import randint

count = 0

while True:
    print('=+'*20)
    j = str(input('escolha par ou impar (P/I): ')).upper()[0]
    while j not in 'PI':
        j = str(input('escolha par ou impar (P/I): ')).upper()[0]
    jn = int(input('escolha um número: '))
    cn = randint(0, 9)

    print('')

    if (jn + cn) % 2 == 0:
        if j is 'P':
            print(f'Você escolheu {jn} e o computador escolheu {cn}...'
                  f'a soma é {jn + cn}, ou seja... PAR! Você ganhou!')
            count += 1
        if j is 'I':
            print(f'Você escolheu {jn} e o computador escolheu {cn}...'
                  f'a soma é {jn + cn}, ou seja... PAR! Você perdeu!!')
            break
    else:
        if j is 'P':
            print(f'Você escolheu {jn} e o computador escolheu {cn}...'
                  f'a soma é {jn + cn}, ou seja... IMPAR! Você perdeu!')
            break
        if j is 'I':
            print(f'Você escolheu {jn} e o computador escolheu {cn}...'
                  f'a soma é {jn + cn}, ou seja... IMPAR! Você ganhou!!')
            count += 1
    print('')
print(f"Você ganhou um total de {count} partida(s).")
print("FIM")

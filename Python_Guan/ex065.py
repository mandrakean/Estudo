print('-=-'*20)
print('Matemática a lot')
print('-=-'*20)
print('')

n = int(input('digite um número: '))
menor = n
maior = n
som = n
con = 1

c = str(input('quer digitar mais números (S/N)? ')).upper()
while c != "N":
    n = int(input('digite um número: '))

    if n > maior:
        maior = n
    if n < menor:
        menor = n
    som += n
    con += 1
    c = str(input('quer digitar mais números (S/N)? ')).upper()

print('O maior valor foi {}, o menor foi {} e a média de todos os valores foi {}.'.format(maior, menor, som/con))

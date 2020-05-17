print('-=-'*20)
print('')
print('-=-'*20)
print('-=-')

soma_idade = 0
NH = ''
IV = 0
mul = 0

for c in range(1, 5):
    print('----- {} PESSOA ------'.format(c))
    nome = str(input('nome: '))
    idade = int(input('idade: '))
    sexo = str(input('Sexo (M/F): '))
    soma_idade += idade
    if c == 1 and sexo in 'Mm:':
        iv = idade
        NH = nome
    if sexo in 'Mm' and idade > IV:
        IV = idade
        NH = nome
    if sexo in 'Ff' and idade < 20:
        mul += 1

media = soma_idade / 4
print('A média das idades é {}'.format(media))
print('o Homem mais velho tem {} anos e se chama {}'.format(IV, NH))
print('mulheres menores de 20 anos: {}'.format(mul))

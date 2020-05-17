print('-=-'*20)
print('Cadastro de pessoas')
print('-=-'*20)
print('')

sup18 = 0
h = 0
m20 = 0
teste = 'S'

while teste is 'S':
    idade = int(input('digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('digite o sexo (M/F): ')).upper().strip()[0]
    if idade < 20 and sexo is "F":
        m20 += 1
    if sexo is "M":
        h += 1
    if idade >= 18:
        sup18 += 1
    teste = ' '
    while teste not in 'SN':
        teste = str(input('quer fazer outro cadastro (S/N)? ')).upper().strip()[0]

print(f'Existem {sup18} pessoas maiores de 18 anos, {m20} mulheres abaixo de 20 anos e ao todo {h} homens.')

print('-=-'*20)
print('Identificação de Sexo')
print('-=-'*20)
print('')

sex = str(input('digite seu sexo (M/F): ')).strip().upper()[0]
while sex not in 'FfMm':
    sex = str(input('Resposta inválida, digite M ou F: ')).strip().upper()[0]
print('fim')
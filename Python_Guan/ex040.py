print('-=-'*20)
print('Calculadora de média')
print('-=-'*20)

nota1 = float(input('Primeira nota: '))
nota2 = float(input('segunda nota: '))
media = (nota1 + nota2)/2
if media < 5:
    print('Reprovado.')
elif 7 > media > 5:
    print('Em recuperação.')
else:
    print('aprovado.')

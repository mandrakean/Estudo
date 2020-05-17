print('-=-' * 10)
print('  Avaliação de empréstimo')
print('-=-' * 10)

val = float(input('\nQual o valor do imóvel? '))
sal = float(input('qual o seu salário? '))
anos = int(input('quer pagar em quantos anos? '))

prest = val / (anos*12)
vm = sal * 0.3

if prest <= vm:
    print('\nVocê pagara R$ {:.2f} por mês.'.format(prest))
else:
    print('\nDesculpe, seu emprestimo foi recusado por que a parcela excede 30% de seu salário.')


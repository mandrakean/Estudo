print('---'*15)
print(' '*10, 'Tabela de preços', ' '*11)
print('---'*15)

p = ('Lápis', 1.75, 'Borracha', 2.00,
     'Caderno', 15.90, 'Estojo', 25.00,
     'Transferidor', 4.20)

for n in range(0, len(p)):
     if n % 2 == 0:
          print(f'{p[n]:.<30}', end=' ')
     else:
          print(f'{n:>7.2f} R$')

print('---'*15)

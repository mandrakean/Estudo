print('-=-'*20)
print('Verificador numérico')
print('-=-'*20)
print('')

lista = ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'quatorze',
         'quinze', 'desesseis', 'desessete',
         'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número de 0 a 20: '))
    if 0 <= n <= 20:
        break
    print('tente novamente. ', end=' ')

print(f'vocÊ digitou o número {lista[n]}.')

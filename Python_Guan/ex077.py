print('-=-'*20)
print('Verificador de vogais')
print('-=-'*20)
print('')

t = ('aprender', 'programar', 'linguagem', 'python', 'curso')

for x in t:
    print(f'Na palavra {x.upper()} existem as vogais: ', end=' ')
    for y in x:
        if y in 'aeiou':
            print(y, end=' ')
    print('')

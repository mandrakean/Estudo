print('-=-'*20)
print('Cadastro de produtos')
print('-=-'*20)
print('')

total = sup1000 = barato = 0

while True:
    print('-'*20)
    print('Produto')
    print('-'*20)
    print('')
    nome = str(input('nome: '))
    preco = float(input('Preço: '))
    if preco > 1000:
        sup1000 += 1
    if total == 0:
        barato = preco
    else:
        if preco < barato:
            barato = preco
    total += preco

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('quer continuar (S/N)? ')).upper().strip()[0]
    else:
        break

print(f'''O total de compra foi {total:.2f} R$
Temos {sup1000} produtos custando mais de mil
O produto mais barato custou {barato:.2f} R$''')

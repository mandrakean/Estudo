print('-=-'*20)
print('Verificador numérico')
print('-=-'*20)
print('')

times = ('flamengo', 'santos', 'palmeiras', 'grêmio',
         'athletico-PR', 'são paulo', 'internacional',
         'corinthians', 'fortaleza', 'goiás', 'bahia',
         'vasco', 'atlético-MG', 'fluminense',
         'botafogo', 'ceará', 'cruzeiro', 'csa',
         'chapecoense', 'avaí')

print(f'lista de times: {times}. \n')

print(f'Primeiros 5 colocados: {times[:5]}. \n')

print(f'ultimos 4 colocados: {times[-4:]}. \n')

print(f'Todos em ordem alfabética: {sorted(times)}. \n')

print(f'O chapecoense está na {times.index("chapecoense")+1}ª posição.')


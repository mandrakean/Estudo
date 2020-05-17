import random

a = input('escreva o nome do aluno 1: ')
b = input('escreva o nome do aluno 2: ')
c = input('escreva o nome do aluno 3: ')
d = input('escreva o nome do aluno 4: ')
nomes = [a, b, c, d]
random.shuffle(nomes)
print('a ordem será: {}'.format(nomes))

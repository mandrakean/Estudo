import random

a = input('escreva o nome do aluno 1: ')
b = input('escreva o nome do aluno 2: ')
c = input('escreva o nome do aluno 3: ')
d = input('escreva o nome do aluno 4: ')
print('o aluno escolhido é o {}'.format(random.choice([a, b, c, d])))

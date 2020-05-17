frase = input("digite uma frase: ").strip().lower()
print('a letra a aparece {} vezes, sendo a primeira vez na posição {} e a ultima na posição {}'.format(frase.count('a'), frase.find('a')+1, frase.rfind('a')+1))

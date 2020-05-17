print('-=-'*20)
print('Progressão aritmética')
print('-=-'*20)
print('-=-')

t = int(input('digite o primeiro termo: '))
r = int(input('digite a razão: '))
c = 0
ad = 1

print(t, end=" ")
while c != 9:
    t += r
    print(t, end=' ')
    c += 1

while ad != 0:
    ad = int(input('\nvocê quer ver quantos termos a mais? (digite 0 (zero) para parar \n'))
    if ad != 0:
        c = 0
        while c != ad:
            t += r
            print(t, end=' ')
            c += 1
print("FIM")
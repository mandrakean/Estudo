ano = int(input("ano: "))
bi = False

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    bi = True

print('é bissexto? {}'.format(bi))

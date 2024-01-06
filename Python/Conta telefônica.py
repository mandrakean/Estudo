m = int(input("minutos: "))

if m < 200:
    t = 0.2
elif m >= 200:
    t = 0.18
elif m >= 400:
    t = 0.15

conta = m * t

print("sua conta é de R$ %.2f" %conta)

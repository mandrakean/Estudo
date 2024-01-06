vel = int(input("qual a velocidade do carro? "))
if vel > 110:
    val = (vel - 110) * 5
    print ("Você foi multado: R$ %.2f" %val)

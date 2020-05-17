alt = float(input('digite a altura: '))
pes = float(input('digite o peso: '))
imc = pes/(alt**2)

if imc < 18.5:
    print('status: Abaixo do peso')
elif 18.5 <= imc < 25:
    print('status: Peso ideal')
elif 25 <= imc < 30:
    print('status: sobrepeso')
elif 30 <= imc < 40:
    print('status: obesidade')
elif imc >= 40:
    print('status: obesidade mórbida')

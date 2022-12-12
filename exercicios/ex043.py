peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce está ABAIXO DO PESO normal')
elif imc < 25:
    print('PARABENS, você está na faixa de PESO NORMAL')
elif imc < 30:
    print('Você está em SOBREPESO')
elif imc < 40:
    print('Você está em OBESIDADE, cuidado!')
elif imc > 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado')

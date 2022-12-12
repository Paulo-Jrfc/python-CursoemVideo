salário = float(input('Qual é o salário do funcionário? '))
salário_aumento = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a ganhar R${:.2f}'.format(salário, salário_aumento))

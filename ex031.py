distância = int(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar a viagem de {}Km.'.format(distância))
'''if distância <= 200:
    preço = distância * 0.50
    print('E o preço da sua passagem será de R${}'.format(preço))
else:
    preço = distância * 0.45'''
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${}'.format(preço))

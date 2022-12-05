preço = float(input('Qual é o preço do produto? '))
preço_desconto = preço - (preço*0.05) #ou preço - (preço* 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(preço, preço_desconto))

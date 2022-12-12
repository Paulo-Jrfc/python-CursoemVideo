print('-' * 30)
print('LOJA SUPER BARATÃO')
print('-' * 30)
total = prod1000 = barato = c = 0
nome_barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    c += 1
    total += preço
    if preço > 1000:
        prod1000 += 1
    if c == 1 or preço < barato:
        nome_barato = produto
        barato = preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {prod1000} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_barato} que custa {barato}')

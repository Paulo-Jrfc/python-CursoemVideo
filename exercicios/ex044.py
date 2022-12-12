print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vitas dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = (preço + (preço * 20 / 100)) / totparc
    novo = parcela * totparc
    print('Sua compra será parcelada em {}x de R${} COM JUROS'.format(totparc, parcela))
else:
    total = 0
    print('\033[31mOPÇÃO INVÁLIDA de pagamento. Tente novamente!\033[m')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))

import moeda
p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p, "US$")} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'Aumentou 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuiu 10%, temos {moeda.moeda(moeda.diminuir(p, 10))}')

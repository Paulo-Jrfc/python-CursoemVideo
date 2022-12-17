import moeda
p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.metade(p)}')
print(f'Aumentou 10%, temos R${moeda.aumentar(p, 10)}')
print(f'Diminuiu 10%, temos R${moeda.diminuir(p, 10)}')

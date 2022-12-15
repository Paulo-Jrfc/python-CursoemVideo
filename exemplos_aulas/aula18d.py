galera = list()
dado = list()
for c in range(0, 3):
    print('-' * 20)
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera[:])

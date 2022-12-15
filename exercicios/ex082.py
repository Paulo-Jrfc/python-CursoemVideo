lista = list()
pares = list()
ímpares = list()
while True:
    n = (int(input('Digite um número: ')))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        ímpares.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()
    if resp == 'N':
        break
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {ímpares}')

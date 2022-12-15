valores = [[], []]
n = 0
pares = list()
ímpares = list()
for c in range(1, 8):
    n = (int(input(f'Digite o {c}° valor: ')))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
valores.append(pares[:])
valores.append(ímpares[:])
valores[0].sort()
valores[1].sort()
print('-=' * 30)
print(f'A lista de pares é {valores[0]}')
print(f'A lista de impares é {valores[1]}')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma3 = maior2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if matriz[l][2]:
            soma3 += matriz[l][2]
        if matriz[1][0]:
            maior2 = matriz[1][0]
        if matriz[1][c] > maior2:
            maior2 = matriz[1][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {maior2}')

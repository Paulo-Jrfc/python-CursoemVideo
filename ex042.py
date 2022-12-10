r1 = int(input('Primeiro seguimento: '))
r2 = int(input('Segundo seguimento: '))
r3 = int(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 == r2 or r1 == r3:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo!')

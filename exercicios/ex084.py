galera = list()
pessoas = list()
mai = men = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(galera) == 0:
        mai = men = pessoas[1]
    else:
        if pessoas[1] > mai:
            mai = pessoas[1]
        if pessoas[1] < men:
            men = pessoas[1]
    galera.append(pessoas[:])
    pessoas.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break



print('-=' * 40)
print(f'Ao todo você cadastrou {len(galera)} pessoas')
print(f'O maior peso foi de {mai}kg. Peso de ', end='')
for p in galera:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {men}kg. Peso de ', end='')
for p in galera:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print()

mais18 = m = mulher20 = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F] ')).strip().upper()[0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        m += 1
    if idade < 20 and sexo == 'F':
        mulher20 += 1
    print('-' * 30)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {m} homens cadastrados')
print(f'E temos {mulher20} mulheres com menos de 20 anos')

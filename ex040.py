n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, m))
if m <= 5:
    print('O aluno está REPROVADO')
elif m <= 6.9:
    print('O aluno está de RECUPERAÇÃO')
else:
    print('O aluno está APROVADO')


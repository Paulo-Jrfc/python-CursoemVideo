from random import randint
print('-=' * 30)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 30)
computador = randint(1, 11)
v = 0
while True:
    n = int(input('Diga um valor: '))
    jogador = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    if jogador != 'P' and jogador != 'I':
        print('ESCOLHA INVÁLIDA! Escolha novamente')
        jogador = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    if jogador == 'P':
        computadorpi = 'I'
    else:
        computadorpi = 'P'
    total = n + computador
    if total % 2 == 0:
        pi = 'DEU PAR'
        if jogador == 'P' and pi == 'DEU PAR':
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    else:
        pi = 'DEU IMPAR'
        if jogador == 'I' and pi == 'DEU IMPAR':
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('-' * 30)
    print(f'Você jogou {n} e o computador {computador}. Total de {total} {pi}')
    print('-' * 30)
print('-=' * 30)
print(f'GAME OVER! Você venceu {v} vezes.')

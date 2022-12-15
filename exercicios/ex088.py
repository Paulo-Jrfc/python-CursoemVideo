from random import randint
from time import sleep
print('-' * 30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-' * 30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(1, jogos+1):
    sorteio = [randint(1, 60), randint(1, 60), randint(1, 60),
               randint(1, 60), randint(1, 60), randint(1, 60)]
    sorteio.sort()
    print(f'Jogo {c}: {sorteio}')
    sleep(0.5)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)

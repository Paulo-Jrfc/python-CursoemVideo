from math import radians, sin, cos, tan
a = float(input('Digite o âmgulo que você deseja: '))

seno = sin(radians(a))
cosseno = cos(radians(a))
tangente = tan(radians(a))

print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(a, seno))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(a, cosseno))
print('O ângulo de {:.2f} tem o TANGENTE de {:.2f}'.format(a, tangente))

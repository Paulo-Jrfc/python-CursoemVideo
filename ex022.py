nome = str(input('Digite o seu nome completo: ')).strip()
print('Analizando o seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nom tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
# print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {}, e ele tem {} letras'.format(separa[0], len(separa[0])))
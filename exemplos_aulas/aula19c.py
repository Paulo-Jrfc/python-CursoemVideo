pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 29}
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k in pessoas.keys():
    print(k)
print('-' * 30)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-' * 30)
for k in pessoas.values():
    print(k)

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 29}
for k in pessoas.keys():
    print(k)
print('-' * 30)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-' * 30)
for k in pessoas.values():
    print(k)

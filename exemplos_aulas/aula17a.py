num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort(reverse=True)
print(num)
num.insert(2, 0)
print(num)
num.pop(2)
print(num)
num.insert(2, 2)
print(num)
num.remove(2)
print(num)
if 4 in num:
    num.remove(4)
    print(num)
else:
    print('Não achei o número 4')
print(f'Essa lista tem {len(num)} elementos')

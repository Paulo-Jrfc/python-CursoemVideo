medida = float(input('Digite uma distancia em metros: '))
km = medida/1000
hm = medida/100
dam = medida/10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))

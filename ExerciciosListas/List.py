list = []
list.append('1°Termo')
print(list)

CartoesAmarelos = []
CartoesAmarelos.append('Luis Fabiano')
CartoesAmarelos.append('3 minutos')
print(CartoesAmarelos)

CartoesAmarelos.append('Neymar')
CartoesAmarelos.append('78 minutos')
print(CartoesAmarelos)


CartoesAmarelos[3] = '80 minutos'
print(CartoesAmarelos)

print(len(CartoesAmarelos))


valores = [1,2,3,4,5,6,7,8,9,10]
print(valores[5:10])
print(valores[3:])

#clonagem de lista
Lista1 = [3,56,6,4]
Lista2 = Lista1[:]
Lista2.append(10000)
print(Lista1,Lista2)


#delete 
valores = [1,2,3,4,5,6,7,8,9,10]
del valores[2]
print(valores)

#delete por faixa
valores = [1,2,3,4,5,6,7,8,9,10]
del valores[2:6]
print(valores)

alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(alfabeto[0:13])
print(alfabeto[13:27])
print(alfabeto[13:])
letra = alfabeto[1:10]
print(len(alfabeto))

valores = [1,2,7,2,4,6,1,3,4,86]
valores.sort()
print(valores)


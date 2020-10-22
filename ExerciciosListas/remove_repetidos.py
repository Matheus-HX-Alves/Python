
def remove_repetidos(lista):
    lista.sort()
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return print (l)

lista = [2, 4, 2, 2, 3, 3, 1]
remove_repetidos(lista)


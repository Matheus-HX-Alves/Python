lista = [4,2,3,8,6,9,5,2,5,7,6,56,4,6,1,3,5,2,45,3,56]

def maior_elemento(lista):
    x = 0
    for Maior in lista:
        if Maior > x:
            x = Maior
    return print(x)


maior_elemento(lista)


def maior_elemento(lista):
    x = 0
    for Maior in lista:
        if Maior > x:
            x = Maior
    return x


maior_elemento([-90, -27, -12])
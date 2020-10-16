largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))
i = largura
while altura > 0:
    largura = i
    while largura > 0:
        print ('#', end = "")
        largura -= 1
    print(end = "\n")
    altura -= 1 
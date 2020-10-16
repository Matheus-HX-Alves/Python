largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))

i = largura
k = altura

while altura > 0:
    largura = i
    while largura > 0:
        if largura == 1 or largura == i or altura == k or altura == 1:
            print ('#', end = "")
            largura -= 1
        else:
            print('', end=" ")
            largura -= 1
    print(end = "\n")
    altura -= 1 

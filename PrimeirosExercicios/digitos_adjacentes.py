#PENDENTE

x = int(input("Digite um número inteiro: "))
i = x % 10
print (i)
y = x

Verific = True

while Verific:
    if x <= 10:
        print('não')
        Verific = False
    x = x // 10
    if i != y and verific:
        y = i
        i = x % 10
        print (i , y)
        if x // 10 == 0 and y != i:
            print('não')
            Verific = False
    else:
        print ('sim')
        Verific = False


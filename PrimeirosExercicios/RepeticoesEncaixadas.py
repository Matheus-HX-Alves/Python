linha = 1
coluna = 1

while linha <= 10:
    while coluna <= 10:
        print(linha * coluna, end="\t")
        coluna += 1
    linha += 1
    coluna = 1
    print()
    

def Fat(x):    
    i = x
    if x == 0:
        x = 1
    else:
        while i > 1:
                i = i - 1
                x = x * i 
    print(x)
#'Fatorial
Verific= True
x = 0
i = 0
while Verific:
    x = int(input("Digite um numero: "))
    if x < 0:
        Verific = False
    else:
        Fat(x)


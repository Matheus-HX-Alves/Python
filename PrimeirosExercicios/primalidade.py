x = int(input('Digite um número inteiro: '))
y = x - 1
o = None
Verif = True

while Verif:
    o = x % y
    if o  == 0 and y > 1:
        print('não primo')
        Verif = False
    elif y == 1: 
        print('primo')
        Verif = False
    else:
        y = y - 1
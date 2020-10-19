def TransformaNota(Nota):
    if Nota >= 9.0:
        Nota = str('A')
    elif Nota >= 8.0:
        Nota = str('B')
    elif Nota >= 7.0:
        Nota = str('C')
    elif Nota >= 6.0:
        Nota = str('D')
    elif Nota >= 5.0:
        Nota = str('E')
    else: 
        Nota = str('F')
    print(Nota)


Nota = int(input('Digite qual a nota do estudante: '))
TransformaNota(Nota)
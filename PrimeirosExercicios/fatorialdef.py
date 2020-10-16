
def Fatorial(x):
    i = 1
    while x > 1:
        i = i * x
        x = x -1
    return i

def testa_fatorial():
    if Fatorial (1) == 1:
        print("Fnc 1")
    else:
        print("N func 1")
    if Fatorial (2) == 2:
        print("Fnc 2")
    else:
        print("N func 1")
    if Fatorial (0) == 1:
        print("Fnc 0")
    else:
        print("N func 0")

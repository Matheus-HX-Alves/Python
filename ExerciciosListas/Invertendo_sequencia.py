Lista = []
x = None
Verific = True

while Verific:
    x = int(input("DIgite um número: "))
    y =+ 1
    if x == 0:
        Verific = False
    else:
        Lista.append(x)

Lista.reverse()
for i in Lista:
    print(i)

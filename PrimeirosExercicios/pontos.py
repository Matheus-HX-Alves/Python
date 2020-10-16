import math

x1 = float(input("Digite um número para x1: "))
y1 = float(input("Digite um número para y1: "))
x2 = float(input("Digite um número para x2: "))
y2 = float(input("Digite um número para y2: "))

DistanciaAB =  math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
if DistanciaAB >= 10:
    print ("longe")
else:
    print("perto")
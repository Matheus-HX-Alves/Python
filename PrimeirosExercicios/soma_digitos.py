x = int(input('Digite um numero'))
i = 0
while x / 1 != 0: 
    i = i + (x % 10)
    x = x//10
print(i)
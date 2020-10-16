x = 0
y = x + 1
i = 0
while i <= 15:
    print(x)
    x += y
    print(y)
    y += x
    i += 2
    
x = 0
y = x + 1
for i in range(0,16):
    print(x)
    x += y
    print(y)
    y += x
    i += 2
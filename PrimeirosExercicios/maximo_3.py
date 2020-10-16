def maximo (x,y,z):
    if x > y and x > z: 
        return x
    elif z > y and z > x: 
        return z
    elif y > x and y > z: 
        return y
    else: 
        return x
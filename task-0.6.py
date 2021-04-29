def max(a,b,c): 
    if a > b or c: 
        return a
    elif b > a or c: 
        return b
    elif c > a or b:
        return c
    else: 
        return "No greater number"

print(max(10,5,9))


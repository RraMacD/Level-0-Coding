def max(a,b,c):
    if a > b or c:
        print(a)
    elif b > a or c:        
        print(b)
    elif c > a or b:
        print(c)
    else:
        print("No greater number")
max(10,5,9)


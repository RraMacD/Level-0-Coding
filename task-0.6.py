def max(a,b,c):
    if a > b and c:
        print(a)
    elif b > a and c:
        print(b)
    elif c > a and b:
        print(c)
    else:
        print("Invalid inputs")

max(4,9,1)

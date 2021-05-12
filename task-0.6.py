
def maximum_value(a,b,c):
    if b <= a >= c:
        return a
    elif a <= b >= c:
        return b
    elif a <= c >= b:
        return c
    else:
        return 'no greater value'
print(maximum_value(0,90,-7))






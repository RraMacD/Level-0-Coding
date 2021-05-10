def even_or_odd(a):
    if (a % 2) == 0:
        return "{0} is Even number".format(a)
    else:
        return "{0} is Odd number".format(a)
print(even_or_odd(3))

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
#A triangle has 3 sides: a,b,c
#Formula to calculate the area of a triangle is (s*(s-a)*(s-b)*(s-c)**0.5)
#s is the semi perimeter
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)**0.5)
print("Area of the triangle is %0.2f" %area)


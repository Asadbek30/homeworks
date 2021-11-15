import math
 
def circle(r):
    return math.pi * r**2
 
def rectangle(a, b):
    return a*b
 
def triangle(a, b, c):
    p = (a+b+c)/2
    return math.sqrt(p * (p-a) * (p-b) * (p-c))
 
choice = input("Circle(c), Rectangle(r) или Triangle(t): ")
if choice == 'c':
    rad = float(input("Radius: "))
    print("Square of circle: %.2f" % circle(rad))
elif choice == 'r':
    l = float(input("Length: "))
    w = float(input("Width: "))
    print("Square of rectangle: %.2f" % rectangle(l,w))
elif choice == 't':
    AB = float(input("1st side: "))
    BC = float(input("2nd side: "))
    CA = float(input("3rd side: "))
    print("Square of triangle: %.2f" % triangle(AB,BC,CA))
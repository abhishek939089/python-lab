#AREA OF A TRIANGLE......
a = int(input("Enter the value of first side of triangle:"))
b = int(input("Enter the value of second side of triangle:"))
c = int(input("Enter the value of third side of triangle:"))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(area)
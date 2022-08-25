
import cmath

a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))

d = (b ** 2) - (4 * a * c)
x = (-b + cmath.sqrt(d)) / (2 * a)
y = (-b - cmath.sqrt(d)) / (2 * a)
print('The solution are {0} and {1}'.format(x, y))

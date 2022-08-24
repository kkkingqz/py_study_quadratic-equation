import math

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

D = b ** 2 - 4 * a * c
print(D)
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
elif D == 0:
    x1 = (-b) / (2 * a)
    x2 = None
else:
    y1 = complex(-b, math.sqrt(-D))
    y2 = complex(-b, -math.sqrt(-D))
    x1 = y1 / (2 * a)
    x2 = y2 / (2 * a)

print(x1, '   ', x2)

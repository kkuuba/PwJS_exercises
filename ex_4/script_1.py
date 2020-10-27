import math

print("Enter a:")
a = float(input())
print("Enter b:")
b = float(input())
print("Enter c:")
c = float(input())

delta = b * b - 4 * a * c

if delta > 0:
    print("x1 = {}".format((-b + math.sqrt(delta))/2*a))
    print("x1 = {}".format((-b - math.sqrt(delta))/2*a))
elif delta == 0:
    print("x1 = {}".format(-b / 2*a))
else:
    print("This equation have not got solution in non complex domain")

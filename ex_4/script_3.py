import random

v_1 = []
v_2 = []

for x in range(0, 20):
    v_1.append(random.randint(-100, 100))
    v_2.append(random.randint(-100, 100))

print("Vector v1 = {}".format(v_1))
print("Vector v2 = {}".format(v_2))

result = 0
for a, b in zip(v_1, v_2):
    result = result + a * b

print("Result of vector product: {}".format(result))

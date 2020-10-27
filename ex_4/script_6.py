import random
import numpy as np

m = []

for x in range(64):
    row = []
    for k in range(64):
        row.append(random.randint(-100, 100))
    m.append(row)

matrix = np.array(m)
print("Det of matrix = {}".format(np.linalg.det(matrix)))

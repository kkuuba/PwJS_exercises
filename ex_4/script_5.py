import random
import numpy as np

m_1 = []
m_2 = []

for x in range(8):
    row_1 = []
    row_2 = []
    for k in range(8):
        row_1.append(random.randint(-100, 100))
        row_2.append(random.randint(-100, 100))
    m_1.append(row_1)
    m_2.append(row_2)

a = np.array(m_1)
b = np.array(m_2)
result = np.multiply(a, b)
print(result)

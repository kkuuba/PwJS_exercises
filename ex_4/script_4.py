import random

m_1 = []
m_2 = []

for x in range(128):
    row_1 = []
    row_2 = []
    for k in range(128):
        row_1.append(random.randint(-100, 100))
        row_2.append(random.randint(-100, 100))
    m_1.append(row_1)
    m_2.append(row_2)

result = []
for x in range(128):
    row = []
    for i, j in zip(m_1[x], m_2[x]):
        row.append(i + j)
    result.append(row)

for k in range(128):
    for g in range(128):
        if not m_1[k][g] + m_2[k][g] == result[k][g]:
            print("Error")

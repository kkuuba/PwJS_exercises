from threading import Thread
import random
import matplotlib.pyplot as plt

gauss_data = []
Y = list(range(40))
X = list(range(40))

[gauss_data.append(random.gauss(200, 50)) for i in range(10000)]


def calculate_data_set(data_set_id):
    data_set = gauss_data[1000 * data_set_id:1000 * data_set_id + 1000]
    for data in data_set:
        for num in range(40):
            if 10 * num <= data <= 10 * num + 10:
                Y[num] += 1


threads_tab = []
for set_id in range(10):
    threads_tab.append(Thread(target=calculate_data_set, args=(set_id,)))
    threads_tab[-1].start()
    threads_tab[-1].join()

color = ['yellow', 'greenyellow', 'lawngreen', 'limegreen', 'g']
color = color * 5

barlist = plt.bar([element * 10 for element in X], Y, color=color)

plt.show()

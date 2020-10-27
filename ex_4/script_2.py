import random

random_tab = []

for x in range(0, 50):
    random_tab.append(random.randint(1, 1000))


def sort_numbers(tab):
    for i in range(len(tab) - 1):
        for j in range(0, len(tab) - i - 1):

            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
    return tab


print("Random 50 numbers: ")
print(random_tab)
print("Random 50 numbers sorted: ")
print(sort_numbers(random_tab))

tab_build_in_sorted = sort_numbers(random_tab)
if tab_build_in_sorted == sort_numbers(random_tab):
    print("Correct sorting")
else:
    print("Incorrect sorting")

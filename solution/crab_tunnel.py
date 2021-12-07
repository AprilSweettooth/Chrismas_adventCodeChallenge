import csv
import numpy as np
import statistics
crabs = []
with open("data/data_day7.txt") as file:
    reader = csv.reader(file, delimiter=",")
    for row in reader:
        crabs.append(row)
crabs = crabs[0]
for i in range(len(crabs)):
    crabs[i] = int(crabs[i])
num = statistics.median(crabs)
num_2 = statistics.mean(crabs)

print(num_2)


def total(x, arr):
    sum = 0
    for i in range(len(arr)):
        n = abs(arr[i] - x)
        sum += n*(n+1)/2
    return sum


# list = []
# for i in range(2000):
#     list.append(total(i, crabs))

print(total(467, crabs))
print(total(466, crabs))

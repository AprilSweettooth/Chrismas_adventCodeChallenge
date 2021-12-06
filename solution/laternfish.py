import csv
import numpy as np
initial = []
with open("data/data_day6.txt") as file:
    reader = csv.reader(file, delimiter=",")
    for row in reader:
        initial.append(row)

# print(type(initial[0][0]))
starter = initial[0]
for i in range(len(starter)):
    starter[i] = int(starter[i])
# print(starter)

# for i in range(256):
#     for j in range(len(starter)):
#         if starter[j] == 0:
#             starter.append(8)
#             starter[j] = 6
#         else:
#             starter[j] -= 1

# for i in range(len(starter)):
#     if starter[i] == 0:
#         starter.remove(starter[i])


def birth_rate(arr):
    n = 0
    while(n < 128):
        for j in range(len(arr)):
            if arr[j] == 0:
                arr.append(8)
                arr[j] = 6
            else:
                arr[j] -= 1
        n += 1
        # print(len(arr))
    return [len(arr), arr]


# print(birth_rate(starter)[1])

cases = []
for i in range(9):
    cases.append(i)

halves = []
case_num = np.zeros([9, 9])
for i in range(9):
    halves.append(birth_rate([cases[i]])[0])
    for j in range(9):
        case_num[i][j] += birth_rate([cases[i]])[1].count(j)

# print(halves)
# print(case_num)

num = []
for i in range(9):
    num.append(starter.count(i))

# print(num)

second_cycle = []
for i in range(len(case_num)):
    second_cycle.append([halves[j] * case_num[i][j]
                        for j in range(len(halves))])
# second_cycle = [halves[j] * case_num[8][j] for j in range(len(halves))]
# print(second_cycle)

full_cycle = np.dot(num, second_cycle)
print(sum(full_cycle))

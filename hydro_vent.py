import csv
import numpy as np
data = []
with open("data_day5.txt") as file:
    reader = csv.reader(file, delimiter=" ")
    for row in reader:
        data.append(row)

for i in range(len(data)):
    data[i][0] = data[i][0].split(',')
    data[i][-1] = data[i][-1].split(',')

# print(data[0][0][1])

vent = np.zeros([1000, 1000], dtype=int)
# print(vent)

for i in range(len(data)):
    if data[i][0][0] == data[i][2][0]:
        x_co = int(data[i][0][0])
        num_1 = int(data[i][0][1])
        num_2 = int(data[i][2][1])
        Max = max(num_1, num_2)
        Min = min(num_1, num_2)
        for j in range(Max - Min + 1):
            vent[Min+j][x_co] += 1
    elif data[i][0][1] == data[i][2][1]:
        y_co = int(data[i][0][1])
        num_1 = int(data[i][0][0])
        num_2 = int(data[i][2][0])
        Max = max(num_1, num_2)
        Min = min(num_1, num_2)
        for j in range(Max - Min + 1):
            vent[y_co][Min+j] += 1
    elif data[i][0][0] == data[i][0][1] and data[i][2][0] == data[i][2][1]:
        num_1 = int(data[i][0][0])
        num_2 = int(data[i][2][0])
        Max = max(num_1, num_2)
        Min = min(num_1, num_2)
        for j in range(Max - Min + 1):
            vent[Min+j][Min+j] += 1
    elif (int(data[i][2][1])-int(data[i][0][1]))/(int(data[i][2][0])-int(data[i][0][0])) == -1:
        x_co_1 = int(data[i][0][0])
        x_co_2 = int(data[i][2][0])
        y_co_1 = int(data[i][0][1])
        y_co_2 = int(data[i][2][1])
        interval = abs(x_co_1-x_co_2)
        Min = min(x_co_2, x_co_1)
        Max = max(y_co_1, y_co_2)
        for j in range(interval + 1):
            vent[Max-j][Min+j] += 1
    elif (int(data[i][2][1])-int(data[i][0][1]))/(int(data[i][2][0])-int(data[i][0][0])) == 1:
        x_co_1 = int(data[i][0][0])
        x_co_2 = int(data[i][2][0])
        y_co_1 = int(data[i][0][1])
        y_co_2 = int(data[i][2][1])
        interval = abs(x_co_1-x_co_2)
        Min_x = min(x_co_2, x_co_1)
        Min_y = min(y_co_1, y_co_2)
        for j in range(interval + 1):
            vent[Min_y+j][Min_x+j] += 1
# print(vent)
count = 0
for i in range(1000):
    for j in range(1000):
        if vent[i][j] >= 2:
            count += 1
print(count)

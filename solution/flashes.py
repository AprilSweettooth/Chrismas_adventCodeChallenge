import csv
import numpy as np
flash = []
with open("data/data_day11.txt") as file:
    reader = csv.reader(file, delimiter=" ")
    for row in reader:
        flash.append(row)
for i in range(10):
    temp = flash[i][0]
    flash[i] = []
    for j in range(10):
        flash[i].append(int(temp[j]))
print(flash)


def increase_all(data):
    for i in range(10):
        for j in range(10):
            data[i][j] += 1


def GetElement(data, x, y):
    if x < 0 or x >= 10:
        return -1
    if y < 0 or y >= 10:
        return -1
    return data[x][y]


def flashes(data) -> int:
    flashing = 0
    for i in range(10):
        for j in range(10):
            if data[i][j] > 9:
                flashing += 1
                data[i][j] = -100000
                around = [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1],
                          [i, j+1], [i+1, j], [i+1, j+1], [i+1, j-1]]
                for one in around:
                    if GetElement(data, *one) != -1:
                        data[one[0]][one[1]] += 1
    return flashing


def removeNeg(data):
    for x in range(10):
        for y in range(10):
            if data[x][y] < 0:
                data[x][y] = 0


def atOnce(data):
    total = 0
    for x in range(10):
        for y in range(10):
            if data[x][y] == 0:
                total += 1
    return total == 100


totalFlash = 0
# for generation in range(100):
#     increase_all(flash)
#     flasher = flashes(flash)
#     while flasher > 0:
#         totalFlash += flasher
#         flasher = flashes(flash)
#     removeNeg(flash)
# print(totalFlash)

generation = 0
while True:
    generation += 1
    increase_all(flash)
    flasher = flashes(flash)
    while flasher > 0:
        totalFlash += flasher
        flasher = flashes(flash)
    removeNeg(flash)
    if atOnce(flash):
        print(generation)
        break

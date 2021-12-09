import csv
import numpy as np
maps = []
with open("data/data_day9.txt") as file:
    reader = csv.reader(file, delimiter=" ")
    for row in reader:
        maps.append(row)

for i in range(len(maps)):
    temp = []
    for j in range(100):
        temp.append(int(maps[i][0][j]))
    maps[i] = temp

boundary_hori = len(maps)
boundary_ver = len(maps[0])
low = []
count = 0
for i in range(boundary_hori-2):
    for j in range(boundary_ver-2):
        if maps[i+1][j+1] < maps[i+1][j+2] and maps[i+1][j+1] < maps[i+1][j] and maps[i+1][j+1] < maps[i][j+1] and maps[i+1][j+1] < maps[i+2][j+1]:
            low.append(maps[i+1][j+1])
    if maps[i+1][0] < maps[i][0] and maps[i+1][0] < maps[i+2][0] and maps[i+1][0] < maps[i+1][1]:
        low.append(maps[i+1][0])
    if maps[i+1][boundary_ver-1] < maps[i][boundary_ver-1] and maps[i+1][boundary_ver-1] < maps[i+2][boundary_ver-1] and maps[i+1][boundary_ver-1] < maps[i+1][boundary_ver-2]:
        low.append(maps[i+1][boundary_ver-1])
for j in range(boundary_ver-2):
    if maps[0][j+1] < maps[0][j+2] and maps[0][j+1] < maps[0][j] and maps[0][j+1] < maps[1][j+1]:
        low.append(maps[0][j+1])
    if maps[boundary_hori-1][j+1] < maps[boundary_hori-1][j+2] and maps[boundary_hori-1][j+1] < maps[boundary_hori-1][j] and maps[boundary_hori-1][j+1] < maps[boundary_hori-2][j+1]:
        low.append(maps[boundary_hori-1][j+1])
# print(len(low))
basin = np.zeros([100, 100])
for i in range(100):
    for j in range(100):
        if maps[i][j] == 9:
            count += 1
            basin[i][j] += 1
basins = []
for i in range(100):
    basins.append("".join(str(int(x)) for x in basin[i]))
for i in range(len(basins)):
    basins[i] = basins[i].replace("1", " ")
print(basins)
with open("data/output.txt", "w") as txt_file:
    for line in basins:
        txt_file.write(" ".join(str(line)) + "\n")

import csv

table = []
with open("data_day4.txt") as file:
    reader = csv.reader(file, delimiter=" ")
    for row in reader:
        table.append(row)

# print(table)

for x in table:
    index = table.index(x)
    x = ' '.join(x).split()
    table[index] = x
    # print(x)

# print(table)
position = table[0]
table.remove(position)
position = position[0]
position = position.split(",")
for i in range(len(position)):
    position[i] = int(position[i])
# print(type(int(position[0])))

# print(position)
# print(len(table))

tables = []
for i in range(100):
    tmpt = []
    for j in range(5):
        tmpt.append(table[1+j+6*i])
    tables.append(tmpt)

# print(tables[0])
# print(len(tables))


def check(M, result):
    sum = 0
    for i in range(5):
        for j in range(5):
            sum += int(M[j][i])
            if sum == -5:
                return True
    for x in range(5):
        result = all(elem == -1 for elem in M[x])
        if result == True:
            return True
    return False


# for x in range(len(position)):
#     cont = 0
#     for i in range(100):
#         for j in range(5):
#             for k in range(5):
#                 if position[x] == int(tables[i][j][k]):
#                     tables[i][j][k] = -1
#     # print(position[x+1])
#     result = False
#     index = 0
#     while(index < 100):
#         if check(tables[index], result) == True:
#             print(tables[index])
#             cont = 1
#             break
#         index += 1
#     if cont == 1:
#         break
# print(tables)

# add = 0
# for i in range(29):
#     add += position[i]
# print(add * position[30])

# 95 18 69. 85. 63.
# 16. 78 97. 10 41
# 53 98 73 87 19.
# 15. 35 94 57 82
# 48. 40. 14.  3. 38.

# 67,3,19,4,64,39,85,14,84,93,79,26,61,24,65,63,15,69,48,8,82,75,36,96,16,49,28,40,97,38,76,91,83,7,62,94,21,95,6,10,43,17,31,34,81,23,52,60,54,29,70,12,35,0,57,45,20,71,78,44,90,2,33,68,53,92,50,73,88,47,58,5,9,87,22,13,18,30,59,56,99,11,77,55,72,32,37,89,42,27,66,41,86,51,74,1,46,25,98,80

completion = 0
for x in range(len(position)):
    for i in range(len(tables)):
        for j in range(5):
            for k in range(5):
                if position[x] == int(tables[i][j][k]):
                    tables[i][j][k] = -1
    # print(position[x+1])
    result = False
    index = 0
    while(index < len(tables)):
        if check(tables[index], result) == True:
            completion += 1
            tables.remove(tables[index])
        index += 1
    if completion == 99:
        print(position[x])
        print(tables)
        break

import csv

# list = []
# with open("data_day3.txt") as file:
#     reader = csv.reader(file, delimiter=" ")
#     for row in reader:
#         list.append(row)

# print(type(list[0][0]))

txtfile = open('data/data_day3.txt')
L = []
for line in txtfile:
    L.append(str(line.rstrip()))
txtfile.close()


# most_common = []
# least_common = []

# for j in range(12):
#     digit = []
#     for i in range(len(L)):
#         x = [int(a) for a in str(L[i])]
#         digit.append(x[j])
#     if digit.count(0) > digit.count(1):
#         most_common.append(0)
#         least_common.append(1)
#     else:
#         most_common.append(1)
#         least_common.append(0)


# most_common = [str(i) for i in most_common]
# most_common = int(("".join(most_common)))

# print(most_common)
# print(least_common)

oxygen = L
carbon = L


def filter(x, lead, position):
    M = []
    for i in range(len(x)):
        temp = x[i]
        if int(temp[position]) == int(lead):
            M.append(temp)
    return M


for j in range(12):
    digit = []
    for i in range(len(oxygen)):
        x = [int(a) for a in str(oxygen[i])]
        digit.append(x[j])
    if digit.count(0) > digit.count(1):
        oxygen = filter(oxygen, 0, j)
    else:
        oxygen = filter(oxygen, 1, j)

for j in range(9):
    digit = []
    for i in range(len(carbon)):
        x = [int(a) for a in str(carbon[i])]
        digit.append(x[j])
    if digit.count(0) > digit.count(1):
        carbon = filter(carbon, 1, j)
    else:
        carbon = filter(carbon, 0, j)

print(oxygen)
print(carbon)

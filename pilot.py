txtfile = open('data_day2.txt')
L = []
for line in txtfile:
    L.append(str(line.rstrip()))
txtfile.close()

horizontal = 0
depth = 0

# for i in range(len(L)):
#     pilot = L[i].split()
#     if pilot[0] == "up":
#         depth -= int(pilot[1])
#     elif pilot[0] == "down":
#         depth += int(pilot[1])
#     elif pilot[0] == "forward":
#         horizontal += int(pilot[1])

# product = horizontal * depth
# print(product)

position = [0, 0, 0]
for i in range(len(L)):
    pilot = L[i].split()
    if pilot[0] == "up":
        position[1] -= int(pilot[1])
    elif pilot[0] == "down":
        position[1] += int(pilot[1])
    elif pilot[0] == "forward":
        position[0] += int(pilot[1])
        position[2] += int(pilot[1]) * position[1]

product = position[0] * position[2]
print(product)

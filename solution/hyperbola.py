
# not finished youtube solution

from os import stat


def UpdateState(x, y, dx, dy):
    x += dx
    y += dy

    if dx < 0:
        dx += 1
    elif dx > 0:
        dx -= 1

    return [[x, y], [dx, dy]]


def HasHit(position, target):
    return (position[0] >= target[0][0] and position[0] <= target[0][1] and position[1] <= target[1][0] and position[1] >= target[1][1])


target = []
with open("data/data_day17.txt") as file:
    for coordinate in file.readline().strip('\n').split(":")[1].split(","):
        target.append([int(x) for x in coordinate.split('=')[1].split('..')])
    target[1] = [target[1][1], target[1][0]]
# print(target)
maxHeight = 0
for x in range(300):
    for y in range(300):
        status = [[0, 0], [x, y]]
        originalVelocity = status[1].copy()
        height = 0
        found = False
        while found == False and status[0][0] <= target[0][1] and status[0][1] >= target[1][1]:
            status = UpdateState(*status[0], *status[1])
            height = max(height, status[0][1])
            if HasHit(status[0], target):
                found = True
        if found == True:
            maxHeight = max(maxHeight, height)
print(maxHeight)

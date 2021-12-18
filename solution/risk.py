
# not finished youtube solution

import copy
import sys

# from typing import final

with open("data/data_day15.txt") as file:
    data = [[int(character) for character in line.strip('\n')]
            for line in file]
    for line in data:
        for index in range(4*len(line)):
            newValue = line[index] + 1
            line.append(newValue if newValue < 10 else 1)
        for index in range(4*len(data)):
            new = [x+1 for x in data[index]]
            for index in range(len(new)):
                if new[index] > 9:
                    new[index] -= 9
                data.append(new)


def GetElementValue(data, x, y):
    if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):
        return -1
    return data[x][y]


#           risk open               close  end
end = [len(data[0])-1, len(data)-1]
# [[0, [[0, 0]],  [],  [len(data[0])-1, len(data)-1]]]
allPaths = [[0, [[0, 0]],  []]]
bestPaths = [[sys.maxsize] * len(data[0]) for each in range(len(data))]

while len(allPaths) > 0:
    allPaths.sort(key=lambda x: -x[0])
    path = allPaths.pop()
    # if path[3] in path[2]:
    #     print(path)
    if end == path[1][0]:
        print(path)
    else:
        openlist = path[1].copy()
        path[1] = []
        for next in openlist:
            newPath = copy.deepcopy(path)
            # newPath[2].append(next)
            neighbors = [[next[0]-1, next[1]], [next[0]+1, next[1]],
                         [next[0], next[1]-1], [next[0], next[1]+1]]
            for neighbor in neighbors:
                value = GetElementValue(data, *neighbor)
                if value >= 0 and neighbor not in newPath[2]:
                    if newPath[0] + value < bestPaths[neighbor[0]][neighbor[1]]:
                        bestPaths[neighbor[0]][neighbor[1]
                                               ] = newPath[0] + value
                        finalPath = copy.deepcopy(newPath)
                        finalPath[0] += value
                        finalPath[1].append(neighbor)
                        allPaths.append(finalPath)

print(bestPaths[-1][-1])

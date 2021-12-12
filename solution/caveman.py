
# solutions from prof on youtube

data = dict()
with open("data/data_day12.txt") as file:
    line = file.readline()
    while line:
        nodes = [x for x in line.strip('\n').split('-')]
        if data.get(nodes[0], "FirstTime") == "FirstTime":
            data[nodes[0]] = []
        if data.get(nodes[1], "FirstTime") == "FirstTime":
            data[nodes[1]] = []
        data[nodes[1]].append(nodes[0])
        data[nodes[0]].append(nodes[1])
        line = file.readline()
# print(data)


# def Recursion():
#     if path[-1] != 'end':
#         for nextMove in data[path[-1]]:
#             if(nextMove.upper() == nextMove) or (nextMove not in path):
#                 path.append(nextMove)
#                 Recursion()
#                 path.pop()

#     else:
#         solutions.append(path.copy())

def Recursion():
    global solutions
    if path[-1] != 'end':
        for nextMove in data[path[-1]]:
            if (nextMove != 'start') and (UptoTwo(path)) and \
                    ((nextMove.upper() == nextMove) or (path.count(nextMove) < 2)):
                path.append(nextMove)
                Recursion()
                path.pop()

    elif UptoTwo(path):
        solutions += 1


def UptoTwo(s):
    justlower = [x for x in s if x.upper() != x]
    return len(justlower) - len(set(justlower)) <= 1


path = ["start"]
# solutions = []
solutions = 0
Recursion()
# for s in solutions:
#     print(s)
print(solutions)

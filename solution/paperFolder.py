
# solutions from prof on youtube

data = set()
folds = []
with open("data/data_day13.txt") as file:
    line = file.readline()
    while line != '\n':
        line = tuple([int(x) for x in line.strip('\n').split(',')])
        data.add(line)
        line = file.readline()
    line = file.readline()
    while line:
        line = line.strip('\n').split(' ')[2].split('=')
        line[1] = int(line[1])
        folds.append(line)
        line = file.readline()


def fold_x(data, value):
    result = set()
    for point in data:
        if point[0] > value:
            p = (value-(point[0]-value), point[1])
            result.add(p)
        else:
            p = (point[0], point[1])
            result.add(p)
    return result


def fold_y(data, value):
    result = set()
    for point in data:
        if point[1] > value:
            p = (point[0], value-(point[1]-value))
            result.add(p)
        else:
            p = (point[0], point[1])
            result.add(p)
    return result


for fold in folds:
    if fold[0] == 'x':
        data = fold_x(data, fold[1])
    else:
        data = fold_y(data, fold[1])
    # print(len(data))
# print(data)

array = [[' '] * 40 for i in range(25)]
for point in data:
    array[point[1]][point[0]] = '#'
for line in array:
    s = ""
    for char in line:
        s += char
    print(s)

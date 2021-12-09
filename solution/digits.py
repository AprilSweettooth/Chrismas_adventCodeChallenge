import csv
import numpy as np
digits = []
with open("data/data_day8.txt") as file:
    reader = csv.reader(file, delimiter="|")
    for row in reader:
        digits.append(row)

digit = []
for i in range(len(digits)):
    output = ''.join(digits[i]).split(" ")
    digit.append(output[-4:])

# print(digit)


# def len_dig(x, num, one, four, seven, eight):
#     for i in range(len(x)):
#         if len(x[i]) == one:
#             num += 1
#         elif len(x[i]) == four:
#             num += 1
#         elif len(x[i]) == seven:
#             num += 1
#         elif len(x[i]) == eight:
#             num += 1
#     return num


# count = 0

# for j in range(len(digit)):
#     count += len_dig(digit[j], 0, 2, 4, 3, 7)
# print(count)

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


def get_num(x, leng):
    for m in x:
        if len(m) == leng:
            return m


def get_top(x, y):
    right_side = []
    top = []
    if len(x) == 3:
        right_side.append(y[0])
        right_side.append(y[1])
        for i in range(3):
            if x[i] != y[0] and x[i] != y[1]:
                top.append(x[i])
    else:
        right_side.append(x[0])
        right_side.append(x[1])
        for i in range(3):
            if y[i] != x[0] and y[i] != x[1]:
                top.append(y[i])
    get_top_right = []
    get_top_right.append(top)
    get_top_right.append(right_side)
    return get_top_right


def get_L(x, y):
    L = []
    if len(x) == 4:
        for i in range(4):
            if x[i] != y[0] and x[i] != y[1]:
                L.append(x[i])
    else:
        for i in range(4):
            if y[i] != x[0] and y[i] != x[1]:
                L.append(y[i])
    return L


def get_bottom(x, y):
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    B = []
    if len(x) == 4:
        for i in range(7):
            if letter[i] != x[0] and letter[i] != x[1] and letter[i] != x[2] and letter[i] != x[3] and letter[i] != y[0] and letter[i] != y[1] and letter[i] != y[2]:
                B.append(letter[i])
    return B


list = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd',
        'cdfgeb', 'eafb', 'cagedb', 'ab', 'cdfeb', 'fcadb', 'cdfeb', 'cdbaf']


def assign_number(list, num):
    if num == 1:
        for i in range(list):
            if len(list[i]) == 2:
                return i
    elif num == 8:
        for i in range(list):
            if len(list[i]) == 7:
                return i
    elif num == 4:
        for i in range(list):
            if len(list[i]) == 4:
                return i
    elif num == 7:
        for i in range(list):
            if len(list[i]) == 3:
                return i
    elif num == 9:
        for i in range(list):
            for j in range(list):
                if len(list[j]) == 4 and len(list[i]) == 2:
                    get_L = get_L(list[j], list[i])
                if len(list[j]) == 3 and len(list[i]) == 2:
                    get_top = get_top(list[j], list[i])
        for i in range(list):
            if len(list[i]) == 6:
                ver = [item for item in letter if item not in list[i]]
                if ver[0] not in get_L and ver[0] not in get_top[1]:
                    return i
    elif num == 0:
        pair = []
        for i in range(list):
            if len(list[i]) == 3:
                pair.append(list[i])
            elif len(list) == 4:
                pair.append(list[i])
        for i in range(list):
            if len(list[i]) == 6 and get_bottom()[0] not in list[i] and get_bottom()[1] not in list[i]:
                return i
    elif num == 6:
        pair = []
        for i in range(list):
            if len(list[i]) == 3:
                pair.append(list[i])
            elif len(list) == 4:
                pair.append(list[i])
        for i in range(list):
            if len(list[i]) == 6 and ones[0] not in list[i] and ones[1] not in list[i]:
                return i
    elif num == 5:
        pair = []
        for i in range(list):
            if len(list[i]) == 3:
                pair.append(list[i])
            elif len(list) == 4:
                pair.append(list[i])
        for i in range(list):
            if len(list[i]) == 6 and ones[0] not in list[i] and ones[1] not in list[i]:
                return i
    elif num == 3:
        pair = []
        for i in range(list):
            if len(list[i]) == 3:
                pair.append(list[i])
            elif len(list) == 4:
                pair.append(list[i])
        for i in range(list):
            if len(list[i]) == 5 and ones[0] in list[i] and ones[1] in list[i]:
                return i
    elif num == 2:
        pair = []
        for i in range(list):
            if len(list[i]) == 3:
                pair.append(list[i])
            elif len(list) == 4:
                pair.append(list[i])
        for i in range(list):
            if len(list[i]) == 5 and ones[0] in list[i] and ones[1] in list[i]:
                return i


sum = 0
for i in range(len(digits)):
    digits[i].remove(digits[i][-5])
    digits[i].append([])
    for j in range(10):
        digit[i][assign_number(digits[i], j)] = j

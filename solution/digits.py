# import csv
# import numpy as np
# digits = []
# with open("data/data_day8.txt") as file:
#     reader = csv.reader(file, delimiter="|")
#     for row in reader:
#         digits.append(row)

# digit = []
# for i in range(len(digits)):
#     output = ''.join(digits[i]).split(" ")
#     digit.append(output[-4:])

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

# letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


# def get_num(x, leng):
#     for m in x:
#         if len(m) == leng:
#             return m


# def get_top(x, y):
#     right_side = []
#     top = []
#     if len(x) == 3:
#         right_side.append(y[0])
#         right_side.append(y[1])
#         for i in range(3):
#             if x[i] != y[0] and x[i] != y[1]:
#                 top.append(x[i])
#     else:
#         right_side.append(x[0])
#         right_side.append(x[1])
#         for i in range(3):
#             if y[i] != x[0] and y[i] != x[1]:
#                 top.append(y[i])
#     get_top_right = []
#     get_top_right.append(top)
#     get_top_right.append(right_side)
#     return get_top_right


# def get_L(x, y):
#     L = []
#     if len(x) == 4:
#         for i in range(4):
#             if x[i] != y[0] and x[i] != y[1]:
#                 L.append(x[i])
#     else:
#         for i in range(4):
#             if y[i] != x[0] and y[i] != x[1]:
#                 L.append(y[i])
#     return L


# def get_bottom(x, y):
#     letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     B = []
#     if len(x) == 4:
#         for i in range(7):
#             if letter[i] != x[0] and letter[i] != x[1] and letter[i] != x[2] and letter[i] != x[3] and letter[i] != y[0] and letter[i] != y[1] and letter[i] != y[2]:
#                 B.append(letter[i])
#     return B


# list = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd',
#         'cdfgeb', 'eafb', 'cagedb', 'ab', 'cdfeb', 'fcadb', 'cdfeb', 'cdbaf']


# def assign_number(list, num):
#     if num == 1:
#         for i in range(list):
#             if len(list[i]) == 2:
#                 return i
#     elif num == 8:
#         for i in range(list):
#             if len(list[i]) == 7:
#                 return i
#     elif num == 4:
#         for i in range(list):
#             if len(list[i]) == 4:
#                 return i
#     elif num == 7:
#         for i in range(list):
#             if len(list[i]) == 3:
#                 return i
#     elif num == 9:
#         for i in range(list):
#             for j in range(list):
#                 if len(list[j]) == 4 and len(list[i]) == 2:
#                     get_L = get_L(list[j], list[i])
#                 if len(list[j]) == 3 and len(list[i]) == 2:
#                     get_top = get_top(list[j], list[i])
#         for i in range(list):
#             if len(list[i]) == 6:
#                 ver = [item for item in letter if item not in list[i]]
#                 if ver[0] not in get_L and ver[0] not in get_top[1]:
#                     return i
#     elif num == 0:
#         pair = []
#         for i in range(list):
#             if len(list[i]) == 3:
#                 pair.append(list[i])
#             elif len(list) == 4:
#                 pair.append(list[i])
#         for i in range(list):
#             if len(list[i]) == 6 and get_bottom()[0] not in list[i] and get_bottom()[1] not in list[i]:
#                 return i
#     elif num == 6:
#         pair = []
#         for i in range(list):
#             if len(list[i]) == 3:
#                 pair.append(list[i])
#             elif len(list) == 4:
#                 pair.append(list[i])
#         for i in range(list):
#             if len(list[i]) == 6 and ones[0] not in list[i] and ones[1] not in list[i]:
#                 return i
#     elif num == 5:
#         pair = []
#         for i in range(list):
#             if len(list[i]) == 3:
#                 pair.append(list[i])
#             elif len(list) == 4:
#                 pair.append(list[i])
#         for i in range(list):
#             if len(list[i]) == 6 and ones[0] not in list[i] and ones[1] not in list[i]:
#                 return i
#     elif num == 3:
#         pair = []
#         for i in range(list):
#             if len(list[i]) == 3:
#                 pair.append(list[i])
#             elif len(list) == 4:
#                 pair.append(list[i])
#         for i in range(list):
#             if len(list[i]) == 5 and ones[0] in list[i] and ones[1] in list[i]:
#                 return i
#     elif num == 2:
#         pair = []
#         for i in range(list):
#             if len(list[i]) == 3:
#                 pair.append(list[i])
#             elif len(list) == 4:
#                 pair.append(list[i])
#         for i in range(list):
#             if len(list[i]) == 5 and ones[0] in list[i] and ones[1] in list[i]:
#                 return i


# sum = 0
# for i in range(len(digits)):
#     digits[i].remove(digits[i][-5])
#     digits[i].append([])
#     for j in range(10):
#         digit[i][assign_number(digits[i], j)] = j

# solution from jonathanpaulson
import sys
import itertools
from collections import defaultdict, Counter

# 0: abcefg (6)
# 6: abdefg (6)
# 9: abcdfg (6)

# 2: acdeg (5)
# 3: acdfg (5)
# 5: abdfg (5)

# 1: cf (2)
# 4: bcdf (4)
# 7: acf (3)
# 8: abcdefg (7)

digits = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg',
}


def find_perm_slow(before):
    for perm in itertools.permutations(list(range(8))):
        ok = True
        D = {}
        for i in range(8):
            D[chr(ord('a')+i)] = chr(ord('a')+perm[i])
        for w in before:
            w_perm = ''
            for c in w:
                w_perm += D[c]
            w_perm = ''.join(sorted(w_perm))

            if w_perm not in digits.values():
                ok = False
        if ok:
            return D


def find_perm(before):
    A = {}
    for w in before:
        if len(w) == 2:  # 1
            cf = w
    assert len(cf) == 2, cf
    for w in before:
        if len(w) == 6 and (cf[0] in w) != (cf[1] in w):  # 6
            if cf[0] in w:
                A[cf[0]] = 'f'
                A[cf[1]] = 'c'
            else:
                A[cf[1]] = 'f'
                A[cf[0]] = 'c'
    assert len(A) == 2, f'A={A} cf={cf} {before}'
    for w in before:
        if len(w) == 3:  # 7
            for c in w:
                if c not in cf:
                    A[c] = 'a'
    assert len(A) == 3, A
    for w in before:
        if len(w) == 4:  # 4
            bd = ''
            for c in w:
                if c not in cf:
                    bd += c
    assert len(bd) == 2, bd
    # 0 is length-6 and missing one of b/d. B is present; D is missing.
    # 9 is length-6 missing one of e/g. G is present; E is missing.
    for w in before:
        if len(w) == 6 and (bd[0] in w) != (bd[1] in w):  # 0
            if bd[0] in w:
                A[bd[0]] = 'b'
                A[bd[1]] = 'd'
            else:
                A[bd[1]] = 'b'
                A[bd[0]] = 'd'
    assert len(A) == 5, A
    eg = ''
    for c in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        if c not in A:
            eg += c
    assert len(eg) == 2, eg
    for w in before:
        if len(w) == 6 and (eg[0] in w) != (eg[1] in w):  # 9
            if eg[0] in w:
                A[eg[0]] = 'g'
                A[eg[1]] = 'e'
            else:
                A[eg[1]] = 'g'
                A[eg[0]] = 'e'
    assert len(A) == 7, A
    return A


p1 = 0
ans = 0
infile = sys.argv[1] if len(sys.argv) > 1 else 'data/data_day8.txt'
for line in open(infile):
    before, after = line.split('|')
    before = before.split()
    after = after.split()

    D = find_perm(before)
    ret = ''
    for w in after:
        w_perm = ''
        for c in w:
            w_perm += D[c]
        w_perm = ''.join(sorted(w_perm))
        d = [k for k, v in digits.items() if v == w_perm]
        assert len(d) == 1
        if d[0] in [1, 4, 7, 8]:
            p1 += 1
        ret += str(d[0])
    ans += int(ret)
print(p1)
print(ans)

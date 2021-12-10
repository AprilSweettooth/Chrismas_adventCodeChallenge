# import csv
# import numpy as np
# syn = []
# with open("data/data_day10.txt") as file:
#     reader = csv.reader(file, delimiter=" ")
#     for row in reader:
#         syn.append(row)

# list = ['[', ']', '{', '}', '(', ')', '<', '>']
# prices = [3, 57, 1197, 25137]
# price = 0
# for i in range(len(syn)):
#     square_left = 0
#     square_right = 0
#     bracket_left = 0
#     bracket_right = 0
#     paren_left = 0
#     paren_right = 0
#     bra = 0
#     ket = 0
#     for j in range(len(syn[i][0])):
#         if syn[i][0][j] == '[':
#             square_left += 1
#         elif syn[i][0][j] == ']':
#             square_right += 1
#         elif syn[i][0][j] == '(':
#             bracket_left += 1
#         elif syn[i][0][j] == ')':
#             bracket_right += 1
#         elif syn[i][0][j] == '{':
#             paren_left += 1
#         elif syn[i][0][j] == '}':
#             paren_right += 1
#         elif syn[i][0][j] == '<':
#             bra += 1
#         elif syn[i][0][j] == '>':
#             ket += 1
#     square_diff = square_left-square_right
#     bracket_diff = bracket_left-bracket_right
#     paren_diff = paren_left-paren_right
#     brak_diff = bra-ket
#     if square_diff >= 0 and bracket_diff >= 0 and paren_diff >= 0 and brak_diff >= 0:
#         pass
#     elif square_diff <= 0 and bracket_diff <= 0 and paren_diff <= 0 and brak_diff <= 0:
#         pass
#     else:
#         list = [square_diff, bracket_diff, paren_diff, brak_diff]
#         neg = [x for x in list if x < 0]
#         pos = [x for x in list if x > 0]
#     if square_diff in neg:
#         index = syn[i][0].index()
#         index = index*57

# solution from jonathanpaulson
import sys
import itertools
from collections import defaultdict, Counter, deque

SCORES = []
ans = 0
infile = sys.argv[1] if len(sys.argv) > 1 else 'data/data_day10.txt'
for line in open(infile):
    bad = False
    S = deque()
    for c in line.strip():
        if c in ['(', '[', '{', '<']:
            S.append(c)
        elif c == ')':
            if S[-1] != '(':
                ans += 3
                bad = True
                break
            else:
                S.pop()
        elif c == ']':
            if S[-1] != '[':
                ans += 57
                bad = True
                break
            else:
                S.pop()
        elif c == '}':
            if S[-1] != '{':
                ans += 1197
                bad = True
                break
            else:
                S.pop()
        elif c == '>':
            if S[-1] != '<':
                ans += 25137
                bad = True
                break
            else:
                S.pop()
    if not bad:
        score = 0
        P = {'(': 1, '[': 2, '{': 3, '<': 4}
        for c in reversed(S):
            score = score*5 + P[c]
        SCORES.append(score)
print(ans)
SCORES.sort()
print(SCORES[len(SCORES)//2])

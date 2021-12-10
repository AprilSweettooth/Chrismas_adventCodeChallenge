# import csv
# import numpy as np
# maps = []
# with open("data/data_day9.txt") as file:
#     reader = csv.reader(file, delimiter=" ")
#     for row in reader:
#         maps.append(row)

# for i in range(len(maps)):
#     temp = []
#     for j in range(100):
#         temp.append(int(maps[i][0][j]))
#     maps[i] = temp

# boundary_hori = len(maps)
# boundary_ver = len(maps[0])
# low = []
# count = 0
# for i in range(boundary_hori-2):
#     for j in range(boundary_ver-2):
#         if maps[i+1][j+1] < maps[i+1][j+2] and maps[i+1][j+1] < maps[i+1][j] and maps[i+1][j+1] < maps[i][j+1] and maps[i+1][j+1] < maps[i+2][j+1]:
#             low.append(maps[i+1][j+1])
#     if maps[i+1][0] < maps[i][0] and maps[i+1][0] < maps[i+2][0] and maps[i+1][0] < maps[i+1][1]:
#         low.append(maps[i+1][0])
#     if maps[i+1][boundary_ver-1] < maps[i][boundary_ver-1] and maps[i+1][boundary_ver-1] < maps[i+2][boundary_ver-1] and maps[i+1][boundary_ver-1] < maps[i+1][boundary_ver-2]:
#         low.append(maps[i+1][boundary_ver-1])
# for j in range(boundary_ver-2):
#     if maps[0][j+1] < maps[0][j+2] and maps[0][j+1] < maps[0][j] and maps[0][j+1] < maps[1][j+1]:
#         low.append(maps[0][j+1])
#     if maps[boundary_hori-1][j+1] < maps[boundary_hori-1][j+2] and maps[boundary_hori-1][j+1] < maps[boundary_hori-1][j] and maps[boundary_hori-1][j+1] < maps[boundary_hori-2][j+1]:
#         low.append(maps[boundary_hori-1][j+1])
# # print(len(low))
# basin = np.zeros([100, 100])
# for i in range(100):
#     for j in range(100):
#         if maps[i][j] == 9:
#             count += 1
#             basin[i][j] += 1
# basins = []
# for i in range(100):
#     basins.append("".join(str(int(x)) for x in basin[i]))
# for i in range(len(basins)):
#     basins[i] = basins[i].replace("1", " ")
# print(basins)
# with open("data/output.txt", "w") as txt_file:
#     for line in basins:
#         txt_file.write(" ".join(str(line)) + "\n")


# solution from jonathanpaulson
import sys
import itertools
from collections import defaultdict, Counter, deque

infile = sys.argv[1] if len(sys.argv) > 1 else 'data/data_day9.txt'
G = []
for line in open(infile):
    G.append([int(x) for x in list(line.strip())])
R = len(G)
C = len(G[0])
DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]
ans = 0
for r in range(R):
    assert len(G[r]) == C
    for c in range(C):
        ok = True
        for d in range(4):
            rr = r+DR[d]
            cc = c+DC[d]
            if 0 <= rr < R and 0 <= cc < C and G[rr][cc] <= G[r][c]:
                ok = False
        if ok:
            ans += G[r][c]+1
print(ans)

S = []
SEEN = set()
for r in range(R):
    for c in range(C):
        if (r, c) not in SEEN and G[r][c] != 9:
            size = 0
            Q = deque()
            Q.append((r, c))
            while Q:
                (r, c) = Q.popleft()
                if (r, c) in SEEN:
                    continue
                SEEN.add((r, c))
                size += 1
                for d in range(4):
                    rr = r+DR[d]
                    cc = c+DC[d]
                    if 0 <= rr < R and 0 <= cc < C and G[rr][cc] != 9:
                        Q.append((rr, cc))
            S.append(size)
S.sort()
print(S[-1]*S[-2]*S[-3])

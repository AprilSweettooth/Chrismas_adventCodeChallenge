def sum(x):
    count = 0
    for i in range(len(x)-1):
        if x[i] < x[i+1]:
            count += 1
    return count


txtfile = open('data/data_day1.txt')
L = []
for line in txtfile:
    L.append(int(line.rstrip()))
txtfile.close()
print(sum(L))

M = []
for i in range(len(L)-2):
    count = 0
    num = L[i] + L[i+1] + L[i+2]
    M.append(num)

print(sum(M))

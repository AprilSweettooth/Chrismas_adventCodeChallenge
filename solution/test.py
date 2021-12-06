def check(M):
    result = False
    sum = 0
    for i in range(5):
        for j in range(5):
            sum += int(M[j][i])
            if sum == -5:
                return True
    for x in range(5):
        result = all(elem == -1 for elem in M[i])
        if result == True:
            return True
    return False


x = [[-1, 1, 1, 2, 1], [-1, 1, -1, -1, -1], [
    -1, 3, 3, 4, 1], [-1, 4, 4, 5, 1], [-1, 5, 5, 5, 6]]
print(check(x))

import sys
input = sys.stdin.readline
p = 1000000007

n = int(input())

def matmul(a, b):
    res = [[0 for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += a[i][k] * b[k][j]
            res[i][j] = res[i][j] % p
    return res

def power(a, n):
    if n == 1:
        return a
    tmp = power(a, n//2)
    if n%2 == 0:
        return matmul(tmp, tmp)
    else:
        return matmul(matmul(tmp, tmp), a)
matrix = [[1, 1], [1, 0]]
print(power(matrix, n)[0][1])
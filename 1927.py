import sys

def solution(x, y, n):
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                solution(x, y, n//2)
                solution(x, y + n // 2, n//2)
                solution(x + n // 2, y, n//2)
                solution(x + n // 2, y + n // 2, n//2)
                return
    if color == 0:
        count[0] += 1
    if color == 1:
        count[1] += 1

n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
count = [0, 0]
solution(0, 0, n)
print(count[0])
print(count[1])
import sys

input = sys.stdin.readline
li = input().rstrip('\n')
stack = []
ans = ''
for i in li:
    if i.isupper():
        ans += i
    else:
        if i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(i)
        else:
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(i)
while stack:
    ans += stack.pop()
print(ans)from collections import deque

n, m = map(int, input().split(' '))
g = []
visited = [[[False] * m for _ in range(n)] for _ in range(2)]

for _ in range(n):
    g.append(list(map(int, input())))

def bfs():
    q = deque()
    cnt = 0
    q.append((0, 0, 0, 0))
    move = [[0, -1], [0, 1], [-1, 0], [1, 0]]

    while q:
        loca, x, y, cnt = q.popleft()

        if x == n - 1 and y == m - 1:
            return cnt + 1

        for i in range(4):
            nx, ny = x + move[i][0], y + move[i][1]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if g[nx][ny] == 0 and not visited[loca][nx][ny]:
                visited[loca][nx][ny] = True
                if (loca == 1):
                    q.append((1, nx, ny, cnt + 1))
                else:
                    q.append((0, nx, ny, cnt + 1))

            elif g[nx][ny] == 1 and loca == 0 and not visited[loca][nx][ny]:
                visited[loca][nx][ny] = True
                q.append((1, nx, ny, cnt + 1))
    return -1


print(bfs())
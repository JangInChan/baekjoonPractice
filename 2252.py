from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
indgree = [0 for _ in range(n + 1)]
answer = []
q = deque()

for i in range(m):
    small, big = map(int, input().split())
    indgree[big] += 1
    graph[small].append(big)

for i in range(1, n + 1):
    if indgree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    answer.append(now)

    for i in graph[now]:
        indgree[i] -= 1
        if indgree[i] == 0:
            q.append(i)

print(*answer)
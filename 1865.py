import sys
from collections import defaultdict

tc = int(input())
answer = []
while tc:
    n, m, w = map(int, input().split())
    edges = defaultdict(lambda: float("inf"))

    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        edges[(a, b)] = min(edges[(a, b)], c)
        edges[(b, a)] = min(edges[(b, a)], c)

    for _ in range(w):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        edges[(a, b)] = min(edges[(a, b)], -c)

    def get_answer(start):
        INF = 1e9 #float('inf')사용 X
        dis = [INF] * (n + 1)
        dis[start] = 0

        for i in range(n):
            for (a, b), c in edges.items():
                if dis[b] > dis[a] + c:
                    dis[b] = dis[a] + c
                    if i == n - 1:
                        return "YES"
        return "NO"

    print(get_answer(1))
    tc -= 1

print(*answer, sep="\n")
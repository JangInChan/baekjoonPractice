import sys
input = sys.stdin.readline

n, target_mem = map(int, input().split())
mem = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))

max_cost = sum(cost)
dp = [[0] * (n+1) for _ in range(max_cost + 1)]

found_min_cost = False
min_cost = 100 * 10000000

for i in range(max_cost + 1):
    if found_min_cost:
        break
    
    for j in range(1, n + 1):

        if i >= cost[j]:
            dp[i][j] = dp[i - cost[j]][j-1] + mem[j]
        
        dp[i][j] = max(dp[i][j], dp[i][j-1])
        
        if dp[i][j] >= target_mem:
            found_min_cost = True
            min_cost = i
            break

print(min_cost)
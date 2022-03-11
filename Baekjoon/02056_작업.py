# Gold 4

n = int(input())
dp = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    temp = list(map(int, input().split()))

    dp[i] = temp[0]

    for a in temp[2:]:
        graph[i].append(a)

for i in range(1, n + 1):
    tmp = 0

    for j in graph[i]:
        tmp = max(tmp, dp[j])

    dp[i] += tmp

print(max(dp))
# https://www.acmicpc.net/problem/2606
# Sliver 3

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

network = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    network[a][b] = network[b][a] = 1

visited = [0] * (n + 1)
virus = []

def dfs(v):
    visited[v] = 1
    for i in range(1, n + 1):
        if network[v][i] == 1 and visited[i] == 0:
            virus.append(i)
            dfs(i)
    return len(virus)

print(dfs(1))
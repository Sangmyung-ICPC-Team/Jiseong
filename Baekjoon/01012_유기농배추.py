# Silver 2

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(arr, n, m, x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    arr[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and 0 <= ny:
            if nx < n and ny < m:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    dfs(arr, n, m, nx, ny)

t = int(input())
answer = []
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        a, b = map(int, input().split())
        arr[b][a] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                dfs(arr, n, m, i, j)
                cnt += 1

    answer.append(cnt)

for a in answer:
    print(a)
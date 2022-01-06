# https://www.acmicpc.net/problem/2667
# Sliver 1

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    global cnt

    graph [x][y] = 0
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and 0 <= ny:
            if nx < n and ny < n:
                if graph[nx][ny] == 1:
                    dfs(nx, ny)

cnt = 0
res = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)
            res.append(cnt)
            cnt = 0

res.sort()
print(len(res))
for r in res:
    print(r)
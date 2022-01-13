# https://www.acmicpc.net/problem/1058
# Sliver 2

INF = 10000000

# 입력
n = int(input())
s = []
for _ in range(n):
    s.append(list(input().strip()))

# 2차원 리스트, 모든 값을 무한으로 초기화
graph = [[INF] * (n) for _ in range(n)]

# 자기 자신 0으로 
for a in range(n):
    for b in range(n):
        if a == b:
            graph[a][b] = 0

# 플로이드 와샬
for c in range(n):
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            if s[a][b] == "Y" or (s[a][c] == "Y" and s[c][b] == "Y"):
                graph[a][b] = 1

# 카운트
ans = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if graph[i][j] == 1:
            cnt += 1
    ans = max(ans, cnt)

#출력
print(ans)



















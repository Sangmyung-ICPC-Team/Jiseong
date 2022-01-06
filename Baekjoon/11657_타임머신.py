# Gold 4
import sys
input = sys.stdin.readline
INF = 1000000000

n, m = map(int, input().split())
dist = [INF] * (n + 1)

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append([a, b, c])

def bellmanford(idx):
    dist[idx] = 0

    for i in range(n):
        for j in range(m):
            start = edges[j][0]
            end = edges[j][1]
            cost = edges[j][2]

            if dist[end] > dist[start] + cost and dist[start] != INF:
                dist[end] = dist[start] + cost

                if i == n - 1:
                    return True

    return False

iscycle = bellmanford(1)

if iscycle:
    print("-1")
else:
    for i in range(2, n + 1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])

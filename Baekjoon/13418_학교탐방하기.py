# Gold 3

import sys  
input = sys.stdin.readline 

# 어떤 원소 v가 주어졌을 때 이 원소가 속한 집합반환
def find(parent, v):
    # v가 루트가 아니면 재귀로 루트노드를 찾기
    if parent[v] != v:
        return find(parent, parent[v])
    # v가 루트노드면 자신 반환
    return v
# 두 집합을 하나의 집합으로 합치는 연산
def union(parent, n1, n2):
    #n1와 n2의 루트노드 찾기
    n1 = find(parent, n1)
    n2 = find(parent, n2)
    # 합치기
    if n1 > n2:
        parent[n1] = n2
    else:
        parent[n2] = n1

# kruskal로 피로도 계산
def kruskal(parent, graph):    
    k = 0
    for edge in graph:
        a, b, c  = edge 
        # 갈수 있는 v 찾기
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            # 오르막길(0)일 경우 체크
            if c == 0:
                k += 1
    # 피로도 k^2 반환
    return k ** 2

# 입력           
n, m = map(int, input().split())
t1 = [v for v in range(n + 1)]
t2 = [v for v in range(n + 1)]

graph = list()
for _ in range(m + 1):
    a, b, c = map(int, input().split())
    graph.append([a, b, c])

# 최고 최악 경로 만들어 피로도 값 구하기
# 오르막길(0) 기준 정렬
graph.sort(key = lambda item:item[2])
x = kruskal(t1, graph) # 최악
graph.sort(reverse = True, key = lambda item:item[2])
y = kruskal(t2, graph) # 최적

# 출력
print(x - y)

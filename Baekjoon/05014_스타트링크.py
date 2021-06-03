from collections import deque

def BFS(F, S, G, U, D):
    q = deque([[S, 0]])
    v = {S}

    while q:
        floor, cnt = q.popleft()
        if floor == G:  # 목표 층에 도착
            return cnt
        if ((floor + U <= F) and (floor + U not in v)):  # 위층으로 이동
            q.append([floor + U, cnt + 1])
            v.add(floor + U)
        if ((floor - D >= 1) and (floor - D not in v)):  # 아래층으로 이동
            q.append([floor - D, cnt + 1])
            v.add(floor - D)

    return "use the stairs"

F, S, G, U, D = map(int, input().split())
print(BFS(F, S, G, U, D))
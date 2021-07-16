# Gold 4

from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(n, sx, sy):
    #초기값
    q = deque([(sx, sy)])
    visit = set([(sx, sy)])

    shark_size = 2
    eat_cnt = 0
    eat_status = False
    time = 0
    answer = 0

    # 탐색
    while q:
        size = len(q)
        q = deque(sorted(q))

        for _ in range(size):
            x, y = q.popleft()
 
            # 현재 자리 확인 
            if board[x][y] != 0 and board[x][y] < shark_size:
                board[x][y] = 0
                eat_cnt += 1
                eat_status = True
                answer = time

                # 초기화
                q = deque()
                visit = set([(x, y)])

                # 상어 크기 체크
                if eat_cnt == shark_size:
                    shark_size += 1
                    eat_cnt = 0

            # 이동
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < n:
                    if (nx, ny) in visit:
                        continue

                    elif board[nx][ny] <= shark_size:
                        q.append((nx, ny))
                        visit.add((nx, ny))

            # 상태 확인
            if eat_status:
                eat_status = False
                break
            
        # 이동시간    
        time += 1
        
    return answer

# main
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 상어 위치 저장, 9 -> 0으로 바꾸기
x, y = 0, 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            x, y = i, j
            board[i][j] = 0

print(bfs(n, x, y))
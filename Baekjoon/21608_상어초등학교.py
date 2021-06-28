#21608번 상어초등학교 실버1
from sys import stdin

N = int(stdin.readline())

#init
favors = {}
for i in range(N**2):
    line = list(map(int, stdin.readline().split()))
    favors[line[0]] = line[1:]

orders = [i for i in favors.keys()]
# print(orders)

board = [[-1 for _ in range(N)] for _ in range(N)]
# print(borad)

# 완전 탐색
for stud in orders:
    cand_x, cand_y = None, None
    favor_n = -1
    empty_n = -1

    for i in range(N):
        for j in range(N):
            if board[i][j] == -1:
                favor_count = 0
                empty_count = 0
                for a, b in [[-1, 0], [0, -1], [1, 0], [0, 1]]: # up, left, down, right (r,c)
                    if (0 <= i + a < N and 0 <= j + b < N): # 범위 조정
                        if (board[i + a][j + b] in favors[stud]): # 현재 보는 학생번호가 보드에 있나?
                            favor_count += 1
                        if board[i + a][j + b] == -1: # 아에 없나
                            empty_count += 1 

                if favor_count > favor_n:
                    favor_n = favor_count
                    empty_n = empty_count
                    cand_x, cand_y = i, j
                elif favor_count == favor_n and empty_count > empty_n:
                    favor_n = favor_count
                    empty_n = empty_count
                    cand_x, cand_y = i, j

        board[cand_x][cand_y] = stud

# get score.
score = 0
for i in range(N):
    for j in range(N):
        favor_count = 0
        for a, b in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            if 0 <= i + a < N and 0 <= j + b < N:
                if board[i + a][j + b] in favors[board[i][j]]:
                    favor_count += 1
        if favor_count > 0:
            score += 10 ** (favor_count - 1)

print(score)
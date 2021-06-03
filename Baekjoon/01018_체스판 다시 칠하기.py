N, M = map(int, input().split())
board = list()

for i in range(N):
    board.append(input())
answer = list()
for i in range(N-7):
    for j in range(M-7):
        f_W, f_B = 0, 0
        for k in range(i,i+8):
            for l in range(j,j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        f_W = f_W + 1
                    if board[k][l] != 'B':
                        f_B = f_B + 1
                else:
                    if board[k][l] != 'B':
                        f_W = f_W + 1
                    if board[k][l] != 'W':
                        f_B = f_B + 1
        answer.append(f_W)
        answer.append(f_B)
        
print(min(answer))

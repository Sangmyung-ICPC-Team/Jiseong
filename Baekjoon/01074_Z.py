# Silver 1

import sys
input = sys.stdin.readline

ans = 0

def z(n, x, y):
    global ans
    # find!!
    if x == r and y == c:
        print(ans)
        return
    # n = 1이 되면 좌표 찾기 위해 돌면서 방문 횟수 누적
    if n == 1:
        ans += 1
        return
    # 해당하지 않는 영역의 사각형 수 방문 횟수로 누적
    if not (x <= r < x + n and y <= c < y + n):
        ans += n * n
        return

    z(n // 2, x, y) # 2사분면
    z(n // 2, x, y + n // 2) # 1사분면
    z(n // 2, x + n // 2, y) # 3사분면
    z(n // 2, x + n // 2, y + n // 2) # 4사분면

n, r, c = map(int, input().split())
z(2 ** n, 0, 0)

# Gold 5

import sys
input = sys.stdin.readline
INF = sys.maxsize

def binary_search(s : list, n : int):
    s.sort()
    L, R = 0, n - 1 
    min_val = INF
    temp = []

    while L < R:
        t = s[L] + s[R]
        if t == 0:
            temp = [s[L], s[R]]
            return temp
        elif abs(t) < min_val:
            min_val = abs(t)
            temp = [s[L], s[R]]
            
        if t < 0:
            L += 1
        else:
            R -= 1

    return temp

# 입력
n = int(input())
s = list(map(int, input().split()))

# 이진탐색
result = binary_search(s, n)

# 출력
print(result[0], result[1])
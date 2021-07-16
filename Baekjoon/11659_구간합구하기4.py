# Silver 3

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
sum_list = [0 for _ in range(n)]
answer = []

for i in range(n):
    if i == 0:
        sum_list[i] = num[i]
    else:
        sum_list[i] = sum_list[i - 1] + num[i]

for _ in range(m):
    i, j = map(int, input().split())
    if i == 1:
        answer.append(sum_list[j - 1])
    else:
        answer.append(sum_list[j - 1] - sum_list[i - 2])

for ans in answer:
    print(ans)
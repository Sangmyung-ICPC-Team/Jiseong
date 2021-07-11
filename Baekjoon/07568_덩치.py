# Silver 5

import sys
input = sys.stdin.readline

n = int(input())
body = list()
answer = list()
for _ in range(n):
    kg, cm = map(int, input().split())
    body.append([kg, cm])

for i in range(n):
    rank = 1
    for j in range(n):
        if i == j:
            continue

        if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
            rank += 1

    answer.append(rank)

for a in answer:
    print(a, end=" ")
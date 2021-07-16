# Silver 4

import sys
input = sys.stdin.readline

k = int(input())
s = []

for _ in range(k):
    num = int(input())
    if num == 0:
        s.pop()
    else:
        s.append(num)
print(sum(s))

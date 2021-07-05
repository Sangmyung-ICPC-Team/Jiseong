# Silver 4

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque()
ans = []

for _ in range(n):
    c = list(input().split())

    if c[0] == "push_front":
        dq.appendleft(c[1])

    elif c[0] == "push_back":
        dq.append(c[1])

    elif c[0] == "pop_front":
        if len(dq) == 0:
            ans.append(-1)
        else:
            ans.append(dq.popleft())

    elif c[0] == "pop_back":
        if len(dq) == 0:
            ans.append(-1)
        else:
            ans.append(dq.pop())

    elif c[0] == "size":
        ans.append(len(dq))

    elif c[0] == "empty":
        if len(dq) == 0:
            ans.append(1)
        else:
            ans.append(0)

    elif c[0] == "front":
        if len(dq) == 0:
            ans.append(-1)
        else:
            ans.append(dq[0])

    elif c[0] == "back":
        if len(dq) == 0:
            ans.append(-1)
        else:
            ans.append(dq[-1])

    else:
        pass

for a in ans:
    print(a)
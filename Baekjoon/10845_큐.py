# Silver 4

import sys
input = sys.stdin.readline

n = int(input())
queue = []
answer = []
for _ in range(n):
    c = input().split()

    if c[0] == "push":
        queue.append(c[1])
    elif c[0] == "pop":
        if queue:
            answer.append(queue.pop(0))
        else:
            answer.append(-1)
    elif c[0] == "size":
        answer.append(len(queue))
    elif c[0] == "empty":
        answer.append(1 - int(bool(queue)))
    elif c[0] == "front":
        if queue:  
            answer.append(queue[0])
        else:
            answer.append(-1)
    elif c[0] == "back":
        if queue:  
            answer.append(queue[-1])
        else:
            answer.append(-1)
    else:
        pass

for a in answer:
    print(a)
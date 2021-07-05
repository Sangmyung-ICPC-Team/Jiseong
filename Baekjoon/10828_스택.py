# Silver 4
import sys
input = sys.stdin.readline

n = int(input())
stack = []
answer = []
for _ in range(n):
    c = input().split()

    if c[0] == "push":
        stack.append(c[1])
    elif c[0] == "pop":
        if len(stack) == 0:
            answer.append("-1")
        else:
            answer.append(stack.pop())
    elif c[0] == "size":
        answer.append(len(stack))
    elif c[0] == "empty":
        if len(stack) == 0:
            answer.append("1")
        else:
            answer.append("0")
    elif c[0] == "top":
        if len(stack) == 0:
            answer.append("-1")
        else:
            answer.append(stack[-1])
    else:
        pass
for a in answer:
    print(a)

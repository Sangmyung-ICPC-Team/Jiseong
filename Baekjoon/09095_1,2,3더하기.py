# Silver 3
# n이 3보다 클 때, 
# f(n) = f(n - 1) + f(n - 2) + f(n - 3)

import sys
input = sys.stdin.readline

def dp_sol(n):
    if n == 1 or n == 2:
        return n
    elif n == 3:
        return 4
    else:
        return dp_sol(n - 1) + dp_sol(n - 2) + dp_sol(n - 3)

t = int(input())
answer = []

for _ in range(t):
    n = int(input())
    answer.append(dp_sol(n))
    
for a in answer:
    print(a)
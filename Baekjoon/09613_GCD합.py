# Silver 3

import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

t = int(input())
answer = []

for _ in range(t):
    a = list(map(int, input().split()))
    gcd_sum = 0
    for i in range(1,len(a)):
        for j in range(i+1,len(a)):
            gcd_sum += gcd(a[i],a[j])
    answer.append(gcd_sum)

for ans in answer:
    print(ans)

# Silver 5

import sys
input = sys.stdin.readline

n = int(input())
saram = []

for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    saram.append((age, name))

saram.sort(key = lambda saram: (saram[0]))

for s in saram:
    print(s[0], s[1])
# Silver 3
#이거 풀기 dp
import sys
input = sys.stdin.readline

n = int(input())
answer = []
for i in range(n):
    n = int(input())
    zero = 1
    one = 0
    tmp = 0
    for _ in range(n):
        tmp = one
        one = one + zero
        zero = tmp
    answer.append([zero, one])

for a in answer:
    print(a[0], a[1])

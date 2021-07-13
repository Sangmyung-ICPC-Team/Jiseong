# Silver 3

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
total_time = 0
wait_time = 0

for a in arr:
    wait_time += a
    total_time += wait_time

print(total_time)

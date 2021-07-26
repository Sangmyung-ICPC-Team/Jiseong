# Silver 2

import sys
input = sys.stdin.readline

n = int(input())
schedule = []
cnt = 0

for _  in range(n):
    start, end = map(int, input().split())
    schedule.append([start, end])
schedule = sorted(schedule, key = lambda s:s[0])
schedule = sorted(schedule, key = lambda s:s[1])

last_time = 0

for s, e in schedule:
    if s >= last_time:
        cnt += 1
        last_time = e

print(cnt)
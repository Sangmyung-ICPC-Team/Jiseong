# Silver 1

from collections import deque
import sys
input = sys.stdin.readline

def bfs(n):
    q = deque()
    q.append(n)

    while q: 
        v = q.popleft() 
        if v == k: 
            return time[v]

        step_list = [v - 1, v + 1, v * 2]
        for step in step_list: 
            if 0 <= step < MAX and not time[step]: 
                time[step] = time[v] + 1 
                q.append(step)

MAX = 100001 
n, k = map(int, input().split()) 
time = [0] * MAX 

print(bfs(n))


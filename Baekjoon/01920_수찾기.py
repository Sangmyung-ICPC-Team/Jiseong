# Silver 4

import sys 
input = sys.stdin.readline

n = int(input())
a = sorted(map(int,input().split()))
m = input()
m_num = map(int, input().split())

def binary_search(l, N, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if l == N[mid]:
        return 1
    elif l < N[mid]:
        return binary_search(l, N, start, mid - 1)
    else:
        return binary_search(l, N, mid + 1, end)

for i in m_num:
    start = 0
    end = len(a) - 1
    print(binary_search(i, a, start, end))
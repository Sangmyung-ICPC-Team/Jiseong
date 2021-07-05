# Gold 1

import sys
input = sys.stdin.readline

def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]


def prefix_sum(start, end, node, left, right):
    if left > end or right < start:
        return 0
   
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return prefix_sum(start, mid, node * 2, left, right) + \
        prefix_sum(mid + 1, end, node * 2 + 1, left, right)

def update(start, end, node, index, d):
    if index < start or index > end:
        return
        
    tree[node] += d

    if start == end: 
        return
    
    mid = (start + end) // 2
    update(start, mid, node * 2, index, d) # left
    update(mid + 1, end, node * 2 + 1, index, d) # right

n, m, k = map(int, input().split())
arr = []
tree = [0] * (4 * n)
answer = []
for i in range(n):
    arr.append(int(input()))

init(0, n - 1, 1)

for _ in range(m + k):
    a, b, c = map(int, input().rstrip().split())
    if a == 1:
        b -= 1 
        d = c - arr[b]
        arr[b] = c
        update(0, n - 1, 1, b, d)
    elif a == 2:
        b -= 1
        c -= 1
        answer.append(prefix_sum(0, n - 1, 1, b, c))

for i in answer:
    print(i)
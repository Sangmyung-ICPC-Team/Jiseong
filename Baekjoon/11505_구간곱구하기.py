# Gold 1

import sys
input = sys.stdin.readline
mod = 1000000007

def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) * init(mid + 1, end, node * 2 + 1) % mod
    return tree[node]


def prefix_mul(start, end, node, left, right):
    if left > end or right < start:
        return 1
   
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return prefix_mul(start, mid, node * 2, left, right) * \
        prefix_mul(mid + 1, end, node * 2 + 1, left, right) % mod

def update(start, end, node, index, val):
    if index < start or index > end:
        return

    if start == end:
        tree[node] = val 
        return
    
    mid = (start + end) // 2
    update(start, mid, node * 2, index, val) # left
    update(mid + 1, end, node * 2 + 1, index, val) # right
    tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % mod

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
        arr[b] = c
        update(0, n - 1, 1, b, c)
    elif a == 2:
        b -= 1
        c -= 1
        answer.append(prefix_mul(0, n - 1, 1, b, c))

for i in answer:
    print(i)
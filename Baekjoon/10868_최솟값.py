# Gold 1

import sys
input = sys.stdin.readline

def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = min(init(start, mid, node * 2), init(mid + 1, end, node * 2 + 1))
    return tree[node]

def get_min(start, end, node, left, right):
    if left > end or right < start:
        return 1000000001
   
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return min(get_min(start, mid, node * 2, left, right), \
        get_min(mid + 1, end, node * 2 + 1, left, right))

n, m = map(int, input().split())
arr = []
tree = [0] * (4 * n)
answer = []
for _ in range(n):
    arr.append(int(input()))

init(0, n - 1, 1)

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    answer.append(get_min(0, n - 1, 1, a - 1, b - 1))

for a in answer:
    print(a)
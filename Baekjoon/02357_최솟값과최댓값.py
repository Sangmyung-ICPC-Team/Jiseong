# Gold 1

import sys
input = sys.stdin.readline

def init_min(start, end, node):
    if start == end:
        tree_min[node] = arr[start]
        return tree_min[node]

    mid = (start + end) // 2
    tree_min[node] = min(init_min(start, mid, node * 2), init_min(mid + 1, end, node * 2 + 1))
    return tree_min[node]

def init_max(start, end, node):
    if start == end:
        tree_max[node] = arr[start]
        return tree_max[node]

    mid = (start + end) // 2
    tree_max[node] = max(init_max(start, mid, node * 2), init_max(mid + 1, end, node * 2 + 1))
    return tree_max[node]

def get_min(start, end, node, left, right):
    if left > end or right < start:
        return 1000000001
   
    if left <= start and end <= right:
        return tree_min[node]

    mid = (start + end) // 2
    return min(get_min(start, mid, node * 2, left, right), \
        get_min(mid + 1, end, node * 2 + 1, left, right))

def get_max(start, end, node, left, right):
    if left > end or right < start:
        return 0
   
    if left <= start and end <= right:
        return tree_max[node]

    mid = (start + end) // 2
    return max(get_max(start, mid, node * 2, left, right), \
        get_max(mid + 1, end, node * 2 + 1, left, right))

n, m = map(int, input().split())
arr = []
tree_max = [0] * (4 * n)
tree_min = [0] * (4 * n)
answer = []
for _ in range(n):
    arr.append(int(input()))

init_min(0, n - 1, 1)
init_max(0, n - 1, 1)

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    answer.append([get_min(0, n - 1, 1, a - 1, b - 1), get_max(0, n - 1, 1, a - 1, b - 1)])

for a in answer:
    print(a[0], a[1])
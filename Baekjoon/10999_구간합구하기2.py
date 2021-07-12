# Platinum 4
# https://www.acmicpc.net/problem/10999
# Lazy Propagation 게으른 전파
# 하나씩 업데이트해서 구간을 업데이트하는 것이 아니라 
# 한번에 그 구간을 대표하는 노드를 수정해 O(logN)만에 구간을 업데이트
# 개념: https://bowbowbow.tistory.com/4

import sys
input = sys.stdin.readline

def init(arr, tree, start, end, node):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        init(arr, tree, start, mid, node * 2)
        init(arr, tree, mid + 1, end, node * 2 + 1)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]

def update_lazy(tree, lazy, node, start, end):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0

def update_range(tree, lazy, start, end, node, idx_start, idx_end, diff):
    update_lazy(tree, lazy, node, start, end)
    if idx_start > end or idx_end < start:
        return 

    if idx_start <= start and end <= idx_end:
        tree[node] += (end - start + 1) * diff
        if start != end:
            lazy[node * 2] += diff
            lazy[node * 2 + 1] += diff
        return

    mid = (start + end) // 2
    update_range(tree, lazy, start, mid, node * 2, idx_start, idx_end, diff) # left
    update_range(tree, lazy, mid + 1, end, node * 2 + 1, idx_start, idx_end, diff) # right
    tree[node] = tree[node * 2] + tree[node * 2 + 1] 

def prefix_sum(tree, lazy, start, end, node, left, right):
    update_lazy(tree, lazy, node, start, end)
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return prefix_sum(tree, lazy, start, mid, node * 2, left, right) + \
        prefix_sum(tree, lazy, mid + 1, end, node * 2 + 1, left, right)


n, m, k = map(int, input().split())
arr = []
for v in range(n):
    arr.append(int(input()))

tree = [0] * (4 * n)
lazy = [0] * (4 * n)
answer = []

init(arr, tree, 0, n - 1, 1)

for _ in range(m + k):
    v = list(map(int, input().split()))
    
    if v[0] == 1:
        diff = v[3]
        update_range(tree, lazy, 0, n - 1, 1, v[1] - 1, v[2] - 1, diff)
    if v[0] == 2:
        answer.append(prefix_sum(tree, lazy, 0, n - 1, 1, v[1] - 1, v[2] - 1))

for a in answer:
    print(a)
# Gold 1

import sys
input = sys.stdin.readline

def merge(first, mid, last):
    global cnt
    i, j = first, mid + 1
    temp = []

    while i <= mid and j <= last:
        #원래 순서대로 저장
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        # 순서 바꿈(스와핑)
        else:
            temp.append(arr[j])
            j += 1
            cnt += (mid - i + 1) # 카운트

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= last:
        temp.append(arr[j])
        j += 1

    i = first
    idx = 0
    while (i <= last):
        arr[i] = temp[idx]
        i += 1
        idx += 1

def merge_sort(first, last):
    if first < last:
        mid = (first + last) // 2
        merge_sort(first, mid)
        merge_sort(mid + 1, last)
        merge(first, mid, last)

n = int(input())
arr = list(map(int, input().split()))
cnt = 0
merge_sort(0, n - 1)
print(cnt)

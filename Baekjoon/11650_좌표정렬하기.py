# Silver 5

import sys
input = sys.stdin.readline

def merge(first, mid, last):
    global arr
    temp = []
    idx = 0
    i, j = first, mid + 1

    while i <= mid and j <= last:
        if arr[i][0] < arr[j][0]:
            temp.append(arr[i])
            i += 1

        elif arr[i][0] > arr[j][0]:
            temp.append(arr[j])
            j += 1
        else:
            if arr[i][1] < arr[j][1]:
               temp.append(arr[i])
               i += 1
            elif arr[i][1] > arr[j][1]:
                temp.append(arr[j])
                j += 1
    
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
    global arr
    if first < last:
        mid = (first + last) // 2
        merge_sort(first, mid)
        merge_sort(mid + 1, last)
        merge(first, mid, last)

n = int(input())
arr = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])

merge_sort(0, n - 1)

for a in arr:
    print(a[0], a[1])
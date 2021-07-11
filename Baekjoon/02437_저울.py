# Gold 3
# https://www.acmicpc.net/problem/2437

import sys
input = sys.stdin.readline

def quick_sort(arr, start, end):
    if start >= end: 
        return
    pivot = start 
    left = start + 1
    right = end
    while(left <= right):
         
        while(left <= end and arr[left] <= arr[pivot]):
            left += 1
        
        while(right > start and arr[right] >= arr[pivot]):
            right -= 1
        if(left > right): 
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else: 
            arr[left], arr[right] = arr[right], arr[left]
    
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

n = int(input())
choo_list = list(map(int, input().split()))
ans = 1
quick_sort(choo_list, 0, len(choo_list) - 1)

for choo in choo_list:
    # 추의 합 + 1 보다 저울추의 무게가 클 때
    if ans < choo:
        break
    ans += choo

print(ans)
# Silver 5

from sys import stdin as st

n = int(st.readline()) 
arr = [0] * 10001

for _ in range(n): 
    c = int(st.readline()) 
    arr[c] += 1

for i in range(10001): 
    while arr[i]:
        print(i)
        arr[i] -= 1

# Silver 5

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, str(n)))
arr.sort(reverse = True)
for a in arr:
    print(a, end = "")
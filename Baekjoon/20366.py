import sys
input = sys.stdin.readline

n = int(input())
snow = list(map(int, input().split()))
snow.sort()

res = 1000000000000

for i in range(n - 3):
    for j in range(i + 3, n):
        l, r = i + 1, j - 1
        t1 = snow[i] + snow[j]
        
        while l < r:
            t2 = snow[l] + snow[r]

            if res > abs(t1 - t2):
                res = abs(t1 - t2)
            
            if t1 > t2:
                l = l + 1
            elif t1 < t2:
                r = r - 1
            else:
                print(0)
                sys.exit(0)
print(res)
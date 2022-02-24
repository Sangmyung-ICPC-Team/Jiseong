n, m = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0

for i in range(n):
    p = i
    temp = 0

    while True:
        if p == n:
            break
        
        temp += a[p]

        if temp == m:
            cnt += 1
            break
        elif temp > m:
            break

        p += 1
    
print(cnt)




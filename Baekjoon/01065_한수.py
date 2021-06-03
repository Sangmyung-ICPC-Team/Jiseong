N = int(input())
cnt = 0

for i in range(1, N+1):
    if i <=99:
        cnt += 1
    else:
        d = list(map(int, str(i)))
        if d[0] - d[1] == d[1] - d[2]:
            cnt += 1
print(cnt)
N,M = map(int, input().rsplit())
arr = [list(map(int, list(input().rstrip()))) for _ in range(N)]
answer = 0

if(N == 1):
    for i in arr:
        if sum(i):
            answer = 1
            break
else:            
    for i in range(1,N):
        for j in range(1,M):
            if arr[i][j] == 1:
                arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1
            answer = max(answer, arr[i][j])
            
print(answer**2)

"""
N,M = map(int, input().rsplit())
arr = [list(map(int, list(input().rstrip()))) for _ in range(N)]
answer = 0
        
for i in range(N):
    for j in range(M):
        if i>0 and j>0 and arr[i][j] == 1:
            arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1
        answer = max(answer, arr[i][j])
            
print(answer**2)
"""
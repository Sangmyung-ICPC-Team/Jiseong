# Silver 5

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda arr: (arr[1], arr[0]))

for a in arr:
    print(a[0], a[1])
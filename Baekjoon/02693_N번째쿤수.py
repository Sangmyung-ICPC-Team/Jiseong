# Silver 5

t = int(input())
answer = []
for _ in range(t):
    arr = list(map(int, input().split()))
    arr.sort()
    answer.append(arr[-3])
for a in answer:
    print(a)
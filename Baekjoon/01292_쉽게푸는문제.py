# Silver 5
# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5, 3 7 -> 15 (2 3 3 3 4)

a, b = map(int, input().split())
num = []

for i in range(1, 101):
    num += [i] * i
print(sum(num[a - 1 : b]))

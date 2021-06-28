n, m = map(int , input().split())
# 각 행마다 가장 작은 수를 찾은 뒤에 
# 그 수 중에서 가장 큰수

# [1] min()
result = 0
for u in range(n):
    data = list(map(int , input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

# [2] 2중 for문
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)
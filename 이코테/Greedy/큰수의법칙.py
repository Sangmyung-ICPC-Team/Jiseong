# N,M,K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() #입력받은 수들 정렬
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번쨰로 큰수

#[1]
result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m-=1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

#[2]
# 가장 큰 수가 더해지는 횟수 계산
cnt = int(m / (k + 1)) * k 
cnt += m % (k + 1) # 나누어 떨어지지 않는 경우 고려

result = 0
result += (cnt) * first
result += (m - cnt) * second

print(result)
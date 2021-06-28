n, k = map(int, input().split())

# [1]
cnt = 0
while True:
    if n == 1:
        break
    if n % k == 0:
        n //= k
        cnt += 1
    else: 
        n -= 1
        cnt += 1

print(cnt)

#[2] 더 효율적인 방법 // [1]은 시간 초과 날 수 있음
result = 0
while True:
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    result += 1
    n //= k
#마지막으로 남은 수에 대하여 1씩 빼기
result += (n -1)
print(result)



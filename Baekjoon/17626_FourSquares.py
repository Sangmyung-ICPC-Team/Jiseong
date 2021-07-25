# Silver 5
# 어려워...
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
dp[0], dp[1] = 0, 1

for i in range(2, n + 1):
    if i == int(i ** 0.5) ** 2:
        dp[i] = 1
    else:
        dp[i] = i

for i in range(2, n + 1):
    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], dp[j ** 2] + dp[i - (j ** 2)])

print(dp[n])

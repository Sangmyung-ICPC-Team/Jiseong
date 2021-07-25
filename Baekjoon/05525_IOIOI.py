# Silver 2

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

ans, cnt, idx = 0, 0, 0

while idx < m - 1:
    if s[idx - 1] == "I" and s[idx] == "O" and s[idx + 1] == "I":
        cnt += 1
        if cnt == n:
            ans += 1
            cnt -= 1
        idx += 1
    else:
        cnt = 0
    idx += 1 
print(ans)

############

# ans2, cnt2, idx2 = 0, 0, 0

# while idx2 < m - 3:
#     if s[idx2 : idx2 + 3] == 'IOI':
#         cnt2 += 1
#         if cnt2 == n: 
#             cnt2 -= 1 
#             ans2 += 1 
#         idx2 += 1 
#     else:
#         cnt2 = 0
#     idx2 += 1

# print(ans2)



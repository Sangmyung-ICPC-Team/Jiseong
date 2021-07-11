# Silver 3
import sys
input = sys.stdin.readline

k, l = map(int, input().split())

stunum_dict = {}
for i in range(l):
    num = input()
    if len(num) == 8:
        stunum_dict[num] = i

stunum_dict = dict(sorted(stunum_dict.items(), key = lambda x : x[1]))
answer = list(stunum_dict.keys())

for i in range(min(k, len(answer))):
    print(answer[i])
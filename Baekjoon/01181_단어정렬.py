# Silver 5

import sys
input = sys.stdin.readline
n = int(input())

init_words = []
for _ in range(n):
    init_words.append(input().strip())

init_words = list(set(init_words))

# 소팅 (1차: 길이, 2차: 사전 순)
#람다를 사용하면 한개 이상의 키로 정렬을 할 수 있다.
# key=lambda x: (len(x), x))
sort_words = sorted(init_words, key=lambda x: (len(x), x))

for word in sort_words:
    print(word)
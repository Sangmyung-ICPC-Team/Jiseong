# Gold 5

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

available_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
error_num = list(map(str, input().split()))
for e in error_num:
    if e in available_num:
        available_num.remove(e)

start_num = 100

answer = abs(n - start_num)
               
for num in range(1000001): # 0 <= n <= 500000, 1000000
    num = str(num)
    for i in range(len(num)):
        # 현재 숫자가 입력 불가능한 숫자인지 확인
        if num[i] not in available_num:
            break
        # 모두 사용가능한 번호버튼일 때
        elif i == len(num) - 1:
            # 이전값과 채널번호 + +-를 눌러야하는 회수 비교해서 최소값 저장
            answer = min(answer, abs(n - int(num)) + len(str(num)))

print(answer)
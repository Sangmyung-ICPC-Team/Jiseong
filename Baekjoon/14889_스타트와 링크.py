#경우의 수 구하는 라이브러리
from itertools import combinations 

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
case = []

#경우의수 조합으로 가능한 팀을 만듬
for team in list(combinations(members, N//2)):
    case.append(team)
#예시 입력 1 의 경우 경우의 수 -> [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
# 각 팀에 한 직원만 있어야 한다 -> 리스트에서 첫 조합의 여집합 마지막 조합
# case[i] case[-i-1]로 팀 구분
# for문으로 팀에서 맴버와 함께할 경우의 능력치 구하고 min으로 가장 작은 차이를 구한다.
min_stat_gap = 1000000 

for i in range(len(case)//2):
    #start
    team = case[i]
    stat_start = 0 #start 팀 능력치
    for j in range(N//2):
        member = team[j] #멤버
        for k in team:
            stat_start += S[member][k] #능력치 더함
    
    #link
    team = case[-i-1]
    stat_link = 0 #link 팀 능력치
    for j in range(N//2):
        member = team[j] #멤버
        for k in team:
            stat_link += S[member][k] #능력치 더함
    # 능력치 차이의 최소값을 구함
    min_stat_gap = min(min_stat_gap, abs(stat_start - stat_link)) 
    
print(min_stat_gap)
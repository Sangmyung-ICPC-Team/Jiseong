# Silver 5
# 유클리드 호제법 사용
import sys 

input = sys.stdin.readline
A, B = map(int, input().split()) 
a, b = A, B 

while b != 0: 
    a = a % b 
    a, b = b, a 
    
print(a) 
print(A*B//a)


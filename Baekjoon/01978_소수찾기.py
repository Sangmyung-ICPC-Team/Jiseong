# Silver 4

n = int(input())
numbers = map(int, input().split())
primenum = 0

for num in numbers:
    check = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                check = 1
        if check == 0:
            primenum += 1

print(primenum)
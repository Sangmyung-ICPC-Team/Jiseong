# Silver 5

start = int(input())
last = int(input())

primenum = []
for num in range(start, last+1):
    check = 0
    if num > 1 :
        for i in range(2, num):  
            if num % i == 0:
                check += 1
                break  
        if check == 0:
            primenum.append(num)
            
if len(primenum) > 0 :
    print(sum(primenum))
    print(min(primenum))
else:
    print(-1)
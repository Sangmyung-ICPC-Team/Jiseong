# Silver 2
# In[1]
m, n = map(int, input().split())
answer = []
for i in range(m, n + 1):
    if i == 1:
        continue
    elif i == 2:
        answer.append(i)
        continue

    check = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            check = False
            break

    if check:
        answer.append(i)

for a in answer:
    print(a)
    
# In[2]    
def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)
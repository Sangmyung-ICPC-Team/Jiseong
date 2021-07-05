# Silver 4
# In[1]
n = int(input())
answer = list()

for _ in range(n):
    check = True
    stack = list()
    ps = list(input())

    for i in range(len(ps)):
        if ps[i] == "(":
            stack.append(ps[i])
        else:
            try:
                if stack.pop() == "(":
                    pass
            except:
                answer.append("NO")
                check = False
                break

    if len(stack):
        answer.append("NO")
        continue
    
    if check:
        answer.append("YES")

for a in answer:
    print(a)

# In[2]

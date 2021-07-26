# Silver 5

num = list(input())
c = [0] * 10

for n in num:
    if n == '6' or n == '9':
        if c[6] == c[9]:
            c[6] += 1
        else:
            c[9] += 1
    else:
        c[int(n)] += 1

print(max(c))

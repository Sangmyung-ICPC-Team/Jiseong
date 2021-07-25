# Silver 5

import sys
input = sys.stdin.readline

n = input()
Croatian_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for c in Croatian_alphabet:
    n = n.replace(c, "@")

print(len(n))


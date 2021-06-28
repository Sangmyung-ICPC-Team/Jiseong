import sys

def pseudo_palindrome(word,left,right):
    while (left < right):
        if (word[left] == word[right]):
            left += 1
            right -= 1
        else:
            return False
    return True


def palindrome(word,left,right):
    while (left < right):
        if (word[left] == word[right]):
            left += 1
            right -= 1
        else:
            check1 = pseudo_palindrome(word,left+1,right)
            check2 = pseudo_palindrome(word,left,right-1)
            if(check1 or check2):
                return 1
            else:
                return 2
    return 0

T = int(sys.stdin.readline().rstrip("\n"))
ans_list = list()

for _ in range(T):
    word = sys.stdin.readline().rstrip("\n")
    left = 0
    right = len(word)-1
    ans_list.append(palindrome(word, left, right))

for ans in ans_list:
    print(ans)
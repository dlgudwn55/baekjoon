import sys
input = sys.stdin.readline

def check_palindrome(text):
    left, right = 0, len(text)-1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

def check_pseudo_palindrome(text):
    is_left, is_right = True, True

    left, right = 0, len(text)-1
    flag = True
    while left < right:
        if text[left] != text[right]:
            if flag:
                left += 1
                flag = False
            else:
                is_left = False
                break
        else:
            left += 1
            right -= 1

    left, right = 0, len(text)-1
    flag = True
    while left < right:
        if text[left] != text[right]:
            if flag:
                right -= 1
                flag = False
            else:
                is_right = False
                break
        else:
            left += 1
            right -= 1
    
    return is_left or is_right

n = int(input())
for _ in range(n):
    str_input = input().strip()
    if check_palindrome(str_input):
        print(0)
    elif check_pseudo_palindrome(str_input):
        print(1)
    else:
        print(2)

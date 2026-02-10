ALPHA = "abcdefghijklmnopqrstuvwxyz"

s = input()

if len(s) < 26:
    for char in ALPHA:
        if char not in s:
            print(s + char)
            exit()
else:
    for i in range(25, -1, -1):
        prefix = s[:i]
        for char in ALPHA:
            if char > s[i] and char not in prefix:
                print(prefix + char)
                exit()
print(-1)
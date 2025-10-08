left = "qwertasdfgzxcvb"
right = "yuiophjklnm"

s = input()
cur = None
if s[0] in left:
    cur = "left"
elif s[0] in right:
    cur = "right"

ans = "yes"
for char in s[1:]:
    if char in left and cur == "left":
        ans = "no"
        break
    if char in right and cur == "right":
        ans = "no"
        break
    if cur == "left":
        cur = "right"
    else:
        cur = "left"
print(ans)
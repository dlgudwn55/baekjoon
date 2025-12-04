grade_dict = {"A+": 4.5, "A": 4.0, "B+": 3.5, "B": 3.0,
"C+": 2.5, "C": 2.0, "D+": 1.5, "D": 1.0, "F": 0.0}

s = input()
left = 0
right = 0
count = 0
total = 0
while left < len(s) and right < len(s):
    if right < len(s)-1 and s[right+1] == "+":
        right += 1
        total += grade_dict[s[left:right+1]]
        count += 1
        left += 2
        right += 1
    else:
        total += grade_dict[s[left:right+1]]
        count += 1
        left += 1
        right += 1
print(total/count)
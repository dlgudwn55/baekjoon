def check_case(team_name: str):
    upper_count = 0
    lower_count = 0
    for char in team_name:
        if char.isalpha():
            if char.isupper():
                upper_count += 1
            elif char.islower():
                lower_count += 1
    return upper_count <= lower_count

def check_length(team_name: str):
    return len(team_name) <= 10

def check_config(team_name: str):
    for char in team_name:
        if not char.isnumeric():
            return True
    return False

n = int(input())
ans = ""
for _ in range(n):
    s = input()
    if check_case(s) and check_length(s) and check_config(s):
        ans = s

print(ans)
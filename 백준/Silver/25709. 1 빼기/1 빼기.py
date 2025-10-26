def solve(num, count):
  global ans
  if num == '0':
    ans = min(ans, count)
    return
  if num == '1':
    ans = min(ans, count + 1)
    return
  if '1' not in num:
    solve(str(int(num)-1), count + 1)
  else:
    for i in range(len(num)):
      if num[i] == '1':
        tmp = num[:i] + num[i+1:]
        solve(str(int(tmp)), count + 1)

n = input()
ans = 999999999
solve(n, 0)
print(ans)
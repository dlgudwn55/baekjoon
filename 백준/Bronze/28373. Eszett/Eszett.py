word = input()
lower_word = word.lower()
ans = set()
ans.add(lower_word)
for i in range(len(lower_word)):
    tmp = lower_word[:i]
    tmp += lower_word[i:].replace("ss", "B")
    ans.add(tmp)
for item in ans:
    print(item)
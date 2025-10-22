while True:
    year = int(input())
    if year == 0:
        break
    if year < 1896 or year % 4:
        print(f"{year} No summer games")
    elif 1914 <= year <= 1918 or 1939 <= year <= 1945:
        print(f"{year} Games cancelled")
    elif year > 2020:
        print(f"{year} No city yet chosen")
    else:
        print(f"{year} Summer Olympics")
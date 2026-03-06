n = int(input())
teams = []
for _ in range(n):
    teams.append(input())

rank_dict = {}
for i, team in enumerate(teams):
    if team not in rank_dict:
        rank_dict[team] = [i]
    else:
        rank_dict[team].append(i)

overall_performance_dict = {}
for k, v in rank_dict.items():
    overall_performance_dict[k] = sum(v) / len(v)

overall_performance = sorted(list(overall_performance_dict.items()), key=lambda x: x[1])
for i in range(len(overall_performance)):
    print(overall_performance[i][0])
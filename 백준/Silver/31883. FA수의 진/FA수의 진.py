import sys

input = sys.stdin.readline

N = int(input())
traffic_data = []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    traffic_data.append((a, b, c, d))

time = 0
for i in range(N):
    crosswalk, bridge, green, red = traffic_data[i]
    is_green = time % (green + red) < green
    if is_green:
        time += min(crosswalk, bridge)
    else:
        round = time // (green + red)
        time_to_green = (round + 1) * (green + red) - time
        time += min(bridge, time_to_green + crosswalk)

print(time)
file = open("7.input")
input = list(map(int, file.readline().split(",")))
input.sort()

mid = input[len(input) // 2]
fuel = 0
for item in input:
    if item != mid:
        n = abs(mid - item)
        fuel += n

print(fuel)

def score(origin):
    fuel = 0
    for item in input:
        if item != origin:
            n = abs(origin - item)
            fuel += (n * (n + 1)) // 2
    return fuel

min_score = score(input[0])

for i in range(input[0] + 1, input[len(input) - 1]):
    print(i) 
    min_score = min(score(i), min_score)

print(min_score)

lo = input[0] 
hi = input[len(input) - 1]
while lo < hi:
    mid = (lo + hi) // 2
    mid_score = score(mid)
    if score(lo) < mid_score:
        hi = mid
    elif score(hi) < mid_score:
        lo = mid

#   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15
# 242, 206, 183, 170, 168, 176, 194, 223, 262, 311, 370, 439, 518, 607, 707
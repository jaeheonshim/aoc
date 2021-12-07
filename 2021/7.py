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
    min_score = min(score(i), min_score)

print(min_score)
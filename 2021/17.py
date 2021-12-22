import re

data = list(map(int, re.findall("-?[0-9]+", open("17.input").readline())))

bound_min = (min(data[0], data[1]), min(data[2], data[3]))
bound_max = (max(data[0], data[1]), max(data[2], data[3]))

def sign(n):
    if n == 0: return 0
    return int(n / abs(n))

def maxY(vy):
    y = 0
    while vy > 0:
        y += vy
        vy -= 1

    return y

def check(vx, vy):
    x = 0
    y = 0
    while x <= bound_max[0] and not (y < bound_min[1] and vy < 0):
        x += vx
        y += vy
        vx = (abs(vx) - 1) * sign(vx)
        vy -= 1

        if bound_min[0] <= x <= bound_max[0] and bound_min[1] <= y <= bound_max[1]:
            return True
    return False

def brutecheck(vy):
    for i in range(bound_max[0]):
        if(check(i, vy)):
            return True
    
    return False

maxvy = 0

for i in range(abs(bound_min[1])):
    if brutecheck(i):
        maxvy = i

print(maxY(maxvy))

count = 0

for vx in range(bound_max[0] + 1):
    for vy in range(-abs(bound_min[1]), abs(bound_min[1]) + 1):
        if check(vx, vy): count += 1

print(count)
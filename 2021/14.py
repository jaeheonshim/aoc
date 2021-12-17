from collections import defaultdict

data = open("14.input")

firstline = data.readline().strip()

pairs = defaultdict(lambda: 0, {})
chars = defaultdict(lambda: 0, {})
mapping = {}

chars[firstline[0]] = 1

for i in range(len(firstline) - 1):
    pairs[firstline[i] + firstline[i + 1]] += 1
    chars[firstline[i + 1]] += 1

for line in data:
    if not line.strip(): continue
    spl = line.split("->")
    mapping[spl[0].strip()] = spl[1].strip()

def insert():
    global chars
    global pairs

    newpairs = pairs.copy()
    newchars = chars.copy()
    for key in mapping:
        if key in pairs:
            newpairs[key[0] + mapping[key]] += pairs[key]
            newpairs[mapping[key] + key[1]] += pairs[key]
            newchars[mapping[key]] += pairs[key]
            newpairs[key] -= pairs[key]
    chars = newchars
    pairs = newpairs

for i in range(10):
    insert()

print(max(chars.values()) - min(chars.values()))

for i in range(30):
    insert()

print(max(chars.values()) - min(chars.values()))

import functools

scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
scores2 = {")": 1, "]": 2, "}": 3, ">": 4}
correspond = {"(": ")", "[": "]", "{": "}", "<": ">"}

def scoreline(line):
    stack = []
    for char in line.strip():
        if char in correspond:
            stack.append(char)
        else:
            if correspond[stack.pop()] != char: return scores[char]
    return 0

file = open("10.input")

print(sum([scoreline(line) for line in file]))

def scoremissing(line):
    stack = []
    for char in line.strip():
        if char in correspond:
            stack.append(char)
        else:
            if correspond[stack.pop()] != char: return 0
    return functools.reduce(lambda a, b: a * 5 + b, [scores2[correspond[n]] for n in reversed(stack)])

file.seek(0)
finalscores = []
for line in file:
    score = scoremissing(line)
    if score:
        finalscores.append(score)

finalscores.sort()
print(finalscores[len(finalscores) // 2])
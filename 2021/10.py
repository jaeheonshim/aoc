scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

def scoreline(line):
    stack = []
    for char in line:
        if char == "(":
            stack.append("(")
        elif char == "[":
            stack.append("[")
        elif char == "{":
            stack.append("{")
        elif char == "<":
            stack.append("<")
        elif char == ")":
            if stack.pop() != "(": return scores[char]
        elif char == "]":
            if stack.pop() != "[": return scores[char]
        elif char == "}":
            if stack.pop() != "{": return scores[char]
        elif char == ">":
            if stack.pop() != "<": return scores[char]
    return 0

file = open("10.input")

print(sum([scoreline(line) for line in file]))
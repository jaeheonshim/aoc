import ast
import copy

def add(p1, p2):
    if p1 == None: return p2
    if p2 == None: return p1
    return reduce([p1, p2])

def leftmostadd(arr, n):
    if type(arr[0]) != list:
        arr[0] += n
    else:
        leftmostadd(arr[0], n)

def rightmostadd(arr, n):
    if type(arr[len(arr) - 1]) != list:
        arr[len(arr) - 1] += n
    else:
        rightmostadd(arr[len(arr) - 1], n)

def explode(num, depth):
    if(depth == 4):
        return num
    
    for i in range(len(num)):
        el = num[i]
        if type(el) == list:
            pair = explode(el, depth + 1)
            if not pair: continue
            if depth == 3:
                n = num.index(pair)
                num.pop(n)
                num.insert(n, 0)
            if i - 1 >= 0 and type(num[i - 1]) != list:
                num[i - 1] += pair[0]
                pair[0] = 0
            elif i - 1 >= 0:
                rightmostadd(num[i - 1], pair[0])
                pair[0] = 0
            if i + 1 < len(num) and type(num[i + 1]) != list:
                num[i + 1] += pair[1]
                pair[1] = 0
            elif i + 1 < len(num):
                leftmostadd(num[i + 1], pair[1])
                pair[1] = 0
            return pair
    return None

def split(arr):
    for i in range(len(arr)):
        if(type(arr[i]) == int):
            if arr[i] > 9:
                arr[i] = [arr[i] // 2, int(arr[i] / 2 + 0.5)]
                return True
        else:
            if(split(arr[i])): return True

    return False

def reduce(arr):
    while len(arr) > 0:
        if(explode(arr, 0)): continue
        if(split(arr)): continue
        return arr

def magnitude(el):
    if type(el) != list:
        return el
    return 3 * magnitude(el[0]) + 2 * magnitude(el[len(el) - 1])

data = open("18.input")

nums = []
for line in data:
    nums.append(ast.literal_eval(line.strip()))

result = None

for num in nums:
    result = add(result, num)

print(magnitude(result))

nums.clear()
data.seek(0)

nums = []
for line in data:
    nums.append(ast.literal_eval(line.strip()))

largest = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        largest = max(largest, magnitude(add(copy.deepcopy(nums[i]), copy.deepcopy(nums[j]))))
        largest = max(largest, magnitude(add(copy.deepcopy(nums[j]), copy.deepcopy(nums[i]))))

print(largest)
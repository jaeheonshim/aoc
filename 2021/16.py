import functools

# Note: BS = "Bit String"
def dec(bs):
    return int(str(bs), 2)

def tobs(hex):
    bs = []
    for char in hex:
        if '0' <= char <= '9':
            n = ord(char) - ord('0')
        else:
            n = ord(char) - ord('A') + 10
        bs.append(format(n, "04b"))

    return "".join(bs)

def process(bs, packets, stack):
    ver = dec(bs[0:3])
    type = dec(bs[3:6])

    packets.append(ver)
    
    if type == 4:
        # literal value
        data = bs[6:]
        value = []
        for i in range(0, len(data), 5):
            chunk = data[i:i + 5]
            value.append(chunk[1:])
            if chunk[0] == "0": break
        
        literal = dec("".join(value))
        stack.append(literal)

        return data[i + 5:]
    else:
        # operator
        ltype = bs[6]
        n = len(stack)
        if ltype == "0":
            sublen = dec(bs[7:22])
            data = bs[22:22 + sublen]
            res = process(data, packets, stack)
            while res:
                res = process(res, packets, stack)

            stack.append(calcstack(stack, type, len(stack) - n))
            return bs[22+sublen:]
        else:
            sublen = dec(bs[7:18])
            data = bs[18:]
            res = process(data, packets, stack)
            for i in range(sublen - 1):
                res = process(res, packets, stack)

            stack.append(calcstack(stack, type, len(stack) - n))

            return res
            
def calcstack(stack, type, n):
    values = []
    for i in range(n):
        values.append(stack.pop())
    
    if type == 0:
        return sum(values)
    elif type == 1:
        return functools.reduce(lambda a, b: a  * b, values)
    elif type == 2:
        return min(values)
    elif type == 3:
        return max(values)
    elif type == 5:
        return int(values[1] > values[0])
    elif type == 6:
        return int(values[1] < values[0])
    elif type == 7:
        return int(values[1] == values[0])

data = open("16.input").readline()
res = []
stack = []
process(tobs(data), res, stack)
print(sum(res))
print(stack[0])
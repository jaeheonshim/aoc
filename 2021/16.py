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

def process(bs, packets):
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

        return data[i + 5:]
    else:
        # operator
        ltype = bs[6]
        if ltype == "0":
            sublen = dec(bs[7:22])
            data = bs[22:22 + sublen]
            res = process(data, packets)
            while res:
                res = process(res, packets)
            return bs[22+sublen:]
        else:
            sublen = dec(bs[7:18])
            data = bs[18:]
            res = process(data, packets)
            for i in range(sublen - 1):
                res = process(res, packets)

            return res
            
data = open("16.input").readline()
res = []
process(tobs(data), res)
print(sum(res))
file = open("1.input")
lines = file.readlines()
file.close()
lines = list(map(int, lines))

for n in lines:
    if (2020 - n) in lines:
        print(n * (2020 - n))
        exit
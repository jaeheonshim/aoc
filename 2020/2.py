import re

file = open("2.input")
valid = 0
for line in file:
	m = re.search("(\d*)-(\d*)\s(.):\s(.*)", line).groups()
	if int(m[0]) <= m[3].count(m[2]) <= int(m[1]): valid += 1
print(valid)

file.seek(0)

valid = 0
for line in file:
	m = re.search("(\d*)-(\d*)\s(.):\s(.*)", line).groups()
	pword = m[3]
	char = m[2]
	if (pword[int(m[0]) - 1] == char) != (pword[int(m[1]) - 1] == char):
		valid += 1
print(valid)

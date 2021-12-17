file = open("4.input")
passports = []
currentDict = {}
for line in file:
	if not line.strip():
		passports.append(currentDict)
		currentDict = {}
	else:
		for pair in line.strip().split():
			keyVal = pair.split(":")
			currentDict[keyVal[0]] = keyVal[1]

passports.append(currentDict)

valid = 0
for passport in passports:
	if(len(passport) == 8): valid += 1
	elif len(passport) == 7 and "cid" not in passport: valid += 1

print(valid)

def validate(passport):
	if len(passport["byr"]) != 4 or not (1920 <= int(passport["byr"]) <= 2002):
		return False
	if len(passport["iyr"]) != 4 or not (2010 <= int(passport["iyr"]) <= 2020):
		return False
	if len(passport["eyr"]) != 4 or not (2020 <= int(passport["eyr"]) <= 2030):
		return False
	if passport["hgt"][-2:] != "cm" or passport["hgt"][-2:] != "in":
		return False
	if passport["hgt"][-2:] == "cm" and not (150 <= passport["hgt"][:-2] <= 193):
		return False
	elif passport["hgt"][-2:] == "in" and not (59 <= passport["hgt"][:-2] <= 76):
		return False
	

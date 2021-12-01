import re

with open('input.txt') as input:
    list = input.read().split('\n\n')

# part 1
terms = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passports = 0

for passport in list:
    if all(x in passport for x in terms):
        passports += 1
print(passports)

# part 2
passports = 0

for passport in list:
    if (re.search(r"byr:19[2-9]\d|byr:200[0-2]", passport) and 
    re.search(r"eyr:202\d|eyr:2030", passport) and 
    re.search(r"iyr:201\d|iyr:2020", passport) and
    re.search(r"hgt:1[5-8]\dcm|hgt:19[0-3]cm|hgt:59in|hgt:6\din|hgt:7[0-6]in", passport) and
    re.search(r"hcl:#[a-f0-9]{6}", passport) and
    re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)", passport) and
    re.search(r"pid:\d{9}\b", passport)):
        passports +=1
print(passports)
def components(line):
    policy, password = line.split(': ',1)
    num, letter = policy.split()
    a, b = map(int, num.split('-'))
    return a, b, letter, password

def valid(line):
    min, max, letter, password = components(line)
    return min <= password.count(letter) <= max

def valid2(line):
    pos1, pos2, letter, password = components(line)
    return (password[pos1-1] == letter) != (password[pos2-1] == letter)

print(sum(1 for _ in filter(valid, open('input.txt'))))
print(sum(1 for _ in filter(valid2, open('input.txt'))))
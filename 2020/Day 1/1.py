import itertools

## part 1
for (a,b) in itertools.combinations([int(n) for n in open('input.txt')], 2):
    if a+b == 2020:
        print(a*b)

## part 2
for (a,b,c) in itertools.combinations([int(n) for n in open('input.txt')], 3):
    if a+b+c == 2020:
        print(a*b*c)
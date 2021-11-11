import itertools
for (a,b) in itertools.combinations([int(n) for n in open('input.txt')], 2):
    if a+b == 2020:
        print(a*b)
input = open('input.txt').read().strip('\n').splitlines()

# turn the seats into binary and then sort them
seats = [int(x.replace('F', '0').replace('B','1').replace('L','0').replace('R','1'),2) for x in input]
seats.sort()
print(max(seats))

# find the difference in consecutive seats that doesn't equal 1
for x in range(len(seats)):
    if seats[x+1] - seats[x] != 1:
        print(seats[x] + 1)
        break
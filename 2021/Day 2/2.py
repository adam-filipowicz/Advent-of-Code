with open('input.txt') as f:
    instructions = f.readlines() # remember readlines() returns a list containing each line in the file as a list item

# part 1
horizontal = 0
depth = 0 # need to set both of our positions at 0
for instruction in instructions:
    direction, distance = instruction.split() # need to split up each line into a direction command and a distance command
    distance = int(distance) # also need to turn distance into an int so that it can be added to our positions
    if direction == "forward":
        horizontal += distance # simple if statements telling us to add or subtract the distance from either horizontal or depth depending on the direction command
    elif direction == "down":
        depth += distance
    else:
        depth -= distance
print(horizontal * depth)

# part 2
horizontal = 0
depth = 0
aim = 0 # reset all the positions, including aim this time
for instruction in instructions:
    direction, distance = instruction.split()
    distance = int(distance)
    if direction == "forward":
        horizontal += distance
        depth += (aim*distance) # pretty much the same thing as above, just updating our if statements to follow the new rules
    elif direction == "down":
        aim += distance
    else:
        aim -= distance
print(horizontal * depth)
# original solution
with open('input.txt') as f:
    lines = f.readlines() # return a list containing each line in the input file as a list item
    larger_depths = 0 # set the count we'll want to 0

# part one
for i in range(1, len(lines)): # for loop over the entire list, starting at 1
    if int(lines[i]) > int(lines[i-1]): # compare if the current list item is larger than the previous; had to convert to integer for comparison
        larger_depths += 1 # add 1 to the count
print(larger_depths) # print out the total count

# part two
larger_depths = 0 # reset the count
for i in range(len(lines)-3): # for loop over the entire list - 3
    lines_window1 = int(lines[i]) + int(lines[i+1]) + int(lines[i+2]) # defining what the windows are for comparison
    lines_window2 = int(lines[i+1]) + int(lines[i+2]) + int(lines[i+3])
    if lines_window2 > lines_window1: # similar to part 1, but comparing the windows this time
        larger_depths += 1
print(larger_depths)

# After thinking about it, there's a much easier way to do the comparison for part two
# Look at window1 and window 2. lines[i+1] and lines[i+2] overlap, so we can throw them out and just compare lines[i] and lines[i+3]
larger_depths = 0 # reset the count
for i in range(len(lines)-3): # for loop over the entire list - 3
    if int(lines[i+3]) > int(lines[i]): # similar to part 1, but comparing the windows this time
        larger_depths += 1
print(larger_depths)

# I think we can do this without for loops by using numpy's sum function and list slicing.
import numpy as np
lines = np.loadtxt('input.txt') # load data from text file so it can be used for np functions
print(np.sum(lines[1:] > lines[:-1])) # compare lines 1 to the end with lines 0 to end omitting the last one; this gives us a list of true or false statements, and we can count how many are true using sum
print(np.sum(lines[3:]> lines[:-3])) # compare lines 3 to the end with lines 0 to the end omitting the last three; same reasoning as above, and it works because of that overlap rule we found above
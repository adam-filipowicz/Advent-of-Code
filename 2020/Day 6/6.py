input = open('input.txt').read().strip('\n').split('\n\n')

# part one
count = 0
for group in input:
    for question in 'qwertyuiopasdfghjklzxcvbnm':
        if question in group:
            count += 1
print(count)

# part two
count = 0
for group in input:
    person = group.split('\n')
    answer = set(person[0])
    for i in range(1, len(person)):
        answer &= set(person[i])
    count += len(answer)
print(count)
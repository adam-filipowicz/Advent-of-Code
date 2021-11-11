# part 1
with open('input.txt') as geology: 
    print (sum([(l[(3*i) % (len(l)-1)] =='#') for i,l in enumerate(geology)]))
# part 2
with open('input.txt') as geology: 
    a = (sum([(l[(1*i) % (len(l)-1)] =='#') for i,l in enumerate(geology)]))
with open('input.txt') as geology:
    b = (sum([(l[(3*i) % (len(l)-1)] =='#') for i,l in enumerate(geology)]))
with open('input.txt') as geology:
    c = (sum([(l[(5*i) % (len(l)-1)] =='#') for i,l in enumerate(geology)]))
with open('input.txt') as geology:
    d = (sum([(l[(7*i) % (len(l)-1)] =='#') for i,l in enumerate(geology)]))
with open('input.txt') as geology:
    e = (sum([(l[(1*i) % (len(l)-1)] =='#') for i,l in enumerate(geology) if i % 2 != 1]))
print(a*b*c*d*e)
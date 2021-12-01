import re
from collections import defaultdict
import networkx as nx
from networkx.algorithms.shortest_paths.unweighted import predecessor

lines = [x.strip() for x in open('input.txt', 'r').readlines()]

bags = defaultdict(dict)
for l in lines:
    bag = re.match(r'(.*) bags contain', l).groups()[0]
    for count, b in re.findall(r'(\d+) (\w+ \w+) bag', l):
        bags[bag][b] = { 'weight': int(count)}

G = nx.DiGraph(bags)

def part1():
    RG = G.reverse()
    predecessors = nx.dfs_predecessors(RG, 'shiny gold')
    return len(predecessors)
print(part1())

def part2():
    def search(node):
        count = 1
        for n in G.neighbors(node):
            count += G[node][n]['weight'] * search(n)
        return count
    return search('shiny gold') - 1
print(part2())
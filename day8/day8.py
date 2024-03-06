import logging
import re
import math

logging.getLogger().setLevel(logging.DEBUG)

f = open("input.txt")
instr = f.readline().strip()
nodes = f.read().strip().splitlines()
f.close()
nodedict = {}
for node in nodes:
    nodedict[node[:3]] = node[7:15]

#traverse nodes with instructions
def p1traverse(startnode, endnode):
    currnode = startnode
    lastnode = endnode
    steps = 0
    idx = 0
    maxidx = len(instr)
    while currnode != lastnode:
        if idx >= maxidx:
            idx = 0
        if instr[idx] == "L":
            currnode = nodedict[currnode][:3]
            idx += 1
            steps += 1
        else:
            currnode = nodedict[currnode][5:]
            idx += 1
            steps += 1
    return steps

print("Nodes traversed, steps: %d" % p1traverse("AAA","ZZZ"))

def p2traverse():
    currnodes = [x for x in re.findall(r"(\w{2}A)", ','.join(list(nodedict.keys())))]
    lastnodes = [x for x in re.findall(r"(\w{2}Z)", ','.join(list(nodedict.keys())))]
    totalsteps = []
    for node in currnodes:
        currnode = node
        steps = 0
        idx = 0
        maxidx = len(instr)
        while currnode not in lastnodes:
            if idx >= maxidx:
                idx = 0
            if instr[idx] == "L":
                currnode = nodedict[currnode][:3]
                idx += 1
                steps += 1
            else:
                currnode = nodedict[currnode][5:]
                idx += 1
                steps += 1
        logging.debug("Total steps for node %s: %d" % (node, steps))
        totalsteps.append(steps)
    return math.lcm(*totalsteps)
    
print("Nodes traversed, steps: %d" % p2traverse())
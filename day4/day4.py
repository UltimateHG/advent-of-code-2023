import logging

# logging.getLogger().setLevel(logging.DEBUG)

def winner(line):
    cards = line.split(":")[1].split("|")
    for i in range(2):
        cards[i] = cards[i].split()
    logging.debug("Card pair: "+str(cards))
    matches = len(set(cards[0]) & set(cards[1]))
    logging.debug("%d matches found" % matches)
    if matches > 0:
        return 2**(matches-1)
    return 0

f = open("input.txt")
lines = f.readlines()
total = 0
for line in lines:
    total += winner(line)
    logging.info("Running total: %d" % total)

print("Total: %d" % total)
print("=====================\n\n")

########
#Part 2#
########

newlines = lines.copy()

#helper for "recursion"
def recurse(line):
    cards = line.split(":")[1].split("|")
    for i in range(2):
        cards[i] = cards[i].split()
    logging.debug("Card pair: "+str(cards))
    matches = len(set(cards[0]) & set(cards[1]))
    logging.debug("%d matches found" % matches)
    idx = lines.index(line)
    for i in range(matches):
        if idx+1+i < len(lines):
            newlines.append(lines[idx+1+i])

count = 0
while count < len(newlines):
    line = newlines[count]
    recurse(line)
    count += 1

print("Final length: %d" % count)
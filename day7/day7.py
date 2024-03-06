import logging
import re

# logging.getLogger().setLevel(logging.DEBUG)

f = open("input.txt")
lines = f.readlines()
hand_list = list()
for line in lines:
    spl = line.split()
    hand_list.append([spl[0], int(spl[1])])

pokerorder = "23456789TJQKA"
pokerorder2 = "J23456789TQKA"

#sort by 2 things: type of hand followed by ranking among same types
def sorttype(hand, joker=False):
    five, four, house, house2, three, two, one = r"(\w)\1{4}", r".*(\w)\1{3}.*", r"(\w)\1{2}(\w)\2", r"(\w)\1(\w)\2{2}", r".*(\w)\1{2}.*", r".*(\w)\1.*(\w)\2.*", r".*(\w)\1.*"
    sortedhand = sorted(hand, key = lambda elem: [pokerorder.index(c) for c in elem])
    sortedhand = ''.join(sortedhand)
    #handle for joker
    if joker:
        logging.debug("Sorted hand: %s" % sortedhand)
        #we will always form the best possible hand
        #if joker count is 5: 6
        #if joker count is 4: 6
        #if joker count is 3: one->6; else->5
        #if joker count is 2: three->6; one->5; else->3
        #if joker count is 1: four->6; three->5; two->4; one->3; else->1
        #if joker count is 0: handle normally (pass)
        match(hand.count("J")):
            case 5:
                return 6
            case 4:
                return 6
            case 3:
                if re.search(one, sortedhand.replace("J","")) != None: return 6
                return 5
            case 2:
                if re.search(three, sortedhand.replace("J","")) != None: return 6
                if re.search(one, sortedhand.replace("J","")) != None: return 5
                return 3
            case 1:
                if re.search(four, sortedhand.replace("J","")) != None: return 6
                if re.search(three, sortedhand.replace("J","")) != None: return 5
                if re.search(two, sortedhand.replace("J","")) != None: return 4
                if re.search(one, sortedhand.replace("J","")) != None: return 3
                return 1
            case 0:
                pass
    logging.debug("Sorted hand: %s" % sortedhand)
    #5 of a kind
    if re.search(five, sortedhand) != None: return 6
    #4 of a kind
    if re.search(four, sortedhand) != None: return 5
    #full house (2 cases possible)
    if (re.search(house, sortedhand) != None) or (re.search(house2, sortedhand) != None): return 4
    #3 of a kind
    if re.search(three, sortedhand) != None: return 3
    #2 pairs
    if re.search(two, sortedhand) != None: return 2
    #1 pair
    if re.search(one, sortedhand) != None: return 1
    #nothing matches, high card
    return 0

#sort magic
sortedlist = sorted(hand_list, key = lambda hand: (sorttype(hand[0]), [pokerorder.index(c) for c in hand[0]]))
logging.debug("Sorted list:\n%s" % sortedlist)
total = 0
#calculate values
for idx in range(len(sortedlist)):
    total += sortedlist[idx][1]*(idx+1)
    
print("Part 1 Total: %d\n===========" % total)

#sort magic second time
sortedlist2 = sorted(hand_list, key = lambda hand: (sorttype(hand[0], joker=True), [pokerorder2.index(c) for c in hand[0]]))
logging.debug("Sorted list:\n%s" % sortedlist2)
total = 0
#calculate values
for idx in range(len(sortedlist2)):
    total += sortedlist2[idx][1]*(idx+1)

print("Part 2 Total: %d" % total)
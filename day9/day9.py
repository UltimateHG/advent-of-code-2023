f = open("input.txt")
lines = f.readlines()
f.close()

def predictNext(initial, p2=False):
    numbers = [int(x) for x in initial.split()]
    diff = [numbers]
    ridx = 1
    while not diff[-1][-1] == 0 or len(diff) == 1:
        diff.append(list())
        for numidx in range(len(numbers)-1):
            diff[ridx].append(numbers[numidx+1]-numbers[numidx])
        numbers = diff[ridx]
        ridx += 1
    # go from top down
    if p2:
        nextdiff, nextnum = 0, 0
        for diffidx in range(len(diff)-1):
            nextnum = diff[-2-diffidx][0]
            nextnum -= nextdiff
            nextdiff = nextnum
        return nextnum
    # go from bottom up
    nextdiff, nextnum = 0, 0
    for diffidx in range(len(diff)-1):
        nextnum = diff[-2-diffidx][-1]
        nextnum += nextdiff
        nextdiff = nextnum
    return nextnum

total = 0
for line in lines:
    total += predictNext(line)
print("Part 1 total: %d" % total)

total = 0
for line in lines:
    total += predictNext(line, p2=True)
print("Part 2 total: %d" % total)
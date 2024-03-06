import logging

# logging.getLogger().setLevel(logging.DEBUG)

def processline(inp):
    minbag = {
        "red":0,
        "green":0,
        "blue":0
    }
    
    #split game number from sets
    spl = inp.split(":")
    game = spl[0]
    gameno = int(game.split()[-1])
    logging.info("Processing game %d" % gameno)
    spl = spl[1]
    
    #split into indiv sets
    spl = spl.split(";")
    
    #split each set into colours
    for i in range(len(spl)):
        spl[i] = spl[i].split(",")
    
    #split each colour into a pair
    for i in range(len(spl)):
        for j in range(len(spl[i])):
            spl[i][j] = spl[i][j].split()
    
    logging.info("Split colour: "+str(spl))
    
    #test against bag: if any single colour in any set exceeds, return game num, if not return 0
    for sets in spl:
        for colour in sets:
                key = colour[1]
                val = int(colour[0])
                if val > minbag.get(key):
                    logging.info("Minbag value %s:%d exceeded with %d" % (key,minbag.get(key),val))
                    minbag[key] = val
    
    retval = 1
    logging.info("Final minbag for game %d: %s", gameno, minbag)
    for i in minbag:
        retval *= minbag.get(i)
    return retval

f = open("input.txt")
lines = f.readlines()
total = 0
lineno = 1
for line in lines:
    total += processline(line)
    print("Processed game: %d" % lineno)
    lineno += 1
    print("Running total: %d" % total)
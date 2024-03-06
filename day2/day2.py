import logging

logging.getLogger().setLevel(logging.DEBUG)

bag = {
    "red":12,
    "green":13,
    "blue":14
}

def processline(inp):
    #split game number from sets
    spl = inp.split(":")
    game = spl[0]
    gameno = int(game.split()[-1])
    print("Processing game %d" % gameno)
    spl = spl[1]
    
    #split into indiv sets
    spl = spl.split(";")
    logging.info("Sets: "+str(spl))
    
    #split each set into colours
    for i in range(len(spl)):
        spl[i] = spl[i].split(",")
    
    logging.info("Split sets: "+str(spl))
    
    #split each colour into a pair
    for i in range(len(spl)):
        for j in range(len(spl[i])):
            spl[i][j] = spl[i][j].split()
    
    logging.info("Split colour: "+str(spl))
    
    #test against bag: if any single colour in any set exceeds, return game num, if not return 0
    for sets in spl:
        for colour in sets:
            if(int(colour[0]) > bag.get(colour[1])):
                print("Game %d not possible! %s:%d" % (gameno, colour[1], int(colour[0])))
                return 0
    
    #default case
    return gameno

f = open("input.txt")
lines = f.readlines()
total = 0
lineno = 0
for line in lines:
    total += processline(line)
    logging.info("Processed line: %d" % lineno)
    lineno += 1
    print("Running total: %d" % total)
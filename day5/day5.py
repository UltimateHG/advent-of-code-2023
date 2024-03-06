import logging

# logging.getLogger().setLevel(logging.INFO)

def createmap(text):
    spl = text.strip().split("\n")
    logging.debug("Split text: %s" % str(spl))
    newmap = {}
    for line in spl:
        elems = line.split()
        dest = int(elems[0])
        src = int(elems[1])
        rnge = int(elems[2])
        newmap[src] = (dest, rnge)
    logging.debug("Map created: %s" % newmap)
    return newmap

def traverse(start, maps):
    currnode = start
    count = 1
    for mp in maps:
        for key, elem in mp.items():
            logging.debug("Key elem pair: %s:%s" % (key, elem))
            if currnode < key:
                logging.debug("Currnode smaller than key, continuing")
                continue
            elif currnode > key+elem[1]:
                logging.debug("Currnode larger than key+elem, continuing")
                continue
            else:
                currnode = elem[0]+abs(currnode-key)
                logging.debug("Currnode updated: %d" % currnode)
                break
        logging.debug("map %d traversed, result = %d" % (count, currnode))
        count += 1
    logging.info("Final node reached: %d for seed %d" % (currnode, start))
    return currnode

f = open("input.txt")
filetext = f.read()
seeds = filetext.split("seed-to-soil map:")[0].split("seeds: ")[1].split()
map1text = filetext.split("soil-to-fertilizer map:")[0].split("seed-to-soil map:")[1]
map2text = filetext.split("fertilizer-to-water map:")[0].split("soil-to-fertilizer map:")[1]
map3text = filetext.split("water-to-light map:")[0].split("fertilizer-to-water map:")[1]
map4text = filetext.split("light-to-temperature map:")[0].split("water-to-light map:")[1]
map5text = filetext.split("temperature-to-humidity map:")[0].split("light-to-temperature map:")[1]
map6text = filetext.split("humidity-to-location map:")[0].split("temperature-to-humidity map:")[1]
map7text = filetext.split("humidity-to-location map:")[1]
f.close()

maps = [createmap(map1text), createmap(map2text), createmap(map3text), createmap(map4text), createmap(map5text), createmap(map6text), createmap(map7text)]

seedtravel = {}

for seed in seeds:
    seedtravel[int(seed)] = traverse(int(seed), maps)

print("Min ending location: %d" % min(seedtravel.values()))

# Func for splitting into categories
def split_cat(mp, idx, inputr):
    logging.info("split_cat called with idx %d\n======\n" % idx)
    cats = []
    base = inputr[0]
    inprange = inputr[1]
    #base case escape
    if idx >= len(mp):
        return [inputr]
    key = list(mp.keys())[idx]
    tup = list(mp.values())[idx]
    outrange = tup[1]
    maxstart = max(base, key)
    minend = min(base+inprange, key+outrange)
    logging.info("Maxstart: %d | Minend: %d\n======\n" % (maxstart, minend))
    #if any part of base+inrange intersects with input range
    if maxstart < minend:
        logging.info("Range exists")
        resultrange = (traverse(maxstart, [mp]), minend-maxstart)
        cats.append(resultrange)
        logging.info("Appended resultrange: %s" % cats)
        if maxstart > base:
            # handle below range
            belowrange = split_cat(mp, idx+1, (base, maxstart-base-1))
            cats.extend(belowrange)
            logging.info("Appended below range: %s" % cats)
        if base+inprange > key+outrange:
            # handle above range
            aboverange = split_cat(mp, idx+1, (key+outrange+1, base+inprange-key-outrange-1))
            cats.extend(aboverange)
            logging.info("Appended above range: %s" % cats)
    else:
        logging.info("Range does not exist\n======\n")
        return split_cat(mp, idx+1, inputr)
    logging.info("Returning final cats: %s\n======\n" % cats)
    return cats

def magic(startpair, maps):
    curr = [startpair]
    cats = []
    for mp in maps:
        for inputs in curr:
            cats.extend(split_cat(mp, 0, inputs))
        curr = cats.copy()
        cats = []
        logging.info("Map done, cats: %s" % curr)
    return curr

seedfinal = list()
# destlist = list()

# recursively call split_cat
for pair_idx in range(int(len(seeds)/2)):
    base = int(seeds[pair_idx*2])
    rnge = int(seeds[pair_idx*2+1])
    seedfinal.extend(magic([base, rnge-1], maps))

seedfinal = map(lambda x: x[0], seedfinal)
print("Min path is: %d" % min(seedfinal))
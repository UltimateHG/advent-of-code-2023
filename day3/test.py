f = open("input.txt")
lines = f.readlines()

retval = set()

for line in lines:
    retval = retval.union(set(list(line)))

temp = retval.copy()

for elem in temp:
    if elem.isdigit():
        retval.remove(elem)

print(retval)
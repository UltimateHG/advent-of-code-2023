import logging

logging.getLogger().setLevel(logging.INFO)

def eqn(t, d, x):
    logging.debug("Equation result: %d" % (t*x-x*x-d))
    return t*x-x*x-d > 0

f = open("input.txt")
lines = f.readlines()
ts = [int(x) for x in lines[0].strip("Time:").split()]
ds = [int(x) for x in lines[1].strip("Distance:").split()]
logging.debug("\nts: %s\nds: %s" % (ts, ds))
#form eqn then find all values of x that fits the equation
total = 1
for i in range(len(ts)):
    count = 0
    t = ts[i]
    d = ds[i]
    for x in range(t):
        if eqn(t,d,x): count += 1
    logging.info("Final count for t=%d and d=%d: %d" % (t,d,count))
    total *= count

print("Result: %d" % total)

t = int(''.join(lines[0].strip("Time:").split()))
d = int(''.join(lines[1].strip("Distance:").split()))
logging.debug("\nt: %s\nd: %s" % (t, d))
total = 0
for x in range(t):
    if eqn(t,d,x): total += 1
print("Result: %d" % total)
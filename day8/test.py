from collections import Counter
lastnodes = ['XDZ', 'JVZ', 'DDZ', 'THZ', 'SRZ', 'ZZZ']
currnodes = ['DDZ', 'XDZ', 'ZZZ', 'JVZ', 'THZ', 'SRZ']
lastnodecheck = Counter(lastnodes)
print(Counter(currnodes) == lastnodecheck)
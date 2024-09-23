from itertools import permutations
i = input()
r = []
for w in permutations(i):
    e = ''.join(w)
    e = e[:2]
    r.append(int(e))
r = [i for i in r if i >= 10]
print(min(r), max(r))


        

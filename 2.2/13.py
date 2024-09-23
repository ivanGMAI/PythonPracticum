i = (input())
f = (input())
d = (input())
t = [i[0], i[1], f[1], f[0], d[1], d[0]]
s = 0
for i in t:
    if s < t.count(i):
        s = t.count(i)
q = max([t.count(i) for i in t])
print(max([i for i in t if t.count(i) == q]))

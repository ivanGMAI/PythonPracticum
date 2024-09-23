p = int(input())
v = int(input())
t = int(input())
r = sorted([p, v, t])
if r[-1]**2 == r[0]**2 + r[1]**2:
    print('100%')
else:
    if r[-1]**2 > (r[0]**2 + r[1]**2):
        print('велика')
    elif r[0]**2 < r[1]**2 + r[2]**2:
        print('крайне мала')


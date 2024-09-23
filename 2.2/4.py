p = int(input())
v = int(input())
t = int(input())
r = [p, v, t]
rr = ['Петя', 'Вася', 'Толя']
print(f'1. {rr[r.index(max(r))]}')
print(f'2. {rr[r.index(sum(r) - max(r) - min(r))]}')
print(f'3. {rr[r.index(min(r))]}')

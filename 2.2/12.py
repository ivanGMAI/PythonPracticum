p = int(input())
v = int(input())
t = int(input())

if all([((p + v) > t), ((t + v) > p), ((p + t) > v)]):
	print('YES')
else:
	print('NO')

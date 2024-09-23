y = int(input())
a = [int(i) for i in range(0, 10000, 4)]
for i in a:
    if i % 100 == 0 and i % 400 != 0:
        a.remove(i)
if y in a:
    print('YES')
else:
    print('NO')


i = input()
i = [int(i[0]), int(i[1]), int(i[2])]
i = sorted(i)
if max(i) + min(i) == i[1] * 2:
    print('YES')
else:
    print('NO')

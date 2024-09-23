f = input()
e = input()
w = sorted([int(f[0]), int(f[1]), int(e[0]), int(e[1])])
if (w[2] + w[1]) < 10:
    print(str(max(w)) + str(w[2] + w[1]) + str(min(w)))
else:
    print(str(max(w)) + str(w[2] + w[1])[-1] + str(min(w)))

FILE_NAME = "data1.dat"
fi = open("./" + FILE_NAME, "r")
fo = open("./" + FILE_NAME.split(".")[0] + "1." + FILE_NAME.split(".")[1], "w")

inp = fi.readlines()

l = []

for line in inp:
    l.append(list(map(float, line.split())) if line[0] != '#' else [])

l = sorted(l[1:-1:1], key=lambda x: x[0])

s = 0

for i in l:
    s += i[1]

n = len(l)
s /= len(l)

frac_a = 0

for i in l:
    frac_a += (s - i[1])**2

ans = ( frac_a / (n - 1) / n ) ** 0.5

print(ans)

for i in (l):
    if len(i) == 2:
        fo.write(str(i[0]) + " " + str(i[1]) + " " + str(ans) + "\n")

fi.close()
fo.close()

name = 'IV3.csv'
outname = 'IV3_.csv'
texname = 'IV3tex.csv'

fin = open(name, 'r')
fout = open(outname, 'w')
ftex = open(texname, 'w')

data = fin.read()
data = data.split(',')

ans = ''
for i in range(len(data) - 1):
    ans += data[i] + '.'
ans += data[-1]

fout.write(ans)

data = ans.split(' ')

ans = ''
for i in range(len(data) - 1):
    ans += data[i] + ' & '
ans += data[-1]

data = ans.split('\n')
print(data)

ans = ''
for i in range(len(data) - 1):
    ans += data[i] + '\\\\ \\hline \n'

ftex.write(ans)

fin.close()
fout.close()

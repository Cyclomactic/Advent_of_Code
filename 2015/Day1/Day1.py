import linecache
INPUT = "./2015/Day1/input/input.txt"
a = linecache.getline(INPUT, 1)
opn = a.count('(')
cls = a.count(')')
floor = opn - cls
print('floor: ' + str(floor))

# part 2
b = ", ".join(a[i:i+1] for i in range(0, len(a), 1))
c = b[:-3]
d = "'" + c + "'"
res = eval(d)
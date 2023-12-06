import linecache
INPUT = "./2015/Day_1/input.txt"
a = linecache.getline(INPUT, 1)
print(a)
opn = a.count('(')
cls = a.count(')')
floor = opn - cls
print(floor)

# part 2
b = ", ".join(a[i:i+1] for i in range(0, len(a), 1))
c = b[:-3]
d = "'" + c + "'"
res = eval(d)
print(res)
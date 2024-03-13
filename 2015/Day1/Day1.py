import linecache
INPUT = "./2015/Day1/input/input.txt"
a = linecache.getline(INPUT, 1)

# part 1
opn = a.count('(')
cls = a.count(')')
floor = opn - cls
print('floor: ' + str(floor))

# part 2
floor = 0
position = 0
for char in a:
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
    position += 1
    print(f'position: {position}')
    if floor == -1:
        print(f'position: {position}')
        break

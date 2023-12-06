import re

file = open("1/text.txt", "r")
sample = file.readlines()
day_1 = []
for char in sample:
    first_num = re.search(r'[0-9]',char)
    last_num = re.search(r'(\d)(?!.*\d)',char)
    if first_num:
        elem = (first_num.group() + last_num.group())
        day_1.append(int(elem))
day_1_sum = sum(day_1)
print('sum = :' + str(day_1_sum))

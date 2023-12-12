from datetime import datetime


file_v = 'sample'
if file_v == 'sample':
    file = '2023/Day?/input/sample.txt'
else:
    file = '2023/Day?/input/text.txt'

def main():
    print(datetime.now())

start = datetime.now()
print(start)

main()

taken = datetime.now() - start
print('Time to finish: ' + str(taken))
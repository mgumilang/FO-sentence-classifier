import string
import os

with open("tes.txt", 'r+') as f:
    printable = set(string.printable)
    lines = []
    for l in f:
        l = list(filter(lambda x: x in printable, l))
        lines.append(''.join(l))

os.remove("TrainingData.txt")
with open("TrainingData.txt", 'w') as f:
    for line in lines:
        cindex = line.rfind(',')
        if cindex != -1:
            line = list(line)
            line[cindex] = '.'
            line = ''.join(line)
        f.write(line)

    print(len(lines))

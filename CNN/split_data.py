import os

with open("TrainingData.txt", 'r') as f:
    lines = f.readlines()

os.remove("pos_data.txt")
with open("pos_data.txt", 'w') as f:
    counter = 0
    for line in lines:
        line = line.split('.')
        label = line[1].strip()
        if (label == '1'):
            tmp = line[0] + '\n'
            f.write(tmp)
            counter += 1
    print(counter)

with open("neg_data.txt", 'w') as f:
    counter = 0
    for line in lines:
        line = line.split('.')
        label = line[1].strip()
        if (label == '0'):
            tmp = line[0] + '\n'
            f.write(tmp)
            counter += 1
    print(counter)

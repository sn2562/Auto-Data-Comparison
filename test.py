files = ['data/log1.txt','data/log2.txt']
table = {}
step = 0

def sourceProcessingStep(f):
    for line in open(f, 'r+'):
        line = line.rstrip().split('\t')
        key = tuple(line[0:4])
        if key not in table:
            table[key] = [[float(v) for v in line[4:]],[]]

def comparisonStep(f):
    for line in open(f, 'r+'):
        line = line.rstrip().split('\t')
        key = tuple(line[0:4])
        if key in table:
            table[key][1] = [float(v) for v in line[4:]]
        else:
            print('the columm does not match')

def printResilt():
    print('result')

if __name__ == "__main__":
    for f in files:
        print(f)
        if step == 0:
            sourceProcessingStep(f)
        elif step == 1:
            comparisonStep(f)

        step+=1
        print(table)

    printResilt()

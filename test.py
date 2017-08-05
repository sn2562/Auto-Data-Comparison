files = ['data/log1.txt','data/log2.txt']
table = {}
step = 0

for f in files:
    print(f)
    if step == 0:
        sourceProcessingStep(f)
    elif step == 1:
        comparisonStep(f)

    step+=1
    print(table)

def sourceProcessingStep(f):
    for line in open(f, 'r+'):
        line = line.rstrip().split('\t')
        key = tuple(line[0:4])
        if key not in table:
            table[key] = [line[5:],[]]

def comparisonStep(f):
    for line in open(f, 'r+'):
        line = line.rstrip().split('\t')
        key = tuple(line[0:4])
        if key not in table:
            table[key] = [line[5:],[]]

files = ['data/log1.tsv','data/log2.tsv']
color = {'OKBLUE':'\033[94m','OKGREEN':'\033[92m','WARNING':'\033[93m','FAIL':'\033[91m','ENDC':'\033[0m'}
table = {}

def sourceDataStep(f):
    for line in open(f, 'r+'):
        line = line.rstrip().split('\t')
        key = tuple(line[0:4])
        if key not in table:
            table[key] = [[float(v) for v in line[4:]],[]]

def comparisonDataStep(f):
    for line in open(f, 'r+'):
        line = line.rstrip().split('\t')
        key = tuple(line[0:4])
        if key in table:
            table[key][1] = [float(v) for v in line[4:]]
        else:
            print('the columm does not match')

def printResilt():
    print('== result =='+color['ENDC'])
    for col in table:
        print(col,end="\t")
        for i in range(0,len(table[col][0])):
            print(color['ENDC'],end="")
            print(table[col][0][i],end=" ")
            if table[col][0][i] >  table[col][1][i]:
                print(color['OKBLUE'],end="")
            elif table[col][0][i] <  table[col][1][i]:
                print(color['FAIL'],end="")
            else:
                print(color['ENDC'],end="")
            print(table[col][1][i],end="\t")
        print()

if __name__ == "__main__":
    step = 0
    for f in files:
        print(f)
        if step == 0:
            sourceDataStep(f)
        elif step == 1:
            comparisonDataStep(f)
        step+=1

    printResilt()

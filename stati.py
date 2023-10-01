def mean(x):
    sum=0
    co=0
    #for i in x:
    while co < len(x):
            x[co] = int(x[co])
            sum = sum + x[co]
            co = co + 1
    print(sum/(len(x)))

def median(x):
    x.sort()
    count=0
    for i in x:
        count = count + 1
    if count % 2 == 0:
        a1e = (count/2)-1
        a1e = int(a1e)
        a1 = int(x[a1e])
        a2 = int(x[a1e + 1])
        med = (a1 + a2) /2
        print(med)
    elif count % 2 != 0:
        n = int((count+1)/2)
        print(x[n])

def mode(x):
    mode_dic = {}
    count = 0
    for i in x:
        if i in mode_dic:
            mode_dic[i] += 1
        elif i not in mode_dic:
            mode_dic[i] = 1
    print(mode_dic)

 

 

file = open("mean-median-mode-frequency.csv", "r")
dataIn = file.read()
list1 = dataIn.split()
line = []
file.close()
count = 0
aux=0
for i in range(3):
        string = list1[i]
        aux =  []
        aux[:] = string
        while count < len(aux):
            if aux[count] != " " and aux[count] != "," and aux[count] != "\n":
                line.append(aux[count])
            count = count + 1    
        mean(line)
        median(line)
        mode(line)
        line = []

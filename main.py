def number(line):
    for i in line:
        print(i, " : " , str(line.index(i)))
number([0,1,2,7,3,5,7])
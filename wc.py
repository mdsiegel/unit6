#Matthew Siegel
#5/16/18
#wc.py - finding stuff about files

fileName = input('Enter a file name: ')
file = open(fileName)

def WordCount():
    count = 0
    file = file.strip()
    for line in file:
        count += len(line)
    print

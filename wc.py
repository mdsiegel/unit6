#Matthew Siegel
#5/16/18
#wc.py - finding stuff about files

fileName = input('Enter a file name: ')
file = open(fileName)


count = 0

for line in file:
    line = line.strip()
    count +=1
print('There are',count,'lines')

count3 = 0
for line in file:
    line = line.strip()
    lineList = line.split(' ')
    count3 += len(lineList)
print('There are',count3,'words')

count2 = 0

for line in file:
    line = line.strip()
    for word in line:
        for ch in word:
            count2+=1
print('There are',count2,'characters')


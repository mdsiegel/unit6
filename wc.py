#Matthew Siegel
#5/16/18
#wc.py - finding stuff about files

fileName = input('Enter a file name: ')
file = open(fileName)


count = 0

for line in file:
    line = line.strip()
    count +=1
print(count)


count2 = 0

for line in file:
    line = line.strip()
    for word in line:
        for ch in word:
            count2+=1
print(count2)


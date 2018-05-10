#Matthew Siegel
#5/10/18
#reverseFile.py - reversing the file

fileToOpen = input('What file do you want? ')
file = open(fileToOpen)
L = []
for line in file:
    L.append(line.strip())

for i in range(len(L)-1,-1,-1):
    print(L[i])


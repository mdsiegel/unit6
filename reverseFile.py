#Matthew Siegel
#5/10/18
#reverseFile.py - reversing the file

fileToOpen = input('What file do you want? ')
file = open(fileToOpen)

for line in file:
    print(line.strip())


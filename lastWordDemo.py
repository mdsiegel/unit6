#Matthew Siegel
#5/10/18
#lastWordDemo.py - print the last word of each line of a file

file = open('fileDemo.py')

for line in file:
    print(line.strip('\n'))
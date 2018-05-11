#Matthew Siegel
#5/9/18
#fileDemo.py - how to read a file

file = open('engmix.txt')


for line in file:
    if line[0] == 'm' and line[-2] == 's':
        print(line.strip())
    
    
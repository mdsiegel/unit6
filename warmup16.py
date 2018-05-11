#Matthew Siegel
#5/9/18
#fileDemo.py - how to read a file

file = open('engmix.txt')


for line in file:
    line_ = line.strip()
    if len(line_)>0:
        if line_[0] == 'm' and line_[-1] == 's':
            print(line_)
    
    
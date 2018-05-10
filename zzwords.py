#Matthew Siegel
#5/10/18
#zzwords.py - finds words with zz

file = open('engmix.txt')

for line in file:
    if 'zz' in line:
        print(line.strip())

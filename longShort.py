#Matthew Siegel
#5/11/18
#longShort.py - finding longest and shortest word of each letter

file = open('engmix.txt')

lShort = ['']*26
lLong = ['']*26
lAlph = ['']*26


alph = 'abcdefghijklmnopqrstuvwxyz'
    
    

for line in file:
    line = line.strip()
    if len(line) > 0:
        firstLetter = line[0]
        print(line)
        if line[0] not in alph:
            print(line[0])
        numLetter = alph.index(firstLetter)
        shortestWord = lShort[numLetter]
        longestWord = lLong[numLetter]
        if len(line) < len(shortestWord):
            lShort[numLetter] = line
        if len(line) > len(longestWord):
            lLong[numLetter] = line
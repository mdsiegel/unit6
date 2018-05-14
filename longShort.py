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
    firstLetter = line[0]
    numLetter = alph.index(line[0])
    shortestWord = lShort[numLetter]
    longest = lLong[numLetter]
    if len(line) < len(shortestWord):
        lShort[numLetter] = line
    if len(line) > len(longest):
        lLong[numLetter] = line
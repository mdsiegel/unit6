#Matthew Siegel
#5/11/18
#longShort.py - finding longest and shortest word of each letter

file = open('engmix.txt')

lShort = ['']*26
lLong = ['']*26


alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    

for line in file:
    line = line.strip()
    if len(line) >= 1 and line[0] != ' ':
        firstLetter = line[0]
        if line[0] not in alph:
            firstLetter = line[1]
        numLetter = alph.index(firstLetter)
        shortestWord = lShort[numLetter]
        longestWord = lLong[numLetter]
        if len(line) < len(shortestWord):
            print(line)
            lShort[numLetter] = line
        if len(line) > len(longestWord):
            lLong[numLetter] = line


print(lShort)
print(lLong)
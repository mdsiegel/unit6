#Matthew Siegel
#5/11/18
#longShort.py - finding longest and shortest word of each letter

file = open('engmix.txt')

data = {}
for ch in 'abcdefghijklmnopqrstuvwxyz':
    data[ch:'shortest'] = ''
    data[ch:'longest'] = ''

for line in file:
    line = line.strip()
    firstLetter = line[0]
    if len(line) < len(data[firstLetter:'shortest']):
        data[ch:'shortest'] = line
    if len(line) > len(data[firstLetter:'longest']):
        data[ch:'longest'] = line

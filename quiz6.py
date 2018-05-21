#Matthew Siegel
#5/21/18
#quiz6.py

file = open('engmix.txt')

#1
'''
letter = (input('Enter a letter: ')).lower()
for line in file:
    line = line.strip()
    if line.count(letter) == 4:
        print(line)
        
'''

#2
'''
for line in file:
    line = line.strip()
    if len(line) >= 9:
        if line[0] == line[4] and line[0] == line[8]:
            print(line)
            break
'''

'''
#3
letter = (input('Enter a letter: ')).lower()
num = int(input('Enter a number: '))
for line in file:
    line = line.strip()
    if len(line) > 0:
        if line[0] == letter and len(line) == num:
            print(line)
'''

#4
count = 0
for line in file:
    line = line.strip()
    if len(line) >= 10:
        count+=1
        if count == 8000:
            print(line)
            break

#5
totalCount = 0
word = ''
for line in file:
    count = 0
    line = line.strip()
    for ch in line:
        if ch in 'aeiou':
            count += 1
    if count > totalCount:
        totalCount = count
        line = word
print(word)
        
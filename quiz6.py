#Matthew Siegel
#5/21/18
#quiz6.py

file = open('engmix.txt')

#1
'''
letter = (input('Enter a letter: ')).lower()
for line in file:
    if line.count(letter) == 4:
        print(line)
        
'''

#2
'''
for line in file:
    if len(line) >= 9:
        if line[0] == line[4] and line[0] == line[8]:
            print(line)
            break
'''

#3
letter = (input('Enter a letter: ')).lower()
num = int(input
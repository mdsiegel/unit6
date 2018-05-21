#Matthew Siegel
#5/21/18
#quiz6.py

file = open('engmix.txt')

#1
letter = (input('Enter a letter: ')).lower()
for line in file:
    if line.count(letter) == 4:
        print(line)
#Matthew Siegel
#5/18/18
#anagram.py 

file = open('engmix.txt')
word = input('Enter a word: ')
letters = []
for ch in word:
    letters.append(ch)

for line in file:
    for l in letters:
        if l in line:
            print('line')
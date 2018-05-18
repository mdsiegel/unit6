#Matthew Siegel
#5/18/18
#anagram.py 

file = open('engmix.txt')
word = input('Enter a word: ')
letters = []
for ch in word:
    letters.append(ch)

for line in file:
    if letters in line:
        print(line)
        
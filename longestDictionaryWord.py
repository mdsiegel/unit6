#Matthew Siegel
#5/10/18
#longestDictionaryWord.py - finds longest word

file = open('engmix.txt')
count = 0
word = ''
for line in file:
    if len(line) > count:
        count = len(line)
        word = line
print(count)
print(word)
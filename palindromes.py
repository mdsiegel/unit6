#Matthew Siegel
#5/10/18
#palindromes.py - finding palindromes

file = open('engmix.txt')

for line in file:
    line = line.strip()
    word = ""
    for i in range(len(line)-1,-1,-1):
        word += line[i]
    if line == word:
        print(word)

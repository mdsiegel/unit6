#Matthew Siegel
#5/10/18
#palindromes.py - finding palindromes

file = open('engmix.txt')

for line in file:
    for ch in line:
        word2.append(word2[0])
        word2[0] = ch
        if word2 == line:
            print(line)

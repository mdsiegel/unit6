#Matthew Siegel
#5/10/18
#palindromes.py - finding palindromes

file = open('engmix.txt')

for line in file:
    word = ""
    for i in range(len(line),0,-1):
        word += line[i]
    if line ==- word:
        print(word)

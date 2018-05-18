#Matthew Siegel
#5/18/18
#anagram.py 

file = open('engmix.txt')
word = input('Enter a word: ')
letters = []
for ch in word:
    letters.append(ch)

length = len(letters)
for line in file:
    line = line.strip()
    for i in range(0,length+1):
        good = True
        if letters[i] not in line:
            good  = False
        if i == length + 1:
            if good == True:
                print(line)
        
#Matthew Siegel
#5/14/18
#HW6.py 

file = open('engmix.txt')

#1
word = input('Enter a word: ')
for line in file:
    if word in line.strip():
        print(line.strip())

    


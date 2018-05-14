#Matthew Siegel
#5/14/18
#HW6.py 

file = open('engmix.txt')

#1
"""
word = input('Enter a word: ')
for line in file:
    if word == line.strip():
        print('It is in the dictionary')
        """

#2
L = []
for line in file:
    L.append(line.strip())
num = int(input('Enter a number: '))
if num >= 0 and num <= len(L):
    print(L[num])
else:
    print('not in range')

    


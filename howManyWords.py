#Matthew Siegel
#5/10/18
#howManyWords.py - finds how many words

file = open('engmix.txt')

L = [0]*23
for line in file:
    L[len(line)] +=1

for i in range(0,L):
    print('There are',L[i], i, 'words')
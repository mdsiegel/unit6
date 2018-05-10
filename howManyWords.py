#Matthew Siegel
#5/10/18
#howManyWords.py - finds how many words

file = open('engmix.txt')

L = [0]*22
for line in file:
    L[len(line)] +=1
print(L)
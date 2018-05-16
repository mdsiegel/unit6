#Matthew Siegel
#5/16/18
#Hangman.py - hangman game

from ggame import *
from random import randint

black = Color(0x000000,1)
red = Color(0xFF0000,1)
blue = Color(0x0000FF,1)

file = open('engmix.txt')

def pickWord():
    L = []
    for line in file:
        L.append(line.strip())
    num = randint(1,len(L))
   # print(num)
    data["word"] = L[num]
    print(data["word"])
 #   print("pick word")
  #  print(data["word"])

def wordComplete():
    for ch in data["word"]:
            if ch not in data["guessed"]:
                return False
    return True
    
def printHangman():
    Sprite(head,(370,150))
    
    
def keyPress(event):
    if data["gameOver"] == False:
        if event.key not in data["guessed"]:
            data["guessed"] += event.key
      #  print(event.key)
            if event.key in data["word"]:
                for ch in data["word"]:
                    if event.key == ch:
                  #  print("yay")
                        for w in range(1,i):
                            if data[w] == event.key:
                          #  print(w)
                                addLetter(event.key, w)
                if wordComplete() == True:
             #   print("YOU WIN")
                    Sprite(winText,(330,250))
                    data["gameOver"] = True
                
            else:
                data["wrong"] += 1
                data["wrongLetters"] += " " + event.key
                lettersText = TextAsset(data["wrongLetters"],fill=black,style='bold 20pt Times')
                Sprite(lettersText,(800,250))
                if data["wrong"] == 1:
                    Sprite(head,(370,150))
                if data["wrong"] == 2:
                    Sprite(body,(400,210))
                if data["wrong"] == 3:
                    Sprite(leftLeg,(400,309))
                if data["wrong"] == 4:
                    Sprite(rightLeg,(340,309))
                if data["wrong"] == 5:
                    Sprite(leftArm,(400,250))
                if data["wrong"] == 6:
                    Sprite(rightArm,(330,250))
         #       print("YOU LOSE")
                    Sprite(loseText,(330,250))
                    data["gameOver"] = True
        else:
            print("Pick another letter, you already guessed that")
                    
                
                    
            
            
    
if __name__ == '__main__':
    data = {}
    data["guessed"] = ""
    data["wrong"] = 0
    data["word"] = ""
    data["wrongLetters"] = ""
    data["gameOver"] = False
    pickWord()
    i = 1
    for ch in data["word"]:
        data[i] = ch
        i += 1
    
    black = Color(0x000000,1)
    white = Color(0xFFFFFF,1)
    blackOutline = LineStyle(4,black) 
    baseLine = LineAsset(300, 0, blackOutline)
    vertLine = LineAsset(0, -300, blackOutline)
    topLine = LineAsset(100, 0, blackOutline)
    hangLine = LineAsset(0, 60, blackOutline)
    head = CircleAsset(30, blackOutline, white)
    body = LineAsset(0, -100, blackOutline)
    leftLeg = LineAsset(-60, -70, blackOutline)
    rightLeg = LineAsset(60, -70, blackOutline)
    leftArm = LineAsset(-70, -60, blackOutline)
    rightArm = LineAsset(70, -60, blackOutline)
    winText = TextAsset('YOU WIN!!!',fill=blue,style='bold 40pt Times')
    loseText = TextAsset('YOU LOSE',fill=red,style='bold 40pt Times')
    lettersText = TextAsset('',fill=black,style='bold 15pt Times')
    
    letterLine = LineAsset(60, 0, blackOutline)
    #Spriting all the compoenents of the hangman board
    Sprite(baseLine, (150,400))
    Sprite(vertLine, (300,100))
    Sprite(topLine, (300,100))  
    Sprite(hangLine, (400,100))


    for x in range(0,i-1):
        Sprite(letterLine, (300 + (x*100),500))
 #   print(data)
    def addLetter(letter, x):
        text = TextAsset(letter,fill=black,style='bold 40pt Times')
        Sprite(text, (300+((x-.85)*100),450))
    def keys():
        if data["gameOver"] == False:
            #Listening for any letter being pressed
            abc = "abcdefghijklmnopqrstuvwxyz"
            for ch in abc:
                App().listenKeyEvent('keydown',ch, keyPress)
  
            
        
    
    

    App().run(keys)
    
    
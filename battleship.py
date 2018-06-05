#Matthew Siegel
#5/23/18
#battleship.py

from ggame import *
from random import randint

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
white = Color(0xFFFFFF,1)

#Building the playing bards
def buildBoard():
    redrawAll()
    blackOutline = LineStyle(1,black) #pixels,color
    #Checking to see if someone has won yet and if the computer or player has then there is text to show it
    if data['ComCount'] == 4:
        Losetext = TextAsset('YOU LOSE',fill=red,style='bold 40pt Times')
        Sprite(Losetext, (400,400))
    if data['UserCount'] == 4:
        Wintext = TextAsset('YOU WIN',fill=blue,style='bold 40pt Times')
        Sprite(Wintext, (400,400))
    
    #Building the computer's board. Checking to see if any of the boxes were hit or are misses
    for r in range(0,5):
        for c in range(0,5):
            if board1[r][c] == 1:
                box = RectangleAsset(75,75,blackOutline,red)
            elif board1[r][c] == 3:
                box = RectangleAsset(75,75,blackOutline,blue)
            else:
                box = RectangleAsset(75,75,blackOutline,white)
            Sprite(box, (0+(75*r),0+(75*c)))
    #Building the user board. Checkig to see if there are any hits or misses, and where the ships are.
    for r in range(0,5):
        for c in range(0,5):
            if board2[r][c] == 1:
                box = RectangleAsset(75,75,blackOutline,red)
            elif board2[r][c] == 2:
                box = RectangleAsset(75,75,blackOutline,green)
            elif board2[r][c] == 3:
                box = RectangleAsset(75,75,blackOutline,blue)
            else:
                box = RectangleAsset(75,75,blackOutline,white)
            Sprite(box, (500+(75*r),0+(75*c)))

#Deleting the boards
def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()


#The computer is picking a ship at 4 random locations
def pickShips():
    for i in range(0,4):
        r1 = randint(0,4)
        r2 = randint(0,4)
        if board1[r1][r2] == 2:
            #Trying again if the ships are at the same spot
            r1 = randint(0,4)
            r2 = randint(0,4)
        board1[r1][r2] = 2
    print('Pick Ships')
    

#Called when you click the mouse. Figures out where on the board you clicked.
def mouseClick(event):
    x = event.x
    y = event.y
    #This is called if you are chosing where the ships go since you'll be clicking on the other board.
    if data['PickShips'] == True:
        r = (x-500)//75
        c = y//75
        board2[r][c] = 2
        buildBoard()
        data['ShipsPicked'] +=1
        if data['ShipsPicked'] == 4:
            data['PickShips'] = False
    else:
        r = x//75
        c = y//75
        if r < 5 and c < 5 and r >= 0 and c >= 0:
            if board1[r][c] == 2:
                board1[r][c] = 1
                data['UserCount'] += 1
                buildBoard()
            elif board1[r][c] == 0:
                board1[r][c] = 3
                buildBoard()
            computerTurn()

#Computer chosing spots to guess. 
def computerTurn():
    ran1 = randint(0,4)
    ran2 = randint(0,4)
    if board2[ran1][ran2] == 1 or board2[ran1][ran2] == 3:
        computerTurn()
    if board2[ran1][ran2] == 2:
        board2[ran1][ran2] = 1
        data['ComCount'] += 1
        buildBoard()
    if board2[ran1][ran2] == 0:
        board2[ran1][ran2] = 3
        buildBoard()

                


if __name__ == '__main__':
    data = {}
    data['PickShips'] = True
    data['ShipsPicked'] = 0
    data['ComCount'] = 0
    data['UserCount'] = 0
    board1 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    board2 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    instruction = TextAsset('Matthew',fill=blue,style='bold 40pt Times')
    pickShips()
    buildBoard()
    App().listenMouseEvent('click', mouseClick)
    App().run()
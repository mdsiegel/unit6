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

def buildBoard():
    blackOutline = LineStyle(1,black) #pixels,color
    for r in range(0,5):
        for c in range(0,5):
            if board1[r][c] == 1:
                box = RectangleAsset(75,75,blackOutline,red)
            else:
                box = RectangleAsset(75,75,blackOutline,white)
            Sprite(box, (0+(75*r),0+(75*c)))
    for r in range(0,5):
        for c in range(0,5):
            if board2[r][c] == 1:
                box = RectangleAsset(75,75,blackOutline,red)
            else:
                box = RectangleAsset(75,75,blackOutline,white)
            Sprite(box, (500+(75*r),0+(75*c)))

def findBox(clickx,clicky):
    boxLength = 75
    boxHeight = 75
    for r in range(0,5):
        for c in range(0,5):
            if clickx > 75*r and clickx < 75*(r+1) and clicky > 75*c and clicky < 75*(c+1):
                return (r,c)
    if data['PickShips'] == True:
        for r in range(0,5):
            for c in range(0,5):
                if clickx > 500+(75*r) and clickx < 500+(75*(r+1)) and clicky > 75*c and clicky < 75*(c+1):
                    return (r,c)

def pickShips():
    for i in range(0,4):
        r1 = randint(0,4)
        r2 = randint(0,4)
        board1[r1][r2] = 2
    print('Pick Ships')
    
def mouseClick(event):
    x = event.x
    y = event.y
    if data['PickShips'] == True:
        (r,c) = findBox(x,y)
        board2[r][c] = 2
        print(board2)
        data['ShipsPicked'] +=1
        if data['ShipsPicked'] == 4:
            data['PickShips'] = False
    else:
        (r,c) = findBox(x,y)
        if board1[r][c] == 2:
            print('got it')
            board1[r][c] = 1
            buildBoard()
        print(board1)
        computerTurn()

def computerTurn():
    ran1 = randint(0,4)
    ran2 = randint(0,4)
    if board2[ran1][ran2] == 1 or board2[ran1][ran2] == 3:
        computerTurn()
    if board2[ran1][ran2] == 2:
        print('gotcha')
        board2[ran1][ran2] = 1
        data['ComCount'] += 1
        if data['ComCount'] == 4:
            print('You lose')
        buildBoard()
    if board2[ran1][ran2] == 0:
        board2[ran1][ran2] = 3

                


if __name__ == '__main__':
    data = {}
    data['PickShips'] = True
    data['ShipsPicked'] = 0
    data['ComCount'] = 0
    data['UserCount'] = 0
    board1 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    board2 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    pickShips()
    buildBoard()
    App().listenMouseEvent('click', mouseClick)
    App().run()
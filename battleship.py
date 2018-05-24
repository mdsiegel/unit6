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
    for r in range(0,4):
        for c in range(0,4):
            if board1[r][c] == 1:
                box = RectangleAsset(100,100,blackOutline,red)
            else:
                box = RectangleAsset(100,100,blackOutline,white)
            Sprite(box, (0+(100*r),0+(100*c)))
    for r in range(0,4):
        for c in range(0,4):
            box = RectangleAsset(100,100,blackOutline,white)
            Sprite(box, (500+(100*r),0+(100*c)))

def findBox(clickx,clicky):
    boxLength = 100
    boxHeight = 100
    for r in range(0,4):
        for c in range(0,4):
            if clickx > 100*r and clickx < 100*(r+1) and clicky > 100*c and clicky < 100*(c+1):
                return (r,c)
    if data['PickShips'] == True:
        for r in range(0,4):
            for c in range(0,4):
                if clickx > 500+(100*r) and clickx < 500+(100*(r+1)) and clicky > 100*c and clicky < 100*(c+1):
                    return (r,c)

def pickShips():
    for i in range(0,3):
        r1 = randint(0,3)
        r2 = randint(0,3)
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
        if data['ShipsPicked'] == 3:
            data['PickShips'] = False
        


if __name__ == '__main__':
    data = {}
    data['PickShips'] = True
    data['ShipsPicked'] = 0
    board1 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    board2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    pickShips()
    buildBoard()
    App().listenMouseEvent('click', mouseClick)
    App().run()
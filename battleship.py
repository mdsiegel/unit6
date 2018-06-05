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
    redrawAll()
    blackOutline = LineStyle(1,black) #pixels,color
    if data['ComCount'] == 4:
        print('You lose')
    if data['UserCount'] == 4:
        print('You win')
        
    for r in range(0,5):
        for c in range(0,5):
            if board1[r][c] == 1:
                box = RectangleAsset(75,75,blackOutline,red)
            elif board1[r][c] == 3:
                box = RectangleAsset(75,75,blackOutline,blue)
            else:
                box = RectangleAsset(75,75,blackOutline,white)
            Sprite(box, (0+(75*r),0+(75*c)))
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

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()


def pickShips():
    for i in range(0,4):
        r1 = randint(0,4)
        r2 = randint(0,4)
        if board1[r1][r2] == 2:
            print('did it')
            r1 = randint(0,4)
            r2 = randint(0,4)
        board1[r1][r2] = 2
    print('Pick Ships')
    
def mouseClick(event):
    x = event.x
    y = event.y
    if data['PickShips'] == True:
        r = (x-500)//75
        c = y//75
        board2[r][c] = 2
        buildBoard()
        print(board2)
        data['ShipsPicked'] +=1
        if data['ShipsPicked'] == 4:
            data['PickShips'] = False
    else:
        r = x//75
        c = y//75
        if r < 5 and c < 5 and r >= 0 and c >= 0:
            if board1[r][c] == 2:
                print('got it')
                board1[r][c] = 1
                data['UserCount'] += 1
                if data['UserCount'] == 4:
                    print('You win')
                buildBoard()
            elif board1[r][c] == 0:
                board1[r][c] = 3
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
        buildBoard()

                


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
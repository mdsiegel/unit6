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
            if board1[r][c] == 2:
                box = RectangleAsset(100,100,blackOutline,red)
            else:
                box = RectangleAsset(100,100,blackOutline,white)
            Sprite(box, (0+(100*r),0+(100*c)))
    for r in range(0,4):
        for c in range(0,4):
            box = RectangleAsset(100,100,blackOutline,white)
            Sprite(box, (500+(100*r),0+(100*c)))

def pickShips():
    for i in range(0,3):
        randint1 = randint(1,4)
        randint2 = randint(1,4)
        board2[randint1][randint2] = 2


if __name__ == '__main__':
    board1 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    board2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    buildBoard()
    pickShips()
    App().run()
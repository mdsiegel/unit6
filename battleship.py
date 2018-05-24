#Matthew Siegel
#5/23/18
#battleship.py

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
white = Color(0xFFFFFF,1)


def buildBoard():
    blackOutline = LineStyle(1,black) #pixels,color
    board1 = [[0,0,0],[0,0,0],[0,0,0]]
    for r in range(0,4):
        for c in range(0,4):
            box = RectangleAsset(100,100,blackOutline,white)
            Sprite(box, (0+(100*r),0+(100*c)))


if __name__ == '__main__':
    buildBoard()
    App().run()
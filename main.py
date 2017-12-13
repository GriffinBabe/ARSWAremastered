import pygame as pg
from Input import Listener

#Initialisation & fps settings
pg.init()
FPS = 60
fpsClock = pg.time.Clock()

#Window setup & settings
DISPLAY = pg.display.set_mode((1200,800),0,32)
pg.display.set_caption('ARSWA 2')

#Input listener
listener = Listener("null")

#FontSettings
fontObj = pg.font.SysFont('freesansbold.tff',32)


def main():

    frameCount = 0

    #Main Loop
    while True:

        for event in pg.event.get():
            if event.type == "QUIT":
                pg.quit()

        listener.listen()

        pg.display.update()
        frameCount += 1
        fpsClock.tick(FPS)


#Call main
#main()
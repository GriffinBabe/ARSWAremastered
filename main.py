import pygame as pg
from Input import Listener
from net import Session
from Player import Player

#Initialisation & fps settings
pg.init()
FPS = 60
fpsClock = pg.time.Clock()

#Window setup & settings
DISPLAY = pg.display.set_mode((1280,960),0,32) #1280 and 960 lets 20x15 64x64 tiles
pg.display.set_caption('ARSWA 2')



#Game elements
player = Player()
collidables = [] #List containing collidable elements
renderables = [] #List containing renderable elements
collidables.append(player)
renderables.append(player)


#Input listener
listener = Listener(player=player)

#FontSettings
fontObj = pg.font.SysFont('freesansbold.tff',32)


def main():

    frameCount = 0

    #Main Loop
    while True:

        for event in pg.event.get():
            if event.type == "QUIT":
                pg.quit()

        listener.listen() #Takes the pressed keys and acts about it
        player.updatePos(None)

        #Renders every game element
        DISPLAY.fill(pg.Color(0,0,0)) #Covers the screen in black
        for renderable in renderables:
            renderable.render(DISPLAY)

        pg.display.update()

        frameCount += 1
        fpsClock.tick(FPS)


#Call main
main()

"""
serveraddress = ('localhost',2055)
session = Session(serveraddress)
session.run()
session.csend('Message...')
"""
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
players = [] #List of different players
collidables = [] #List containing collidable elements
username = input("Username: ")
player = Player(username)
players.append(player)
collidables.append(player)


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
        player.updatePos(collidables)

        #Just info
        """if frameCount % 60 == 0:
            for pl in players:
                print(pl.username+" "+str(pl.x)+" "+str(pl.y)+" "+str(pl.dx)+" "+str(pl.dy)+" "+
                      str(pl.direction))
        """
        #Sets the renderables
        renderables = []
        for p in players:
            if p.online:
                renderables.append(p)
        #Renders every game element
        DISPLAY.fill(pg.Color(0,0,0)) #Covers the screen in black
        for renderable in renderables:
            renderable.render(DISPLAY)

        pg.display.update()

        frameCount += 1
        fpsClock.tick(FPS)


#Main call

serveraddress = ('localhost',2055)
session = Session(serveraddress,players,player)
player.setsession(session)
session.start()
connectionstring = "CO-"+player.username+"-"+player.team+"-"+"Warrior"+"-"+str(player.x)+"-"+str(player.y)
connectionpacket = connectionstring.encode("utf-8")
session.send(connectionpacket)

main()


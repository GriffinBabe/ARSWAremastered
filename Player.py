import pygame as pg

class Player:

    def __init__(self):
        """Player constructor, x and y are screen and game positions, vx is
         actual speed in X, vy is actual speed in Y, width and height..."""
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.width = 64
        self.height = 64
        self.direction = 0 #0 in Front 1 in right and -1 in left
        self.character = Warrior()


    def updatePos(self,collidables):
        oldX = self.x
        oldY = self.y

        if self.direction == 1:
            if self.dx + self.character.acceleration > self.character.maxspeed:
                self.dx = self.character.maxspeed
            else:
                self.dx += self.character.acceleration

        elif self.direction == -1:
            if self.dx - self.character.acceleration < -self.character.maxspeed:
                self.dx = -self.character.maxspeed
            else:
                self.dx -= self.character.acceleration

        else: #Freins until it reaches 0
            if self.dx > 0:
                self.dx -= self.character.acceleration
                if self.dx < 0:
                    self.dx = 0
            if self.dx < 0:
                self.dx += self.character.acceleration
                if self.dx > 0:
                    self.dx = 0

        self.x += self.dx
        self.y += self.dy

        if self.collisionX(collidables):
            self.x = oldX
            self.dx = 0

    def collisionX(self,collidables):
        #TODO: Finish the collision with collidable items.
        if self.x < 0 or self.x > 1200 or self.y < 0 or self.y > 800:
            return True
        return False

    def render(self,DISPLAY):
        """Renders the player, kinda an java interface"""
        if self.direction == 0:
            DISPLAY.blit(self.character.imageFront,(self.x,self.y))
        elif self.direction == 1:
            DISPLAY.blit(self.character.imageRight,(self.x,self.y))
        elif self.direction == -1:
            DISPLAY.blit(self.character.imageLeft,(self.x,self.y))




class Warrior:

    def __init__(self):
        self.maxspeed = 400/60
        self.acceleration = 40/60
        self.imageFront = pg.image.load("warriorFront.png")
        self.imageLeft = pg.image.load("warriorLeft.png")
        self.imageRight = pg.image.load("warriorRight.png")

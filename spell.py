import pygame as pg

class Hitbox:

    def __init__(self,type,range,offx,offy): #offx and offy is a shift compared to the player top left
        self.offx = offx
        self.offy = offy
        self.range = range
        if type == "Ball":
            self.image = pg.image.load("hitboxBall"+range+".png")



class Warriorbasic:

    def __init__(self,player):
        self.damage = 20
        self.cooldown = 0
        self.cooldownmax = 60
        self.duration = 15
        self.hitboxes = []
        self.hitboxes.append(Hitbox("Ball",16,64+16+10,32))
        self.image = pg.image.load()

    def act(self):
        if self.cooldown == 0:
            self.cooldown == self.cooldownmax
            


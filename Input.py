import pygame as pg

class Listener():

    def __init__(self,player):
        self.player=player

    def listen(self):
        keys = pg.key.get_pressed()
        direction = 0  #0 null 1 is right -1 is left

        if keys[pg.K_RIGHT]:
            if not keys[pg.K_LEFT]:
                direction = 1
        if keys[pg.K_LEFT]:
            if not keys[pg.K_RIGHT]:
                direction = -1

        self.player.direction = direction


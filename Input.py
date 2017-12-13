import pygame as pg

class Listener():

    def __init__(self,player):
        self.player=player

    def listen(self):
        keys = pg.key.get_pressed()
        print(keys)
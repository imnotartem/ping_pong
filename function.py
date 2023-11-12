from data import *

class Board(pygame.Rect):
    def __init__(self, x, y, width, height, speed= setting_board['SPEED'], color= (0,0,220), name= None ):
        super().__init__(x, y, width, height)
        self.SPEED = speed
        self.COLOR = color
        self.NAME = name
        self.SCORE = 0
        self.MOVE = {'UP': False, 'DOWN': False}

    def move(self, window):
        if self.MOVE['UP'] and self.y > 0:
            self.y -= self.SPEED
        if self.MOVE['DOWN'] and self.bottom < setting_win['HEIGHT']:
            self.y += self.SPEED
        pygame.draw.rect(window, self.COLOR, self)
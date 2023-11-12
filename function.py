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

class Ball():
    def __init__(self, x, y, radius, color= [100,200,123], speed = setting_ball['SPEED']):
        self.X = x
        self.Y = y
        self.RADIUS = radius
        self.COLOR = color
        self.SPEED = speed
        self.SPEED_X = self.SPEED
        self.SPEED_Y = 0

    def move(self, window, board_left, board_right):
        pass


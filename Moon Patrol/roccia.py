from random import randint
from actor import Actor

class Roccia(Actor) :
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._dx = 8

    def move(self,xP,yP):

        if self._x < 0 :
            self._x = randint(200,700)
        else :
            self._x -= self._dx

        for i in range(20) :
            if (xP == self._x + i or xP + i == self._x) :
                    self._x = 800

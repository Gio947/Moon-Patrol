from random import randint
from actor import Actor

class Buca(Actor) :
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._dx = 8

    def move(self):
        self._x -= self._dx

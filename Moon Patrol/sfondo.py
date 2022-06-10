from actor import Actor

class Sfondo(Actor) :

    def __init__(self,x,y):
        self._x = x
        self._y = y
        self._dx = 8
        self._dy = 8

    def move(self):

        if self._x < -220 :
            self._x , self._y = 2,2

        self._x += self._dx

    def go_left(self):
        self._dx, self._dy = -5, 0

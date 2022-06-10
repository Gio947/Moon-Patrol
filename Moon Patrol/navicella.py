from random import randint
from actor import Actor

class Navicella(Actor) :
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._dx = 6
        self._dy = 6

    def move(self,xP,yP):
       posizione = randint(0,1)
       esito = 0

       for i in range(30):
           if (self._x == xP + i or self._x == xP - i):
               if (self._y == yP + i or self._y == yP - i):
                   esito = 1

       if esito != 1 :
           if self._x > 0 and self._x < 700 :
               if posizione == 0 :
                    self._x += 5
                    #self._y -= 5
               if posizione == 1:
                   self._x -= 5
                   #self._y -= 5
           else :
               self._x = 120
       else :
           self._y = 900

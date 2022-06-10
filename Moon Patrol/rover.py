from actor import Actor

class Rover(Actor) :
    def __init__(self, x, y):
        self._punteggio = 0
        self._jump = 0
        self._x = x
        self._y = y
        self._dy = 1

    def collide(self,xP,yP,rangeInt):
        esito = 0

        for i in range(rangeInt):
            if (self._x == xP + i or self._x == xP - i) :
                if (self._y == yP + i or self._y == yP - i) :
                    esito = 1

        return esito

    def punteggio(self):
        return self._punteggio

    def setPunteggio(self, val):
        self._punteggio = val

    def getJump(self):
        return self._jump

    def setJump(self,val):
        self._jump = val

    def go_up(self):
        self._y -= 5
        self._jump = 1

    def go_down(self):
        self._y += 5
        self._jump = -1

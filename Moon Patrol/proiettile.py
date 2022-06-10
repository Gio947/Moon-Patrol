from actor import Actor

class Proiettile(Actor) :
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._dx = 8
        self._dy = 8

    def move(self,num):
        if num == 1 :
            self._x += 5
        if num == 2 :
            self._y -= 5
        if num == 3 :
            if self._y > 450 :
                self._y = 70

            self._y += 5

class Actor :
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._dx = 6
        self._dy = 6

    def move(self):
        raise NotImplementedError("Abstract method")

    def collide(self):
        raise NotImplementedError("Abstract method")

    def setPosizione(self, x, y):
        self._x = x
        self._y = y

    def posizione(self):
        return self._x, self._y
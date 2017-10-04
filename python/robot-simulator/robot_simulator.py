NORTH = 0
EAST  = 1
SOUTH = 2
WEST  = 3

movements = { NORTH: (0,1),
              EAST : (1,0),
              SOUTH: (0,-1),
              WEST : (-1,0) }

class Robot(object):
    def __init__(self, direction = NORTH, startx = 0, starty = 0):
        self.bearing = direction
        self.x = startx
        self.y = starty
        self.actions = { 'L': self.turn_left,
                         'R': self.turn_right,
                         'A': self.advance }

    @property
    def coordinates(self):
        return (self.x, self.y)

    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4

    def turn_left(self):
        self.bearing = (self.bearing - 1) % 4

    def advance(self):
        self.x += movements[self.bearing][0]
        self.y += movements[self.bearing][1]

    def simulate(self, str):
        for i in str:
            self.actions[i]()

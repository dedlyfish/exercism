NORTH = 1
EAST  = 2
SOUTH = 3
WEST  = 4

class Robot(object):
    def __init__(self, direction = NORTH, startx = 0, starty = 0):
        self.bearing = direction
        self.coordinates = (startx, starty)

    def turn_right(self):
        if self.bearing == WEST:
            self.bearing = NORTH
        else:
            self.bearing += 1

    def turn_left(self):
        if self.bearing == NORTH:
            self.bearing = WEST
        else:
            self.bearing -= 1

    def advance(self):
        if self.bearing == NORTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
        if self.bearing == SOUTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1] - 1)
        if self.bearing == EAST:
            self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])
        if self.bearing == WEST:
            self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])

    def simulate(self, actions):
        for i in actions:
            if i == 'L':
                self.turn_left()
            if i == 'R':
                self.turn_right()
            if i == 'A':
                self.advance()

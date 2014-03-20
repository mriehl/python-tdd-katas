import enum
import operator


class Orientation(enum.Enum):
    North = ("N", (0, 1))
    South = ("S", (0, -1))
    East = ("E", (1, 0))
    West = ("W", (-1, 0))


class Move(enum.Enum):
    FORWARD = operator.add
    BACKWARD = operator.sub

class Turn(enum.Enum):
    LEFT = 1

class Rover(object):

    def __init__(self, position=(0, 0), orientation=Orientation.North):
        self.position = position
        self.orientation = orientation

    def move(self, move):
        self.position = tuple(
            map(
                move.value,
                self.position,
                self.delta_vector_for_current_orientation
            )
        )

    def turn(self, turn):
        if self.orientation == Orientation.North:
            self.orientation = Orientation.West
        elif self.orientation == Orientation.West:
            self.orientation = Orientation.South
        elif self.orientation == Orientation.South:
            self.orientation = Orientation.East
        elif self.orientation == Orientation.East:
            self.orientation = Orientation.North



    @property
    def delta_vector_for_current_orientation(self):
        return self.orientation.value[1]

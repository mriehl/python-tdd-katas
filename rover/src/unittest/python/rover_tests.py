import unittest

from rover import Rover, Move, Turn
from rover import Orientation


class RoverTests(unittest.TestCase):

    def test_should_create_new_rover_with_default_coordinates(self):
        r = Rover()

        self.assertEquals(r.position, (0, 0))

    def test_should_create_new_rover_with_default_direction(self):
        r = Rover()

        self.assertEquals(r.orientation, Orientation.North)

    def test_should_create_new_rover_with_given_coordinates(self):
        r = Rover((1, 2))

        self.assertEquals(r.position, (1, 2))

    def test_should_create_new_rover_with_given_coordinates_and_direction(self):
        r = Rover((1, 2), orientation=Orientation.South)

        self.assertEquals(r.position, (1, 2))
        self.assertEquals(r.orientation, Orientation.South)

    def test_should_be_able_to_move_one_forward(self):
        r = Rover()

        r.move(Move.FORWARD)
        self.assertEquals(r.position, (0, 1))

    def test_should_be_able_to_move_one_backward(self):
        r = Rover((1, 2))

        r.move(Move.BACKWARD)
        self.assertEquals(r.position, (1, 1))

    def test_should_be_able_to_move_left(self):
        r = Rover(orientation=Orientation.North)

        r.turn(Turn.LEFT)
        self.assertEquals(r.orientation, Orientation.West, msg=None)

    def test_should_be_able_to_turn_around(self):
        r = Rover(orientation=Orientation.North)

        r.turn(Turn.LEFT)
        r.turn(Turn.LEFT)
        r.turn(Turn.LEFT)
        r.turn(Turn.LEFT)
        self.assertEquals(r.orientation, Orientation.North)


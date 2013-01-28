"""
Classes to fulfill the roles of those described at
    http://doc.sikuli.org/location.html
"""
from .sikuli_class import ClientSikuliClass
from .misc import (constructor,
                   return_from_remote,
                   run_on_remote)
from .asserts import (assert_positive_int, assert_int)

__author__ = 'Alistair Broomhead'


class Location(ClientSikuliClass):
    """
    Manages interaction with Sikuli's Location, reflecting
    http://doc.sikuli.org/location.html#Location
    """
    @run_on_remote
    def getX(self):
        """
        Get the respective attribute of the location.

        :rtype: int
        """
        pass

    @getX.post
    def getX(self, r_float):
        """
        Get the respective attribute of the location.

        :param r_float: float
        :rtype: int
        """
        return int(r_float)

    @run_on_remote
    def getY(self):
        """
        Get the respective attribute of the location.

        :rtype: int
        """
        pass

    @getY.post
    def getY(self, r_float):
        """
        Get the respective attribute of the location.

        :param r_float: float
        :rtype: int
        """
        return int(r_float)

    @run_on_remote
    def setLocation(self, x, y):
        """
        Set the location of this object to the specified coordinates.

        :param x: int > 0
        :param y: int > 0
        """
        assert_positive_int(x, self.setLocation)
        assert_positive_int(y, self.setLocation)

    @return_from_remote('Location')
    def offset(self, dx, dy):
        """
        Get a new location which is dx and dy pixels away horizontally and
        vertically from the current location.

        :param dx: int
        :param dy: int
        :rtype: Location
        """
        assert_int(dx, self.offset)
        assert_int(dy, self.offset)

    @run_on_remote
    def above(self, dy):
        """
        Get a new location which is dy pixels vertically above the current
        location.

        :rtype: int
        :param dy: int > 0
        """
        assert_positive_int(dy, self.above)

    @run_on_remote
    def below(self, dy):
        """
        Get a new location which is dy pixels vertically below the current
        location.

        :rtype: int
        :param dy: int > 0
        """
        assert_positive_int(dy, self.below)

    @run_on_remote
    def left(self, dx):
        """
        Get a new location which is dx pixels horizontally to the left of the
        current location.

        :rtype: int
        :param dx: int > 0
        """
        assert_positive_int(dx, self.left)

    @run_on_remote
    def right(self, dx):
        """
        Get a new location which is dx pixels horizontally to the right of the
        current location.

        :rtype: int
        :param dx: int > 0
        """
        assert_positive_int(dx, self.right)

@constructor(Location)
def _location_constructor(x, y):
    return "Sikuli.Location(%r, %r)" % (x, y)

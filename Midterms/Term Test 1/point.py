"""
point module
"""
from typing import Any


class Point:
    """ Represent a two-dimensional point

    x - horizontal position
    y - vertical position
    """
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        """ Initialize a new point
        """
        self.x, self.y = float(x), float(y)

    def __eq__(self, other: Any) -> bool:
        """ Return whether self is equivalent to other.

        >>> Point(3, 5) == Point(3.0, 5.0)
        True
        >>> Point(3, 5) == Point(5, 3)
        False
        >>> Point(3, 5) == 7
        False
        """
        return (type(self) == type(other)
                and self.x == other.x
                and self.y == other.y)

    def __str__(self) -> str:
        """ Return a string representation of self

        >>> print(Point(3, 5))
        (3.0, 5.0)
        """
        return "({}, {})".format(self.x, self.y)

    def __repr__(self) -> str:
        """
        Return a string that would evaluate to a Point equivalent to self.

        >>> Point(3, 4).__repr__()
        'Point(3.0, 4.0)'
        """
        return "Point({}, {})".format(self.x, self.y)

    def distance_to(self, other: 'Point') -> float:
        """
        Return distance from self to other.

        >>> Point(1, 2).distance_to(Point(4, 6))
        5.0
        """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def distance_from_origin(self) -> float:
        """ Return the distance from the origin of this point

        >>> Point(3, 4).distance_from_origin()
        5.0
        """
        return self.distance_to(Point(0, 0))

    def __add__(self, other: 'Point') -> 'Point':
        """ Produce sum of self + other.

        >>> Point(1, 2) + Point(3, 4) == Point(4, 6)
        True
        >>> Point(1, 2) + Point(0, 0) == Point(1, 2)
        True
        """
        return Point(self.x + other.x, self.y + other.y)


if __name__ == "__main__":
    from doctest import testmod
    testmod()

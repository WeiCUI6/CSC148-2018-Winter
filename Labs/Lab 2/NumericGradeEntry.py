"""
module numericgradeentry
"""


from lab2 import GradeEntry


class NumericGradeEntry(GradeEntry):
    """
    class numericgradeentry
    """
    def __init__(self, course_identifier: str, course_weight: float,
                 course_grade: str) -> None:
        """
        initialize a new numericgradeentry

        >>> b1 = NumericGradeEntry('mat137', 1.0, '76')
        >>> b2 = NumericGradeEntry('csc148', 0.5, '87')
        >>> print(b1)
        mat137 76 1.0
        >>> b2.course_weight
        0.5
        >>> b2.course_grade
        '87'
        >>> b2.course_identifier
        'csc148'
        """
        GradeEntry.__init__(self, course_identifier, course_weight,
                            course_grade)

    def get_points(self) -> float:
        """
        return the point based on its grade

        >>> b4 = NumericGradeEntry('mat137', 1.0, '76')
        >>> b5 = NumericGradeEntry('csc148', 0.5, '87')
        >>> b4.get_points()
        3.0
        >>> b5.get_points()
        4.0
        """
        if int(self.course_grade) >= 90:
            return 4.0
        elif int(self.course_grade) >= 85:
            return 4.0
        elif int(self.course_grade) >= 80:
            return 3.7
        elif int(self.course_grade) >= 77:
            return 3.3
        elif int(self.course_grade) >= 73:
            return 3.0
        elif int(self.course_grade) >= 70:
            return 2.7
        elif int(self.course_grade) >= 67:
            return 2.3
        elif int(self.course_grade) >= 63:
            return 2.0
        elif int(self.course_grade) >= 60:
            return 1.7
        elif int(self.course_grade) >= 57:
            return 1.3
        elif int(self.course_grade) >= 53:
            return 1.0
        elif int(self.course_grade) >= 50:
            return 0.7
        elif int(self.course_grade) >= 0:
            return 0.0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    a1 = NumericGradeEntry('mat137', 1.0, '76')
    a2 = NumericGradeEntry('csc148', 0.5, '87')
    print(a1)
    print(a2)
    print(a1.get_points())
    print(a2.get_points())

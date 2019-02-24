"""
module Letter Grade Entry
"""


from lab2 import GradeEntry


class LetterGradeEntry(GradeEntry):
    """
    class letter grade entry
    """
    def __init__(self, course_identifier: str, course_weight: float,
                 course_grade: str) -> None:
        """
        initialize a new LetterGradeEntry

        >>> c1 = LetterGradeEntry('his450', 0.5, 'B+')
        >>> c2 = LetterGradeEntry('lin101', 0.5, 'C')
        >>> c1.course_identifier
        'his450'
        >>> c1.course_weight
        0.5
        >>> c1.course_grade
        'B+'
        >>> print(c2)
        lin101 C 0.5
        """
        GradeEntry.__init__(self, course_identifier, course_weight,
                            course_grade)

    def get_points(self) -> float:
        """
        return the point of this course based on its letter grade

        >>> c3 = LetterGradeEntry('his450', 0.5, 'B+')
        >>> c4 = LetterGradeEntry('lin101', 0.5, 'C')
        >>> c3.get_points()
        3.3
        >>> c4.get_points()
        2.0
        """
        if self.course_grade == 'A+':
            return 4.0
        elif self.course_grade == 'A':
            return 4.0
        elif self.course_grade == 'A-':
            return 3.7
        elif self.course_grade == 'B+':
            return 3.3
        elif self.course_grade == 'B':
            return 3.0
        elif self.course_grade == 'B-':
            return 2.7
        elif self.course_grade == 'C+':
            return 2.3
        elif self.course_grade == 'C':
            return 2.0
        elif self.course_grade == 'C-':
            return 1.7
        elif self.course_grade == 'D+':
            return 1.3
        elif self.course_grade == 'D':
            return 1.0
        elif self.course_grade == 'D-':
            return 0.7
        elif self.course_grade == 'F':
            return 0.0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    a1 = LetterGradeEntry('lin101', 0.5, 'C')
    a2 = LetterGradeEntry('mat137', 1.0, 'B')
    a3 = LetterGradeEntry('his450', 0.5, 'B+')
    print(a1.get_points())
    print(a2)
    print(a3.course_grade)
    print(a3.course_weight)
    print(a3.course_identifier)

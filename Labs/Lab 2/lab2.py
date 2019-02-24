"""
module GradeEntry
"""


from typing import Any


class GradeEntry:
    """
    a grade system for students

    course_identifier - which course
    course_weight - credit
    course_grade - grade for this course
    """
    course_identifier: str
    course_weight: float
    course_grade: str

    def __init__(self, course_identifier: str, course_weight: float,
                 course_grade: str) -> None:
        """
        initialize a new gradeentry


        >>> a1 = GradeEntry('csc148', 0.5, '87')
        >>> a1.course_identifier
        'csc148'
        >>> a1.course_grade
        '87'
        >>> a1.course_weight
        0.5
        """
        self.course_identifier = course_identifier
        self.course_grade = course_grade
        self.course_weight = course_weight

    def __str__(self) -> str:
        """
        Return a str representation of GradeEntry

        >>> a2 = GradeEntry('mat137', 1.0, '76')
        >>> print(a2)
        mat137 76 1.0
        >>> a3 = GradeEntry('his450', 0.5, 'B+')
        >>> print(a3)
        his450 B+ 0.5
        """
        return "{} {} {}".format(self.course_identifier, self.course_grade,
                                 self.course_weight)

    def __eq__(self, other: Any) -> bool:
        """
        return whether other equals to self

        >>> a4 = GradeEntry('mat137', 1.0, '76')
        >>> a5 = GradeEntry('his450', 0.5, 'B+')
        >>> a6 = GradeEntry('mat137', 1.0, '76')
        >>> a4 == a5
        False
        >>> a4 == a6
        True
        """
        return (type(self) == type(other)
                and self.course_weight == other.course_weight
                and self.course_grade == other.course_grade
                and self.course_identifier == other.course_identifier)

    def get_points(self) -> float:
        """
        get points based on its course grade
        """
        raise NotImplementedError('subclass needed')

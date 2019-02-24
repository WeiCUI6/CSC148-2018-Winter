"""
recursion list_odd and count_odd
"""
from typing import List, Union


def list_odd(obj: Union[list, int]) -> List[int]:
    """
    Return a list of all odd integers in obj,
    or sublists of obj, if obj is a list.  If obj is an odd
    integer, return a list containing obj.  Otherwise return
    en empty list.

    >>> list_odd(3)
    [3]
    >>> list_odd(16)
    []
    >>> list_odd([1, 2, 3, 4, 5])
    [1, 3, 5]
    >>> list_odd([1, 2, [3, 4], 5])
    [1, 3, 5]
    >>> list_odd([1, [2, [3, 4]], 5])
    [1, 3, 5]
    """
    if isinstance(obj, int):
        if obj % 2 == 1:
            return [obj]
        else:
            return []
    else:
        return sum([list_odd(x) for x in obj], [])


def count_odd(obj: Union[list, int]) -> int:
    """
    Return the number of odd numbers in obj or sublists of obj
    if obj is a list.  Otherwise, if obj is a number, return 0
    if it is an even number and 1 if it is an odd number.

    >>> count_odd(3)
    1
    >>> count_odd(16)
    0
    >>> count_odd([1, 2, [3, 4], 5])
    3
    """
    if isinstance(obj, int):
        if obj % 2 == 1:
            return 1
        else:
            return 0
    else:
        return sum([count_odd(x) for x in obj])

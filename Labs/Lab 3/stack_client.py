"""
module stack client code
"""

from stack import Stack
from typing import List


def list_stack(list: list, stack: Stack) -> None:
    """
    some function to use class stack

    >>> a2 = Stack()
    >>> list_stack([1, [3, [5, 7], 9], 11], a2)
    11
    9
    7
    5
    3
    1
    """
    for item in list:
        stack.add(item)
    while not stack.is_empty():
        remove = stack.remove()
        if type(remove) == type(list):
            for thing in remove:
                stack.add(thing)
        else:
            print(remove)


if __name__ == '__main__':
    a1 = Stack()
    while True:
        b1 = input('Type a srting:')
        a1.add(b1)
        if b1 == 'end':
            break
    while not a1.is_empty():
        print(a1.remove())

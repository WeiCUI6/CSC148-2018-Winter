"""
module queue client code
"""

from queue import Queue
from csc148_queue import Queue
from typing import List


def list_queue(list: List, queue: Queue) -> None:
    """
    test class Queue3

    >>> queue = Queue()
    >>> list_queue([1, [3, [5, 7], 9], 11], queue)
    1
    11
    3
    9
    5
    7
    """
    for item in list:
        queue.add(item)
    while not queue.is_empty():
        remove = queue.remove()
        if type(remove) == type(list):
            for thing in remove:
                queue.add(thing)
        else:
            print(remove)


if __name__ == '__main__':
    q1 = Queue()
    a = int(input('Choose an integer:'))
    sum = 0
    while True:
        q1.add(a)
        sum += a
        a = int(input('Choose an integer:'))
        if a == 148:
            break
    print(sum)

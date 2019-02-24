""" practice on linked lists
"""
from typing import Union
from typing import Any


class LinkedListNode:
    """
    Node to be used in linked list

    === Attributes ===
    next_ - successor to this LinkedListNode
    value - data this LinkedListNode represents
    """
    next_: Union["LinkedListNode", None]
    value: object

    def __init__(self, value: object,
                 next_: Union["LinkedListNode", None]=None) -> None:
        """
        Create LinkedListNode self with data value and successor next_.
        """
        self.value, self.next_ = value, next_

    def __str__(self) -> str:
        """
        Return a user-friendly representation of this LinkedListNode.

        >>> n = LinkedListNode(5, LinkedListNode(7))
        >>> print(n)
        5 -> 7 ->|
        """
        # start with a string s to represent current node.
        s = "{} ->".format(self.value)
        # create a reference to "walk" along the list
        current_node = self.next_
        # for each subsequent node in the list, build s
        while current_node is not None:
            s += " {} ->".format(current_node.value)
            current_node = current_node.next_
        # add "|" at the end of the list
        assert current_node is None, "unexpected non_None!!!"
        s += "|"
        return s

    def __eq__(self, other: Any):
        """
        Return whether LinkedListNode self is equivalent to other.

        @param LinkedListNode self: this LinkedListNode
        @param LinkedListNode|object other: object to compare to self.
        @rtype: bool

        >>> LinkedListNode(5).__eq__(5)
        False
        >>> n1 = LinkedListNode(5, LinkedListNode(7))
        >>> n2 = LinkedListNode(5, LinkedListNode(7, None))
        >>> n1.__eq__(n2)
        True
        """
        left_node, right_node = self, other
        while (left_node is not None and right_node is not None
               and type(left_node) == type(right_node)
               and left_node.value == right_node.value):
            left_node = left_node.next_
            right_node = right_node.next_
        return left_node is None and right_node is None


class LinkedList:
    """
    Collection of LinkedListNodes

    === Attributes ==
    front - first node of this LinkedList
    back - last node of this LinkedList
    size - number of nodes in this LinkedList, >= 0
    """
    front: Union[LinkedListNode, None]
    back: Union[LinkedListNode, None]
    size: int

    def __init__(self) -> None:
        """
        Create an empty linked list.
        """
        self.front, self.back, self.size = None, None, 0

    def __str__(self) -> str:
        """
        Return a human-friendly string representation of
        LinkedList self.

        >>> lnk = LinkedList()
        >>> print(lnk)
        Empty!
        >>> lnk.prepend(5)
        >>> print(lnk)
        5 ->| Size: 1
        """
        # deal with the case where this list is empty
        if self.front is None:
            assert self.back is None and self.size is 0, "ooooops!"
            return "Empty!"
        else:
            # use front.__str__() if this list isn't empty
            return str(self.front) + " Size: {}".format(self.size)

    def __eq__(self, other: Any) -> bool:
        """
        Return whether LinkedList self is equivalent to
        other.

        >>> LinkedList().__eq__(None)
        False
        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(5)
        >>> lnk.__eq__(lnk2)
        True
        """
        return (type(self) == type(other)
                and self.front == other.front
                and self.back == other.back
                and self.size == other.size)

    def delete_after(self, value: object) -> None:
        """
        Remove the node following the first occurrence of value, if
        possible, otherwise leave self unchanged.

        >>> l1 = LinkedList()
        >>> l1.prepend(3)
        >>> l1.prepend(4)
        >>> l1.prepend(5)
        >>> l1.delete_after(4)
        >>> print(l1)
        5 -> 4 ->| Size: 2
        >>> l1.append(6)
        >>> l1.delete_after(6)
        >>> print(l1)
        5 -> 4 -> 6 ->| Size: 3
        """
        cur_node = self.front
        while cur_node is not None and cur_node.value != value:
            cur_node = cur_node.next_
        if cur_node is None:
            pass
        else:
            if cur_node == self.back:
                pass
            elif cur_node.next_.next_ is None:
                self.back = cur_node
                self.size -= 1
                cur_node.next_ = None
            else:
                cur_node.next_ = cur_node.next_.next_
                self.size -= 1

    def append(self, value: object) -> None:
        """
        Insert a new LinkedListNode with value after self.back.

        >>> lnk = LinkedList()
        >>> lnk.append(5)
        >>> lnk.size
        1
        >>> print(lnk.front)
        5 ->|
        >>> lnk.append(6)
        >>> lnk.size
        2
        >>> print(lnk.front)
        5 -> 6 ->|
        """
        # create the new node
        new_node = LinkedListNode(value)
        # if the list is empty, the new node is front and back
        if self.size == 0:
            assert self.back is None and self.front is None, "ooops"
            self.front = self.back = new_node
        # if the list isn't empty, front stays the same
        else:
            # change *old* self.back.next_ first!!!!
            self.back.next_ = new_node
            self.back = new_node
        # remember to increase the size
        self.size += 1

    def prepend(self, value: object) -> None:
        """
        Insert value before LinkedList self.front.

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> str(lnk.front)
        '2 -> 1 -> 0 ->|'
        >>> lnk.size
        3
        """
        # Create new node with next_ referring to front
        new_node = LinkedListNode(value, self.front)
        # change front
        self.front = new_node
        # if the list was empty, change back
        if self.size == 0:
            self.back = new_node
        # update size
        self.size += 1

    def delete_front(self) -> None:
        """
        Delete LinkedListNode self.front from self.

        Assume self.front is not None

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.delete_front()
        >>> str(lnk.front)
        '1 -> 0 ->|'
        >>> lnk.size
        2
        >>> lnk.delete_front()
        >>> lnk.delete_front()
        >>> str(lnk.front)
        'None'
        """
        assert self.front is not None, "unexpected None!"
        # if back == front, set it to None
        if self.front == self.back:
            self.back = None
        # set front to its successor
        self.front = self.front.next_
        # decrease size
        self.size -= 1

    def __setitem__(self, index: int, value: object) -> None:
        """
        Set the value of list at position index to value. Raise IndexError
        if index >= self.size or index < -self.size

        >>> l1 =LinkedList()
        >>> l1.prepend(2)
        >>> l1.append(3)
        >>> l1.prepend(4)
        >>> l1[0] = 7
        >>> print(l1)
        7 -> 2 -> 3 ->| Size: 3
        >>> l1[-2] = 10
        >>> print(l1)
        7 -> 10 -> 3 ->| Size: 3
        """
        if index < 0:
            index += self.size
        if index >= self.size or self.size == 0 or index < 0:
            raise IndexError('Index out of range')
        cur_node = self.front
        for steps in range(index):
            cur_node = cur_node.next_
        cur_node.value = value

    def __add__(self, other: "LinkedList") -> "LinkedList":
        """
        Return a new list by concatenating self to other.  Leave
        both self and other unchanged.

        >>> lnk1 = LinkedList()
        >>> lnk1.prepend(5)
        >>> lnk1.prepend(4)
        >>> lnk1.prepend(2)
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(7)
        >>> lnk2.prepend(6)
        >>> lnk2.prepend(13)
        >>> print(lnk1 + lnk2)
        2 -> 4 -> 5 -> 13 -> 6 -> 7 ->| Size: 6
        >>> l2 = lnk1 + lnk2
        >>> l2[0] = 12
        >>> print(lnk1)
        2 -> 4 -> 5 ->| Size: 3
        >>> print(l2)
        12 -> 4 -> 5 -> 13 -> 6 -> 7 ->| Size: 6
        >>> l2[3] = 24
        >>> print(l2)
        12 -> 4 -> 5 -> 24 -> 6 -> 7 ->| Size: 6
        >>> print(lnk2)
        13 -> 6 -> 7 ->| Size: 3
        >>> print(lnk1)
        2 -> 4 -> 5 ->| Size: 3
        """
        cur_node = self.front
        cur_node1 = other.front
        lnk = LinkedList()
        while cur_node is not None:
            lnk.append(cur_node.value)
            cur_node = cur_node.next_
        while cur_node1 is not None:
            lnk.append(cur_node1.value)
            cur_node1 = cur_node1.next_
        lnk.size = self.size + other.size
        return lnk

    def insert_before(self, value1: object, value2: object) -> None:
        """
        Insert value1 into LinkedList self before the first occurrence
        of value2, if it exists.  Otherwise leave self unchanged.

        >>> l1 = LinkedList()
        >>> l1.prepend(3)
        >>> l1.prepend(4)
        >>> l1.prepend(5)
        >>> l1.insert_before(5, 5)
        >>> print(l1)
        5 -> 5 -> 4 -> 3 ->| Size: 4
        >>> l1.insert_before(7, 5)
        >>> print(l1)
        7 -> 5 -> 5 -> 4 -> 3 ->| Size: 5
        >>> l1.insert_before(2, 3)
        >>> print(l1)
        7 -> 5 -> 5 -> 4 -> 2 -> 3 ->| Size: 6
        >>> l1.insert_before(13, 13)
        >>> print(l1)
        7 -> 5 -> 5 -> 4 -> 2 -> 3 ->| Size: 6
        """
        cur_node = self.front
        if cur_node.value == value2:
            self.front = LinkedListNode(value1)
            self.front.next_ = cur_node
        else:
            while cur_node.next_.value != value2 and \
                    cur_node.next_.next_ is not None:
                cur_node = cur_node.next_
            new_node = LinkedListNode(value1)
            new_node.next_ = cur_node.next_
            cur_node.next_ = new_node
        self.size += 1

        # pre_node = None
        # cur_node = self.front
        # while cur_node is not None and cur_node.value != value2:
        #     pre_node = cur_node
        #     cur_node = cur_node.next_
        # if cur_node is None:
        #     pass
        # else:
        #     if pre_node is None:
        #         self.prepend(value1)
        #     else:
        #         new_ndoe = LinkedListNode(value1, None)
        #         new_ndoe.next_ = pre_node.next_
        #         pre_node.next_ = new_ndoe
        #         self.size += 1

        # pre_node = None
        # cur_node = self.front
        # while cur_node.value != value2 and cur_node is not None:
        #     pre_node = cur_node
        #     cur_node = cur_node.next_
        # if cur_node is None:
        #     pass
        # else:
        #     if pre_node is None:
        #         self.prepend(value1)
        #     else:
        #         new_ndoe = LinkedListNode(value1, None)
        #         new_ndoe.next_ = pre_node.next_
        #         pre_node.next_ = new_ndoe
        #         self.size += 1

    def copy(self) -> "LinkedList":
        """
        Return a copy of LinkedList self.  The copy should have
        different nodes, but equivalent values, from self.

        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> lnk.prepend(7)
        >>> print(lnk.copy())
        7 -> 5 ->| Size: 2
        """
        lnk = LinkedList()
        cur_node = self.front
        while cur_node is not None:
            lnk.append(cur_node.value)
            cur_node = cur_node.next_
        lnk.size = self.size
        return lnk

    def __len__(self) -> int:
        """
        Return the number of nodes in LinkedList self.

        >>> l1 = LinkedList()
        >>> l1.append(3)
        >>> l1.prepend(4)
        >>> l1.prepend(5)
        >>> len(l1)
        3
        """
        return self.size

    def __getitem__(self, index: int) -> object:
        """
        Return the value at LinkedList self's position index.

        >>> lnk = LinkedList()
        >>> lnk.append(1)
        >>> lnk.append(0)
        >>> lnk.__getitem__(1)
        0
        >>> lnk[-1]
        0
        """
        # deal with a negative index by adding self.size
        if (-self.size > index
                or index > self.size):
            raise IndexError("out of range!!!")
        elif index < 0:
            index += self.size
        current_node = self.front
        # walk index steps along from 0 to retrieve element
        for _ in range(index):
            assert current_node is not None, "unexpected None!!!!!"
            current_node = current_node.next_
        # return the value at position index
        return current_node.value

    def __contains__(self, value: object) -> bool:
        """
        Return whether LinkedList self contains value.

        >>> lnk = LinkedList()
        >>> lnk.append(0)
        >>> lnk.append(1)
        >>> lnk.append(2)
        >>> 2 in lnk
        True
        >>> lnk.__contains__(3)
        False
        """
        current_node = self.front
        # "walk" the linked list
        while current_node is not None:
            # if any node has a value == value, return True
            if current_node.value == value:
                return True
            current_node = current_node.next_
        # if you get to the end without finding value,
        # return False
        return False

    def remove_first_double(self):
        """
        Remove second of two adjacent nodes with duplicate values.
        If there is no such node, leave self as is.  No need
        to deal with subsequent adjacent duplicate values.
        @param LinkedList self: this linked list
        @rtype: None
        >>> list_ = LinkedList()
        >>> list_.append(3)
        >>> list_.append(2)
        >>> list_.append(2)
        >>> list_.append(3)
        >>> list_.append(3)
        >>> print(list_.front)
        3 -> 2 -> 2 -> 3 -> 3 ->|
        >>> list_.remove_first_double()
        >>> print(list_.front)
        3 -> 2 -> 3 -> 3 ->|
        """
        cur_node = self.front
        while cur_node.next_ is not None \
                and cur_node.value != cur_node.next_.value:
            cur_node = cur_node.next_
        if cur_node.next_ is None:
            pass
        else:
            if cur_node.next_.next_ is None:
                self.back = cur_node
                cur_node.next_ = None
                self.size -= 1
            else:
                cur_node.next_ = cur_node.next_.next_
                self.size -= 1


def reverse_list(list_: LinkedList):
        """ Reverse the order of the nodes in list_.
        >>> lnk = LinkedList()
        >>> lnk.prepend(1)
        >>> lnk.prepend(3)
        >>> lnk.prepend(5)
        >>> print(lnk)
        5 -> 3 -> 1 ->| Size: 3
        >>> reverse_list(lnk)
        >>> print(lnk)
        1 -> 3 -> 5 ->| Size: 3
        """



if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config="pylint.txt")

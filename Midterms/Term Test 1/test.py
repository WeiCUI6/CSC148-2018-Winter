""" classes LinkedListNode and LinkedList
"""
from typing import Union, Any


class LinkedListNode:
    """
    Node to be used in linked list

    === Attributes ===
    next_ - successor to this LinkedListNode
    value - data represented by this LinkedListNode
    """
    next_: Union["LinkedListNode", None]

    def __init__(self, value: object,
                 next_: Union["LinkedListNode", None]=None) -> None:
        """
        Create LinkedListNode self with data value and successor next

        >>> LinkedListNode(5).value
        5
        >>> LinkedListNode(5).next_ is None
        True
        """
        self.value, self.next_ = value, next_

    def __str__(self) -> str:
        """
        Return a user-friendly representation of this LinkedListNode.

        >>> n = LinkedListNode(5, LinkedListNode(7))
        >>> print(n)
        5 -> 7 ->|
        """
        self_str = "{} ->".format(self.value)
        current_node = self.next_
        while current_node is not None:
            self_str += " {} ->".format(current_node.value)
            current_node = current_node.next_
        return self_str + "|"

    def __eq__(self, other: Any) -> bool:
        """
        Return whether LinkedListNode self is equivalent to other.

        >>> LinkedListNode(5).__eq__(5)
        False
        >>> n1 = LinkedListNode(5, LinkedListNode(7))
        >>> n2 = LinkedListNode(5, LinkedListNode(7, None))
        >>> n1.__eq__(n2)
        True
        """
        if type(self) != type(other):
            return False
        else:
            self_node, other_node = self, other
            while self_node is not None and other_node is not None:
                if self_node.value != other_node.value:
                    return False
                self_node, other_node = self_node.next_, other_node.next_
            return self_node is None and other_node is None


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
        self.size, self.front, self.back = 0, None, None

    def __str__(self) -> str:
        """
        Return a human-friendly string representation of LinkedList self.
        """
        return "size: {}\n{}".format(self.size, self.front)

    def __eq__(self, other: Any) -> bool:
        """
        Return whether LinkedList self is equivalent to other.

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
                and self.size == other.size
                and self.back == other.back
                and self.front == other.front)
        pass

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
        new_node = LinkedListNode(value)
        if self.size == 0:
            self.front = self.back = new_node
        else:
            self.back.next_ = new_node
            self.back = new_node
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
        self.front = LinkedListNode(value, self.front)
        if self.size == 0:
            self.back = self.front
        else:
            pass
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
        if self.size == 1:
            self.back = self.front = None
        else:
            self.front = self.front.next_
        self.size -= 1

    def __getitem__(self, index: int) -> object:
        """
        Return the value at LinkedList self's position index,
        which must be a valid position in LinkedList self.

        >>> lnk = LinkedList()
        >>> lnk.prepend(1)
        >>> lnk.prepend(0)
        >>> lnk.__getitem__(1)
        1
        >>> lnk[-1]
        1
        """
        if index < -1 * self.size or index >= self.size:
            raise IndexError("{} out of range".format(index))
        elif index < 0:
            index += self.size
        current_node = self.front
        for steps in range(index):
            current_node = current_node.next_
        return current_node.value

    def __contains__(self, value: object) -> bool:
        """
        Return whether LinkedList self contains value.

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.__contains__(1)
        True
        >>> lnk.__contains__(3)
        False
        """
        current_node = self.front
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next_
        return False

    def concat(self, other: 'LinkedList') -> None:
        """
        concate

        >>> lnk1 = LinkedList()
        >>> lnk1.prepend(2)
        >>> lnk1.prepend(1)
        >>> lnk1.prepend(0)
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(5)
        >>> lnk2.prepend(4)
        >>> lnk2.prepend(3)
        >>> lnk1.concat(lnk2)
        >>> print(lnk1.front)
        0 -> 1 -> 2 -> 3 -> 4 -> 5 ->|
        >>> print(lnk2.front)
        None
        """
        self.back.next_ = other.front
        other.front = None
        self.back = other.back
        self.size += other.size


if __name__ == '__main__':
    import doctest
    doctest.testmod()

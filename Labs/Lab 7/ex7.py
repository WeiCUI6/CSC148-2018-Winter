"""
BTNode exercises
"""
from typing import Union, Any


class BTNode:
    """Binary Tree node.

    data - data this node represents
    left - left child
    right - right child
    """
    data: object
    left: Union["BTNode", None]
    right: Union["BTNode", None]

    def __init__(self, data: object,
                 left: Union["BTNode", None]=None,
                 right: Union["BTNode", None]=None) -> None:
        """
        Create BTNode (self) with data and children left and right.

        An empty BTNode is represented by None.

        """
        self.data, self.left, self.right = data, left, right

    def __eq__(self, other: Any) -> bool:
        """
        Return whether BTNode (self) is equivalent to other.

        >>> BTNode(7).__eq__('seven')
        False
        >>> b1 = BTNode(7, BTNode(5))
        >>> b1.__eq__(BTNode(7, BTNode(5), None))
        True
        """
        return (type(self) == type(other) and
                self.data == other.data and
                (self.left, self.right) == (other.left, other.right))

    def __repr__(self) -> str:
        """
        Represent BTNode (self) as a string that can be evaluated to
        produce an equivalent BTNode.

        >>> BTNode(1, BTNode(2), BTNode(3))
        BTNode(1, BTNode(2, None, None), BTNode(3, None, None))
        """
        return 'BTNode({}, {}, {})'.format(self.data,
                                           repr(self.left),
                                           repr(self.right))

    def __str__(self, indent: str="") -> str:
        """
        Return a user-friendly string representing BTNode (self) inorder.
        Indent by indent.

        >>> b = BTNode(1, BTNode(2, BTNode(3)), BTNode(4))
        >>> print(b)
            4
        1
            2
                3
        <BLANKLINE>
        """
        right_tree = self.right.__str__(indent + '    ') if self.right else ''
        left_tree = self.left.__str__(indent + '    ') if self.left else ''
        return right_tree + '{}{}\n'.format(indent, str(self.data)) + left_tree


def list_longest_path(node: Union[BTNode, None]) -> list:
    """ List the data in a longest path of node.

    >>> list_longest_path(None)
    []
    >>> list_longest_path(BTNode(5))
    [5]
    >>> b1 = BTNode(7)
    >>> b2 = BTNode(3, BTNode(2), None)
    >>> b3 = BTNode(5, b2, b1)
    >>> list_longest_path(b3)
    [5, 3, 2]
    """
    path = []
    if node is None:
        return []
    if node.left is None and node.right is None:
        return [node.data]
    path.append([node.data] + list_longest_path(node.left))
    path.append([node.data] + list_longest_path(node.right))
    lens = [len(child) for child in path]
    return path[lens.index(max(lens))]


def list_between(node: Union[BTNode, None], start: object, end: object) -> list:
    """
    Return a Python list of all data in the binary search tree
    rooted at node that are between start and end (inclusive).

    A binary search tree t is a BTNode where all nodes in the subtree
    rooted at t.left are less than t.data, and all nodes in the subtree
    rooted at t.right are more than t.data

    Avoid visiting nodes with values less than start or greater than end.

    >>> b_left = BTNode(4, BTNode(2), BTNode(6))
    >>> b_right = BTNode(12, BTNode(10), BTNode(14))
    >>> b = BTNode(8, b_left, b_right)
    >>> list_between(None, 3, 13)
    []
    >>> list_between(b, 2, 3)
    [2]
    >>> L = list_between(b, 3, 11)
    >>> L.sort()
    >>> L
    [4, 6, 8, 10]
    """
    if node is None:
        return []
    if start < node.data < end:
        return [node.data] + list_between(node.left, start, end) + \
               list_between(node.right, start, end)
    elif node.data == start:
        return [node.data] + list_between(node.right, start, end)
    elif node.data < start:
        return list_between(node.right, start, end)
    elif node.data == end:
        return [node.data] + list_between(node.left, start, end)
    return list_between(node.left, start, end)


def count_shallower(t: Union[BTNode, None], n: int) -> int:
    """ Return the number of nodes in tree rooted at t with
    depth less than n.

    >>> t = BTNode(0, BTNode(1, BTNode(2)), BTNode(3))
    >>> count_shallower(t, 2)
    3
    """
    if t is None:
        return 0
    elif n <= 0:
        return 0
    else:
        return 1 + sum([count_shallower(t.left, n-1),
                        count_shallower(t.right, n-1)])


def concatenate_leaves(t: Union[BTNode, None]) -> str:
    """
    Return the string values in the Tree rooted at t
    concatenated from left to right.

    Assume all leaves have string value.

    >>> t1 = BTNode("one")
    >>> t2 = BTNode("two")
    >>> t3 = BTNode("three", t1, t2)
    >>> concatenate_leaves(t1)
    'one'
    >>> concatenate_leaves(t3)
    'onetwo'
    """
    if t is None:
        return ''
    elif t.left is None and t.right is None:
        return '{}'.format(t.data)
    else:
        return concatenate_leaves(t.left) + concatenate_leaves(t.right)


def count_leaves(t: Union[BTNode, None]) -> int:
    """
    Return the number of leaves in BinaryTree t.

    >>> t1 = BTNode(1)
    >>> t2 = BTNode(2)
    >>> t3 = BTNode(3, t1, t2)
    >>> count_leaves(None)
    0
    >>> count_leaves(t3)
    2
    """
    if t is None:
        return 0
    elif t.left is None and t.right is None:
        return 1
    else:
        return sum([count_leaves(t.left), count_leaves(t.right)])


def sum_leaves(t: Union[BTNode, None]) -> int:
    """
    Return the sum of the values in the leaves of BinaryTree t.  Return
    0 if t is empty.
    Assume all leaves have integer value.

    >>> t1 = BTNode(1)
    >>> t2 = BTNode(2)
    >>> t3 = BTNode(3, t1, t2)
    >>> sum_leaves(t2)
    2
    >>> sum_leaves(t3)
    3
    """
    if t is None:
        return 0
    elif t.left is None and t.right is None:
        return t.data
    else:
        return sum([sum_leaves(t.left), sum_leaves(t.right)])


def sum_internal(t: Union[BTNode, None]) -> int:
    """
    Return the sum of the values in the internal nodes of BinaryTree t.  Return
    0 if t is empty.
    Assume all internal nodes have integer value.

    >>> t1 = BTNode(1)
    >>> t2 = BTNode(2)
    >>> t3 = BTNode(3, t1, t2)
    >>> sum_internal(t2)
    0
    >>> sum_internal(t3)
    3
    """
    if t is None:
        return 0
    elif t.left is None and t.right is None:
        return 0
    else:
        return t.data + sum_internal(t.left) + sum_internal(t.right)


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config='pylint.txt')
    import doctest
    doctest.testmod()

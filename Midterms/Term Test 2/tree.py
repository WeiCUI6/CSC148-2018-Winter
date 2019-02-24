""" Tree class and functions
"""
from csc148_queue import Queue
from typing import Callable


class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    === Attributes ===
    @param object value: value of root node
    @param list[Tree|None] children: child nodes
    """

    def __init__(self, value=None, children=None):
        """
        Create Tree self with content value and 0 or more children
        @param Tree self: this tree
        @param object value: value contained in this tree
        @param list[Tree|None] children: possibly-empty list of children
        @rtype: None
        """
        self._value = value
        # copy children if not None
        # NEVER have a mutable default parameter...
        self._children = children[:] if children is not None else []

    # make self.value and self.children read-only by setting
    # only the get field of their property
    def _get_value(self):
        return self._value

    value = property(_get_value)

    def _get_children(self):
        return self._children

    children = property(_get_children)

    def __repr__(self):
        """
        Return representation of Tree (self) as string that
        can be evaluated into an equivalent Tree.

        @param Tree self: this tree
        @rtype: str

        >>> t1 = Tree(5)
        >>> t1
        Tree(5)
        >>> t2 = Tree(7, [t1])
        >>> t2
        Tree(7, [Tree(5)])
        """
        # Our __repr__ is recursive, because it can also be called
        # via repr...!
        return ('{}({}, {})'.format(self.__class__.__name__, repr(self.value),
                                    repr(self.children))
        if self.children
        else 'Tree({})'.format(repr(self.value)))

    def __eq__(self, other):
        """
        Return whether this Tree is equivalent to other.

        @param Tree self: this tree
        @param object|Tree other: object to compare to self
        @rtype: bool

        >>> t1 = Tree(5)
        >>> t2 = Tree(5, [])
        >>> t1 == t2
        True
        >>> t3 = Tree(5, [t1])
        >>> t2 == t3
        False
        """
        return (type(self) is type(other) and
                self.value == other.value and
                self.children == other.children)

    def __str__(self, indent=0):
        """
        Produce a user-friendly string representation of Tree self,
        indenting each level as a visual clue.

        @param Tree self: this tree
        @param int indent: amount to indent each level of tree
        @rtype: str

        >>> t = Tree(17)
        >>> print(t)
        17
        >>> t1 = Tree(19, [t, Tree(23)])
        >>> print(t1)
           23
        19
           17
        >>> t3 = Tree(29, [Tree(31), t1])
        >>> print(t3)
              23
           19
              17
        29
           31
        """
        root_str = indent * " " + str(self.value)
        mid = len(self.non_none_kids()) // 2
        left_str = [c.__str__(indent + 3)
                    for c in self.non_none_kids()][: mid]
        right_str = [c.__str__(indent + 3)
                     for c in self.non_none_kids()][mid:]
        return '\n'.join(right_str + [root_str] + left_str)

    def non_none_kids(self):
        """ Return a list of Tree self's non-None children.

        @param Tree self:
        @rtype: list[Tree]
        """
        return [c
                for c in self.children
                if c is not None]

    def is_leaf(self):
        """Return whether Tree self is a leaf

        @param Tree self:
        @rtype: bool

        >>> Tree(5).is_leaf()
        True
        >>> Tree(5,[Tree(7)]).is_leaf()
        False
        """
        return len(self.non_none_kids()) == 0

    def __contains__(self, v):
        """
        Return whether Tree self contains v.

        @param Tree self: this tree
        @param object v: value to search this tree for

        >>> t = Tree(17)
        >>> t.__contains__(17)
        True
        >>> t = descendants_from_list(Tree(19), [1, 2, 3, 4, 5, 6, 7], 3)
        >>> t.__contains__(3)
        True
        >>> t.__contains__(18)
        False
        """
        if self.children == []:
            return self.value == v
        else:
            return any([c.__contains__(v)
                        for c in self.children])

    def count_nodes(self) -> int:
        """
        Return node count of Tree self.

        @param Tree self: this tree
        @rtype int

        >>> t = Tree(17)
        >>> t.count_nodes()
        1
        >>> t = descendants_from_list(Tree(19), [1, 2, 3, 4, 5, 6, 7], 3)
        >>> t.count_nodes()
        8
        """
        return 1 + sum([c.count_nodes()
                        for c in self.children])

    def height(self):
        """
        Return length of longest path, + 1, in tree rooted at self.

        @param Tree self:
        @rtype: int

        >>> t = Tree(5)
        >>> t.height()
        1
        >>> t = descendants_from_list(Tree(7), [0, 1, 3, 5, 7, 9, 11, 13], 3)
        >>> t.height()
        3
        """
        return 1 + max([c.height() for c in self.children] + [0])

    def flatten(self):
        """ Return a list of all values in tree rooted at self.

        @param Tree self:
        @rtype: list

        >>> t = Tree(5)
        >>> t.flatten()
        [5]
        >>> t = descendants_from_list(Tree(7), [0, 1, 3, 5, 7, 9, 11, 13], 3)
        >>> L = t.flatten()
        >>> L.sort()
        >>> L == [0, 1, 3, 5, 7, 7, 9, 11, 13]
        True
        """
        if self.is_leaf():
            return [self.value]
        else:
            return ([self.value]
                    + sum([c.flatten()
                           for c in self.non_none_kids()], []))


def descendants_from_list(t, list_, arity):
    """
    Populate Tree t's descendants from list_, filling them
    in in level order, with up to arity children per node.
    Then return t.
    @param Tree t: tree to populate from list_
    @param list list_: list of values to populate from
    @param int arity: maximum branching factor
    @rtype: Tree
    >>> descendants_from_list(Tree(0), [1, 2, 3, 4], 2)
    Tree(0, [Tree(1, [Tree(3), Tree(4)]), Tree(2)])
    """
    q = Queue()
    q.add(t)
    list_ = list_.copy()
    while not q.is_empty():  # unlikely to happen
        new_t = q.remove()
        for i in range(0, arity):
            if len(list_) == 0:
                return t  # our work here is done
            else:
                new_t_child = Tree(list_.pop(0))
                new_t.children.append(new_t_child)
                q.add(new_t_child)
    return t


def preorder_visit(t):
    """
    Visit each node of Tree t in preorder, and act on the nodes
    as they are visited.
    @param Tree t: tree to visit in preorder
    @param (Tree)->Any act: function to carry out on visited Tree node
    @rtype: None
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> preorder_visit(t)
    [0, 1, 4, 5, 6, 2, 7, 3]
    """
    if not t.children:
        return [t.value]
    else:
        result = [t.value]
        for c in t.children:
            result.extend(preorder_visit(c))
        return result


def postorder_visit(t, act):
    """
    Visit each node of t in postorder, and act on it when it is visited.
    @param Tree t: tree to be visited in postorder
    @param (Tree)->Any act: function to do to each node
    @rtype: None
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> postorder_visit(t, act)
    4
    5
    6
    1
    7
    2
    3
    0
    """
    for c in t.children:
        postorder_visit(c, act)
    act(t)


def levelorder_visit(t, act):
    """
    Visit every node in Tree t in level order and act on the node
    as you visit it.
    @param Tree t: tree to visit in level order
    @param (Tree)->Any act: function to execute during visit
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> levelorder_visit(t, act)
    0
    1
    2
    3
    4
    5
    6
    7
    """
    to_process = Queue()
    to_process.add(t)

    while not to_process.is_empty():
        next_node = to_process.remove()
        act(next_node)
        for c in next_node.children:
            to_process.add(c)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

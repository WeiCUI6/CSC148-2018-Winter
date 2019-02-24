from typing import Any, Union, List, Optional

## 一勾CS大课堂, CSC148 Winter 2018 额外编程练习题
## 请确保你把上课给的题都搞懂，再做这里的问题

# General Tree (Tree)
class Tree:
    value: Any
    children: List[Any]

    def __init__(self, value, children=None):
        self.value = value
        self.children = children.copy() if children else []

    ## helper function to compare two Tree, do not modify
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.value == other.value and \
               self.children == other.children


    ## 简单问题

    def sum_pos(self):
        """ Return the sum of all positive integers in this tree.
        >>> t = Tree(17, [Tree(-2, [Tree(5), Tree(6, [Tree(-8), Tree(13)])]), Tree(3, [Tree(-7), Tree(8, [Tree(9)])]), Tree(4)])
        >>> t.sum_pos()
        65
        >>> t = Tree(17, [Tree(3)])
        >>> t.sum_pos()
        20
        """
        if not self.children:
            if self.value > 0:
                return self.value
            else:
                return 0
        else:
            if self.value > 0:
                return self.value + sum([c.sum_pos() for c in self.children])
            else:
                return sum([c.sum_pos() for c in self.children])

    ## 跟Path有关的额外练习

    def longest_path2(self):
        """ Returns a integer indicating the longest path this tree has

        >>> t = Tree(17, [Tree(-2, [Tree(5), Tree(6, [Tree(-8), Tree(13)])]), Tree(3, [Tree(-7), Tree(8, [Tree(9)])]), Tree(4)])
        >>> t.longest_path2()
        4
        >>> t = Tree(17, [Tree(3)])
        >>> t.longest_path2()
        2
        """
        pass


    ## 跟Depth有关的额外练习

    def count_at_depth(self, depth):
        """ Returns number of values at given depth in tree

        >>> t = Tree(17, [Tree(-2, [Tree(5), Tree(6, [Tree(-8), Tree(13)])]), Tree(3, [Tree(-7), Tree(8, [Tree(9)])]), Tree(4)])
        >>> t.count_at_depth(0)
        1
        >>> t = Tree(17, [Tree(-2, [Tree(5), Tree(6, [Tree(-8), Tree(13)])]), Tree(3, [Tree(-7), Tree(8, [Tree(9)])]), Tree(4)])
        >>> t.count_at_depth(1)
        3
        >>> t = Tree(17, [Tree(-2, [Tree(5), Tree(6, [Tree(-8), Tree(13)])]), Tree(3, [Tree(-7), Tree(8, [Tree(9)])]), Tree(4)])
        >>> t.count_at_depth(2)
        4
        """
        if depth < 0:
            return 0
        if depth == 0:
            return 1
        else:
            return sum([c.count_at_depth(depth - 1) for c in self.children])

    def sum_values_until_depth(self, depth):
        """ Returns the sum of all the values in this tree until given depth is reached
            if given depth 0 means only value of the root
            if given depth 1 means root plus all the values in depth 1
            etc

        >>> t = Tree(17, [Tree(-2, [Tree(5), Tree(6, [Tree(-8), Tree(13)])]), Tree(3, [Tree(-7), Tree(8, [Tree(9)])]), Tree(4)])
        >>> t.sum_values_until_depth(0)
        17
        >>> t.sum_values_until_depth(1)
        22
        >>> t.sum_values_until_depth(2)
        34
        >>> t.sum_values_until_depth(3)
        48
        >>> t.sum_values_until_depth(4)
        48
        """
        if depth < 0:
            return 0
        if depth == 0:
            return self.value
        else:
            return self.value + sum([c.sum_values_until_depth(depth - 1) for c in self.children])


if __name__ == '__main__':
    import doctest
    doctest.testmod()

from typing import Any, Union, List, Optional

# Recursion Q1

def num_lists(obj: Union[Any, List]) -> int:
    """Return the number of list objects in the given nested list.
    If obj is a list itself, include it in the count.
    
    >>> num_lists(4)
    0
    >>> num_lists([1, 2, 3])
    1
    >>> num_lists([1, [2], [[3, 4]]])
    4
    """
    pass

# Recursion Q2

def num_strings(obj: Union[Any, List]) -> int:
    """Return the number of string objects in the given object.
    If obj is a string itself, include it in the count.
    
    >>> num_strings(3)
    0
    >>> num_strings("sb")
    1
    >>> num_strings([1, "you", "suck"])
    2
    >>> num_strings([1, ["you"], "really", [["suck", 4]]])
    3
    """
    pass
    
# Recursion Q3

def all_string_length(obj: Union[Any, List]) -> int:
    """Return the total string length of all string objects 
    in the given object.
    If obj is a string itself, include it in the total.
    
    >>> all_string_length(3)
    0
    >>> all_string_length("sb")
    2
    >>> all_string_length([1, "you", "suck"])
    7
    >>> all_string_length([1, ["you"], "really", [["suck", 4]]])
    13
    """
    pass


# Binary Tree

# following class is based on CSC148 Winter 2018 Danny Heap
class BTNode:
    """Binary Tree node.
    """
    # The item stored at the root of the tree, or None if the tree is empty
    data: object
    # The left subtree, or None if the tree is empty
    left: Optional['BTNode']
    # The right subtree, or None if the tree is empty
    right: Optional['BTNode']

    def __init__(self, data: object,
                 left: Union["BTNode", None]=None,
                 right: Union["BTNode", None]=None) -> None:
        """
        Create BTNode (self) with data and children left and right.
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

    def __repr__(self):
        """ (BTNode) -> str

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

    def __contains__(self, data):
        """ (BTNode, object) -> value

        Return whether tree rooted at node contains value.

        >>> BTNode.__contains__(None, 5)
        False
        >>> t = BTNode(5, BTNode(7), BTNode(9))
        >>> t.__contains__(7)
        True
        >>> 9 in t
        True
        >>> 11 in t
        False
        """
        if self is None:
            return False
        else:
            return (self.data == data
                    # call with BTNode in case self.left, self.right are None
                    or BTNode.__contains__(self.left, data)
                    or BTNode.__contains__(self.right, data))

# module level function to calculate height
def height(node: Union[BTNode, None]) -> int:
    """
    Return height of tree rooted at node.

    >>> height(None)
    0
    >>> height(BTNode(5, BTNode(3), BTNode(7)))
    2
    """
    if node is None:
        return 0
    else:
        return 1 + max(height(node.left), height(node.right))

# module level function to calcuate the maximum node from the 
# given node (BT), please note this is NOT binary search
def find(node: Union[BTNode, None],
         data: object) -> Union[BTNode, None]:
    """

    Return a BTNode containing data, or else None.

    >>> find(None, 15) is None
    True
    >>> b = BTNode(5, BTNode(4))
    >>> find(b, 7) is None
    True
    >>> find(b, 4)
    BTNode(4, None, None)
    """
    if node is None:
        return None
    else:
        find_left_result = find(node.left, data)
        if node.data == data:
            return node
        elif find_left_result is not None:
            return find_left_result
        else:
            return find(node.right, data)
        
def bst_find(node: Union[BTNode, None], data: object) -> Union[BTNode, None]:
    """
    Return a BTNode containing data, or else None. node will be a BST.
    >>> find(None, 15) is None
    True
    >>> b = BTNode(5, BTNode(4))
    >>> find(b, 7) is None
    True
    >>> find(b, 4)
    BTNode(4, None, None)
    >>> b = BTNode(5, BTNode(4), BTNode(8))
    >>> find(b, 8)
    BTNode(8, None, None)
    """
    if node is None:
        return None
    if node.data == data:
        return node
    if data < node.data:
        return bst_find(node.left)
    else:
        return bst_find(node.right)

def find_max(node):
    """Return the maximum item in this BST root node, or None if this  
       BST is empty.
    >>> find_max(None) is None
    True
    >>> b = BTNode(5, BTNode(4), BTNode(8))
    >>> find_max(b)
    8
    """
    pass

def in_order_travel(node: Union[BTNode, None]) -> List[object]:
    """
    Extra practice
    >>> b = BTNode(5, BTNode(4), BTNode(8))
    >>> in_order_travel(b)
    [4, 5, 8]
    """
    pass

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
    
    def sum_values(self):
        """ Returns the sum of all the values in this tree
        
        >>> t = Tree(17, [Tree(-2, [Tree(5), Tree(6, [Tree(-8), Tree(13)])]), Tree(3, [Tree(-7), Tree(8, [Tree(9)])]), Tree(4)]) 
        >>> t.sum_values()
        48
        """
        pass
    
    def max_value(self):
        """ Returns the maximum value within the tree
        
        >>> t = Tree(17, [Tree(-2, [Tree(5), Tree(6, [Tree(-8), Tree(13)])]), Tree(3, [Tree(-7), Tree(8, [Tree(9)])]), Tree(4)]) 
        >>> t.max_value()
        17
        """
        pass
    
    def sum_values_above_n(self, n):
        """ Returns the sum of all the values that are strickly greater than n.
        
        >>> t = Tree(17, [Tree(-2, [Tree(5), Tree(6, [Tree(-8), Tree(13)])]), Tree(3, [Tree(-7), Tree(8, [Tree(9)])]), Tree(4)]) 
        >>> t.sum_values_above_n(5)
        53
        """
        pass
    
    def __contains__(self, obj):
        """ Return true if obj in tree, False otherwise
        
        >>> t = Tree(17, [Tree(-2, [Tree(5), Tree(6, [Tree(-8), Tree(13)])]), Tree(3, [Tree(-7), Tree(8, [Tree(9)])]), Tree(4)]) 
        >>> 17 in t
        True
        >>> 3 in t
        True
        >>> 55 in t
        False
        """
        pass
    
    def longest_path(self):
        """ Returns a list of items on the longest possible path between the 
            root of the tree and one of its leaves. The list is ordered by 
            increasing depth, so the tree’s root is always the first element.
            
        >>> t = Tree(17, [Tree(-2, [Tree(5), Tree(6, [Tree(-8), Tree(13)])]), Tree(3, [Tree(-7), Tree(8, [Tree(9)])]), Tree(4)]) 
        >>> t.longest_path()
        [17, 3, 8, 9]
        """
        pass
    
    def all_path(self):
        """
        returns a list of list of items on all possible path between the root
        of the tree and one of its leaves. Each list in returned list is ordered
        by increasing depth, so the tree’s root is always the first element, and 
        returned list of list can be in any order
        
        >>> t = Tree(17, [Tree(-2, [Tree(5), Tree(6, [Tree(-8), Tree(13)])]), Tree(3, [Tree(-7), Tree(8, [Tree(9)])]), Tree(4)]) 
        >>> t.all_path()
        [[17, -2, 5], [17, -2, 6, -8], [17, -2, 6, 13], [17, 3, -7], [17, 3, 8, 9], [17, 4]]
        """
        pass
    
    def partition_leaves(self):
        """ Returns a tuple of two lists, where the first list contains the 
        leaves of the tree that are negative, and the second list contains the
        leaves that are greater than or equal to 0. Assume that all values 
        stored in the tree are integers.
        
        >>> t = Tree(17, [Tree(-2, [Tree(5), Tree(6, [Tree(-8), Tree(13)])]), Tree(3, [Tree(-7), Tree(8, [Tree(9)])]), Tree(4)]) 
        >>> t.partition_leaves()
        ([-8, -7], [5, 13, 9, 4])
        """
        pass
    
    def sum_at_depth(self, depth):
        """ Returns the sum of all the values at given d
        
        >>> t = Tree(17, [Tree(-2, [Tree(5), Tree(6, [Tree(-8), Tree(13)])]), Tree(3, [Tree(-7), Tree(8, [Tree(9)])]), Tree(4)]) 
        >>> t.sum_at_depth(0)
        17
        >>> t.sum_at_depth(1)
        5
        >>> t.sum_at_depth(2)
        12
        >>> t.sum_at_depth(3)
        14
        >>> t.sum_at_depth(4)
        0
        """
        pass
    
    def remove_beyond_depth(self, depth: int) -> None:
        """ Remove all children and all children's children at depth 
        Precondition: depth > 1
        
        >>> t = Tree(17, [Tree(-2, [Tree(5), Tree(6, [Tree(-8), Tree(13)])]), Tree(3, [Tree(-7), Tree(8, [Tree(9)])]), Tree(4)]) 
        >>> t.remove_beyond_depth(1)
        >>> t == Tree(17)
        True
        >>> t = Tree(17, [Tree(-2, [Tree(5), Tree(6, [Tree(-8), Tree(13)])]), Tree(3, [Tree(-7), Tree(8, [Tree(9)])]), Tree(4)]) 
        >>> t.remove_beyond_depth(2)
        >>> t == Tree(17, [Tree(-2), Tree(3), Tree(4)])
        True
        """
        ## if depth is 0 or self got no children
        ## we don't have to do anything, nothing will be chagned
        if depth == 0 or not self.children:
            return
        ## if depth is 1, means i need remove all my children, because
        ## all my children is depth 1 to myself
        if depth == 1:
            self.children = []
            return
        for c in self.children:
            c.remove_beyond_depth(depth - 1)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    # Your playground
    
    # t = Tree(17, [Tree(-2, [Tree(5), Tree(6, [Tree(-8), Tree(13)])]), Tree(3, [Tree(-7), Tree(8, [Tree(9)])]), Tree(4)]) 
    # print(t.longest_path())
    # print(t.all_path())
    # print(t.partition_leaves())
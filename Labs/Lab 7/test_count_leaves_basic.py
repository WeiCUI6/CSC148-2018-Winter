import unittest

from extra_practice import count_leaves
from hypothesis import given
from hypothesis.strategies import recursive
from hypothesis.strategies import booleans
from hypothesis.strategies import tuples
from hypothesis.strategies import none

class BTNode:
    """
    A Binary Tree, i.e. arity 2.
   === Attributes ===
    @param object data: data in this node of tree
    @param BTNode|None left: left child
    @param BTNode|None right: right child
    @rtype: None
    """


    def __init__(self, data, left=None, right=None):
        """
        Create BTNode self with data and children left and right.
        @param BTNode self: this binary tree
        @param object data: data of this node
        @param BTNode|None left: left child
        @param BTNode|None right: right child
        @rtype: None
        """
        self.data, self.left, self.right = data, left, right

def tuples_to_tree(t):
    """
    Return a BTNode generated from t and the number of leaves.

    Precondition: t is in the form (data, left child, right child) where
                  left child and right child are either None, a data, or
                  another tuple.

    @param tuple(bool, tuple|None|bool, tuple|None|bool) t: The tuple to turn
                                                            into a BTNode
    @rtype: (BTNode, int)
    """
    if t is None:
        return (None, 0)

    if type(t) == bool:
        return (BTNode(t), 1)

    (left, l_count) = tuples_to_tree(t[1])
    (right, r_count) = tuples_to_tree(t[2])
    num_leaves = l_count + r_count

    if num_leaves == 0:
        num_leaves = 1

    return (BTNode(t[0], left, right), num_leaves)

class CountLeavesTests(unittest.TestCase):
    def test_returns_int(self):
        """
        Test count_leaves to make sure it returns an int.
        """
        return_type = type(count_leaves(BTNode(1)))

        self.assertEqual(return_type, int, "count_leaves should return type " +
                         "int, but instead returned type {}.".format(
                             return_type))

    def test_none(self):
        """
        Test count_leaves on None.
        """
        self.assertEqual(count_leaves(None), 0, "count_leaves on None should " +
                         "return 0.")

    def test_leaf(self):
        """
        Test count_leaves on a leaf.
        """
        self.assertEqual(count_leaves(BTNode(1)), 1, "count_leaves should" +
                         " return 1 when used on a leaf.")

    def test_one_left_child(self):
        """
        Test count_leaves on a BTNode with one left child.
        """
        t = BTNode(1, BTNode(2))
        self.assertNotEqual(count_leaves(t), 2, "count_leaves should not " +
                            "count None or any BTNodes with children as" +
                            " leaf nodes.")
        self.assertEqual(count_leaves(t), 1, "count_leaves should return 1 " +
                         "when used on a BTNode with only one child, " +
                         "where the child is a leaf.")

    def test_one_right_child(self):
        """
        Test count_leaves on a BTNode with one right child
        """
        t = BTNode(1, None, BTNode(2))
        self.assertNotEqual(count_leaves(t), 2, "count_leaves should not " +
                            "count None or any BTNodes with children as" +
                            " leaf nodes.")
        self.assertEqual(count_leaves(t), 1, "count_leaves should return 1 " +
                         "when used on a BTNode with only one child, " +
                         "where the child is a leaf.")

    def test_two_leaf_children(self):
        """
        Test count_leaves on a BTNode with two leaf children.
        """
        t = BTNode(1, BTNode(2), BTNode(3))
        self.assertEqual(count_leaves(t), 2, "count_leaves should count all " +
                         "of the leaves in the entire BTNode.")

    @given(recursive(none() | booleans(), lambda children: tuples(booleans(),
                                                                  children,
                                                                  children)))
    def test_count_leaves(self, tuple_tree):
        """
        Test count_leaves on a randomly generated BTNode.
        """
        (t, expected) = tuples_to_tree(tuple_tree)
        actual = count_leaves(t)
        self.assertEqual(actual, expected,
                         ("test_count_leaves on BTNode\n{}\nReturned {}" +
                          " instead of {}.").format(tuple_tree, actual,
                                                    expected))

if __name__ == '__main__':
    unittest.main()

import unittest

from extra_practice import sum_leaves
from hypothesis import given
from hypothesis.strategies import recursive
from hypothesis.strategies import integers
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

    @param tuple(bool, tuple|None|int, tuple|None|int) t: The tuple to turn
                                                            into a BTNode
    @rtype: (BTNode, int)
    """
    if t is None:
        return (None, 0)

    if type(t) == int:
        return (BTNode(t), t)

    (left, l_count) = tuples_to_tree(t[1])
    (right, r_count) = tuples_to_tree(t[2])
    sum_leaves = l_count + r_count

    if not left and not right:
        sum_leaves = t[0]

    return (BTNode(t[0], left, right), sum_leaves)

class SumLeavesTests(unittest.TestCase):
    def test_returns_int(self):
        """
        Test sum_leaves to make sure it returns an int.
        """
        return_type = type(sum_leaves(BTNode(1)))

        self.assertEqual(return_type, int, "sum_leaves should return type " +
                         "int, but instead returned type {}.".format(
                             return_type))

    def test_none(self):
        """
        Test sum_leaves on None.
        """
        self.assertEqual(sum_leaves(None), 0, "sum_leaves on None should " +
                         "return 0.")

    def test_leaf(self):
        """
        Test sum_leaves on a leaf.
        """
        self.assertEqual(sum_leaves(BTNode(2)), 2, "sum_leaves should" +
                         " return the leaf's data when used on a leaf.")

    def test_one_left_child(self):
        """
        Test sum_leaves on a BTNode with one left child.
        """
        t = BTNode(1, BTNode(5))
        self.assertNotEqual(sum_leaves(t), 1, "sum_leaves should not " +
                            "count None or any BTNodes with children as" +
                            " leaf nodes.")
        self.assertNotEqual(sum_leaves(t), 6, "sum_leaves should not " +
                            "count None or any BTNodes with children as" +
                            " leaf nodes.")
        self.assertEqual(sum_leaves(t), 5, "sum_leaves should return the " +
                         "data of the leaf child when used on a BTNode " +
                         "with a single leaf child.")

    def test_one_right_child(self):
        """
        Test sum_leaves on a BTNode with one right child
        """
        t = BTNode(1, None, BTNode(5))
        self.assertNotEqual(sum_leaves(t), 1, "sum_leaves should not " +
                            "count None or any BTNodes with children as" +
                            " leaf nodes.")
        self.assertNotEqual(sum_leaves(t), 6, "sum_leaves should not " +
                            "count None or any BTNodes with children as" +
                            " leaf nodes.")
        self.assertEqual(sum_leaves(t), 5, "sum_leaves should return the " +
                         "data of the leaf child when used on a BTNode " +
                         "with a single leaf child.")

    def test_two_leaf_children(self):
        """
        Test sum_leaves on a BTNode with two leaf children.
        """
        t = BTNode(5, BTNode(4), BTNode(3))
        self.assertEqual(sum_leaves(t), 7, "sum_leaves should sum all " +
                         "of the leaves in the entire BTNode.")

    @given(recursive(none() | integers(min_value=0, max_value=100),
                     lambda children: tuples(integers(min_value = 0,
                                                      max_value = 100),
                                             children,
                                             children))
           )
    def test_sum_leaves(self, tuple_tree):
        """
        Test sum_leaves on a randomly generated BTNode.
        """
        (t, expected) = tuples_to_tree(tuple_tree)
        actual = sum_leaves(t)
        self.assertEqual(actual, expected,
                         ("test_sum_leaves on BTNode\n{}\nReturned {}" +
                          " instead of {}.").format(tuple_tree, actual,
                                                    expected))

if __name__ == '__main__':
    unittest.main()

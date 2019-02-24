import unittest

from extra_practice import sum_internal
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
    Return a BTNode generated from t and the number of internal.

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
        return (BTNode(t), 0)

    (left, l_count) = tuples_to_tree(t[1])
    (right, r_count) = tuples_to_tree(t[2])
    sum_internal = l_count + r_count

    if left or right:
        sum_internal += t[0]

    return (BTNode(t[0], left, right), sum_internal)


class SumInternalTests(unittest.TestCase):
    def test_returns_int(self):
        """
        Test sum_internal to make sure it returns an int.
        """
        return_type = type(sum_internal(BTNode(1)))

        self.assertEqual(return_type, int, "sum_internal should return type " +
                         "int, but instead returned type {}.".format(
                             return_type))

    def test_none(self):
        """
        Test sum_internal on None.
        """
        self.assertEqual(sum_internal(None), 0, "sum_internal on None should " +
                         "return 0.")

    def test_leaf(self):
        """
        Test sum_internal on a leaf.
        """
        self.assertEqual(sum_internal(BTNode(2)), 0, "sum_internal should" +
                         " return 0 when used on a leaf.")

    def test_one_left_child(self):
        """
        Test sum_internal on a BTNode with one left child.
        """
        t = BTNode(1, BTNode(5))
        self.assertNotEqual(sum_internal(t), 5, "sum_internal should not " +
                            "count None or any BTNodes without children as" +
                            " internal nodes.")
        self.assertNotEqual(sum_internal(t), 6, "sum_internal should not " +
                            "count None or any BTNodes without children as" +
                            " internal nodes.")
        self.assertEqual(sum_internal(t), 1, "sum_internal should return the " +
                         "data of the root node when used on a BTNode " +
                         "with a single leaf child.")

    def test_one_right_child(self):
        """
        Test sum_internal on a BTNode with one right child
        """
        t = BTNode(1, None, BTNode(5))
        self.assertNotEqual(sum_internal(t), 5, "sum_internal should not " +
                            "count None or any BTNodes without children as" +
                            " internal nodes.")
        self.assertNotEqual(sum_internal(t), 6, "sum_internal should not " +
                            "count None or any BTNodes without children as" +
                            " internal nodes.")
        self.assertEqual(sum_internal(t), 1, "sum_internal should return the " +
                         "data of the root node when used on a BTNode " +
                         "with a single leaf child.")

    def test_two_leaf_children(self):
        """
        Test sum_internal on a BTNode with two leaf children.
        """
        t = BTNode(5, BTNode(4), BTNode(3))
        self.assertEqual(sum_internal(t), 5, "sum_internal should sum all " +
                         "of the internal nodes in the entire BTNode.")

    @given(recursive(none() | integers(min_value=0, max_value=100),
                     lambda children: tuples(integers(min_value = 0,
                                                      max_value = 100),
                                             children,
                                             children))
           )
    def test_sum_internal(self, tuple_tree):
        """
        Test sum_internal on a randomly generated BTNode.
        """
        (t, expected) = tuples_to_tree(tuple_tree)
        actual = sum_internal(t)
        self.assertEqual(actual, expected,
                         ("test_sum_internal on BTNode\n{}\nReturned {}" +
                          " instead of {}.").format(tuple_tree, actual,
                                                    expected))


if __name__ == '__main__':
    unittest.main()

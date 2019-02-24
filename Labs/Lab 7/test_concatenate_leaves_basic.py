import unittest

from extra_practice import concatenate_leaves
from hypothesis import given
from hypothesis.strategies import recursive
from hypothesis.strategies import text
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
        return (None, '')

    if type(t) == str:
        return (BTNode(t), t)

    (left, l_count) = tuples_to_tree(t[1])
    (right, r_count) = tuples_to_tree(t[2])
    concatenate_leaves = l_count + r_count

    if not left and not right:
        concatenate_leaves = t[0]

    return (BTNode(t[0], left, right), concatenate_leaves)


class ConcatenateLeavesTests(unittest.TestCase):
    def test_returns_int(self):
        """
        Test concatenate_leaves to make sure it returns an int.
        """
        return_type = type(concatenate_leaves(BTNode("a")))

        self.assertEqual(return_type, str,
                         "concatenate_leaves should return type " +
                         "int, but instead returned type {}.".format(
                             return_type))

    def test_none(self):
        """
        Test concatenate_leaves on None.
        """
        self.assertEqual(concatenate_leaves(None), "",
                         "concatenate_leaves on None should " +
                         "return ''.")

    def test_leaf(self):
        """
        Test concatenate_leaves on a leaf.
        """
        self.assertEqual(concatenate_leaves(BTNode("a")), "a",
                         "concatenate_leaves should" +
                         " return the leaf's data when used on a leaf.")

    def test_one_left_child(self):
        """
        Test concatenate_leaves on a BTNode with one left child.
        """
        t = BTNode("a", BTNode("b"))
        self.assertNotEqual(concatenate_leaves(t), "ab",
                            "concatenate_leaves should not " +
                            "count None or any BTNodes with children as" +
                            " leaf nodes.")
        self.assertNotEqual(concatenate_leaves(t), "a",
                            "concatenate_leaves should not " +
                            "count None or any BTNodes with children as" +
                            " leaf nodes.")
        self.assertEqual(concatenate_leaves(t), "b",
                         "concatenate_leaves should return the " +
                         "data of the leaf child when used on a BTNode " +
                         "with a single leaf child.")

    def test_one_right_child(self):
        """
        Test concatenate_leaves on a BTNode with one right child
        """
        t = BTNode("a", None, BTNode("b"))
        self.assertNotEqual(concatenate_leaves(t), "ab",
                            "concatenate_leaves should not " +
                            "count None or any BTNodes with children as" +
                            " leaf nodes.")
        self.assertNotEqual(concatenate_leaves(t), "a",
                            "concatenate_leaves should not " +
                            "count None or any BTNodes with children as" +
                            " leaf nodes.")
        self.assertEqual(concatenate_leaves(t), "b",
                         "concatenate_leaves should return the " +
                         "data of the leaf child when used on a BTNode " +
                         "with a single leaf child.")

    def test_two_leaf_children(self):
        """
        Test concatenate_leaves on a BTNode with two leaf children.
        """
        t = BTNode("a", BTNode("b"), BTNode("c"))
        self.assertEqual(concatenate_leaves(t), "bc",
                         "concatenate_leaves should sum all " +
                         "of the leaves in the entire BTNode.")

    @given(recursive(none() | text(max_size=3),
                     lambda children: tuples(text(max_size = 3),
                                             children,
                                             children))
           )
    def test_concatenate_leaves(self, tuple_tree):
        """
        Test concatenate_leaves on a randomly generated BTNode.
        """
        (t, expected) = tuples_to_tree(tuple_tree)
        actual = concatenate_leaves(t)
        self.assertEqual(actual, expected,
                         ("test_concatenate_leaves on BTNode\n{}" +
                          "\nReturned {}" +
                          " instead of {}.").format(tuple_tree, actual,
                                                    expected))


if __name__ == '__main__':
    unittest.main()

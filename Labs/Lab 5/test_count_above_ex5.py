"""
count above unit tests
"""
import unittest
from typing import List
from hypothesis import given
from hypothesis.strategies import integers
from hypothesis.strategies import lists
from ex5 import count_above


def create_nested_list(list_values: list, nested_index_sets: List[List[int]]) -> list:
    """
    Create nested lists from values in list_values and indices in nested_index_sets.

    To clarify: Initially, the first two indices in nested_index_sets[0] will
    be taken (referred to as 'start' and 'end'), and list_values[start:end] will
    be replaced with a sublist containing values from list_values[start:end].
    Once all indices in nested_index_sets[0] are used, the resulting list will
    be used and sublists formed using indices in nested_index_sets[1].

    Precondition: All of the lists in nested_index_sets are sorted.

    >>> create_nested_list([0, 1, 2, 3, 4], [[0, 2, 3, 4]])
    [[0, 1], 2, [3], 4]
    >>> create_nested_list([0, 1, 2, 3, 4], [[0, 2], [0, 2]])
    [[[0, 1], 2], 3, 4]
    >>> create_nested_list([0, 1, 2, 3, 4], [[0, 2, 3, 4], [0, 4]])
    [[[0, 1], 2, [3]], 4]
    """

    nested_list_values = []

    list_to_add_to = nested_list_values
    list_to_use = list_values

    sublist = []
    finished_forming_sublist = True

    return_list = []

    for n in range(len(nested_index_sets)):
        nested_indices = nested_index_sets[n]

        if n == len(nested_index_sets) - 1:
            list_to_add_to = return_list

        for i in range(len(list_to_use)):
            if nested_indices:
                if i == nested_indices[0]:
                    nested_indices.pop(0)
                    finished_forming_sublist = not finished_forming_sublist

                    sublist.append(list_to_use[i])

                    # Add the formed sublist into nested_list_values
                    if finished_forming_sublist:
                        list_to_add_to.append(sublist)
                        sublist = []

                    if nested_indices and nested_indices[0] == i:
                        finished_forming_sublist = True
                        list_to_add_to.append(sublist)
                        sublist = []
                        while nested_indices and nested_indices[0] == i:
                            nested_indices.pop(0)
                else:
                    if not finished_forming_sublist:
                        sublist.append(list_to_use[i])
                    else:
                        # We're not forming a sublist at the moment, so
                        # append to nested_list_values.
                        list_to_add_to.append(list_to_use[i])
            else:
                if not finished_forming_sublist:
                    list_to_add_to.append(sublist)
                    sublist = []
                    finished_forming_sublist = True

                list_to_add_to.append(list_to_use[i])

        if not finished_forming_sublist:
            list_to_add_to.append(sublist)
            sublist = []
            finished_forming_sublist = True

        list_to_use = list_to_add_to
        list_to_add_to = []

    return return_list


class CountAboveTests(unittest.TestCase):
    def test_returns_int(self):
        """
        Test count_above to make sure it returns an int.
        """
        return_type = type(count_above(1, 2))
        self.assertEqual(return_type, int, "count_above should return type " +
                         "int, but instead returned type {}.".format(
                             return_type))

        return_type = type(count_above([1], 2))
        self.assertEqual(return_type, int, "count_above should return type " +
                         "int, but instead returned type {}.".format(
                             return_type))

    def test_smaller_integer(self):
        """
        Test count_above on an integer <= n.
        """
        self.assertEqual(count_above(2, 2), 0, "count_above should return 0 " +
                         "when passed an integer <= n.")

    def test_larger_integer(self):
        """
        Test count_above on an integer > n
        """
        self.assertEqual(count_above(2, 1), 1, "count_above should return 1 " +
                         "when given an integer > n.")

    def test_one_nested_sublist(self):
        """
        Test count_above on a list with only one sublist in it.
        """
        self.assertEqual(count_above([[2]], 1), 1, "count_above should return" +
                         " the number of integers > n in nested sublists.")

    def test_one_nested_sublist_and_integers(self):
        """
        Test count_above on a list with at most one level of nested sublists in
        it mixed with integers.
        """
        self.assertEqual(count_above([[2], 3, [4]], 2), 2,
                         "count_above should return the number of integers " +
                         "> n in nested sublists and in the list passed " +
                         "in.")

    @given(lists(integers(min_value = 0, max_value = 100), max_size = 20),
           lists(integers(min_value = 0, max_value = 20), min_size = 1,
                 max_size = 20),
           integers(min_value = -1))
    def test_count_even(self, list_values, list_indices, n):
        """
        Test the submitted count_even against a randomly generated list.
        """

        # Gather all of the even values
        expected = 0
        for i in list_values:
            if i > n:
                expected += 1

        # Create up to 2 levels of nesting for the values in list_values, where
        # the indices we turn into sublists are contained in
        # nesting_indices_1 and nesting_indices_2
        nesting_indices_1 = list_indices[:len(list_indices)//2]
        nesting_indices_2 = list_indices[len(list_indices)//2:]
        nesting_indices_1.sort()
        nesting_indices_2.sort()

        obj = create_nested_list(list_values, [nesting_indices_1,
                                               nesting_indices_2])

        # Ignoring the order of the values, in case students have an
        # out-of-order version for some reason.
        actual = count_above(obj, n)

        self.assertEqual(actual, expected,
                         ("Using count_above with n = {} on {} returned" +
                          " {} instead of {}.").format(n, obj, actual, expected)
                         )


if __name__ == "__main__":
    unittest.main()

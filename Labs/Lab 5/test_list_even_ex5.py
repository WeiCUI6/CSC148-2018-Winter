"""
unit tests for list_even
"""
import unittest
from hypothesis import given
from hypothesis.strategies import integers
from hypothesis.strategies import lists
from ex5 import list_even


def create_nested_list(list_values, nested_index_sets):
    """
    Create nested lists containing the values in list_values based on the
    indices to turn into sublists in nested_index_sets.

    To clarify: Initially, the first two indices in nested_index_sets[0] will
    be taken (referred to as 'start' and 'end'), and list_values[start:end] will
    be replaced with a sublist containing values from list_values[start:end].
    Once all indices in nested_index_sets[0] are used, the resulting list will
    be used and sublists formed using indices in nested_index_sets[1].

    Precondition: All of the lists in nested_index_sets are sorted.

    @param list list_values: The non-list values in the list to be returned.
    @param list[list[int]]: Lists containing the indices to turn into sublists.
    @rtype list[obj]
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


class ListEvenTests(unittest.TestCase):
    def test_returns_list(self):
        """
        Test list_even to make sure it returns a list.
        """
        return_type = type(list_even(1))
        self.assertEqual(return_type, list, "list_even should return type " +
                         "list, but instead returned type {}.".format(
                             return_type))

    def test_odd_integer(self):
        """
        Test list_even on an odd integer.
        """
        self.assertEqual(list_even(1), [], "list_even should return an empty " +
                         "list when passed an odd integer.")

    def test_even_integer(self):
        """
        Test list_even on an even integer.
        """
        self.assertEqual(list_even(2), [2], "list_even should return a " +
                         "list containing the even integer passed in when " +
                         "given an even integer.")


    def test_one_nested_sublist(self):
        """
        Test list_even on a list with only one sublist in it.
        """
        self.assertEqual(list_even([[2]]), [2], "list_even should return " +
                         "the even integers in nested sublists.")


    def test_one_nested_sublist_and_integers(self):
        """
        Test list_even on a list with at most one level of nested sublists in
        it mixed with integers.
        """
        self.assertEqual(list_even([[2], 3, [4]]), [2, 4],
                         "list_even should return the even integers in nested" +
                         " sublists and in the list passed in.")


    @given(lists(integers(min_value = 0, max_value = 100), max_size = 20),
           lists(integers(min_value = 0, max_value = 20), min_size = 1,
                 max_size = 20))
    def test_list_even(self, list_values, list_indices):
        """
        Test the submitted list_even against a randomly generated list.
        """

        # Gather all of the even values
        expected = []
        for n in list_values:
            if n % 2 == 0:
                expected.append(n)
        expected.sort()

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
        actual = list_even(obj)
        actual.sort()

        self.assertEqual(actual, expected,
                         ("Using list_even on {} returned" +
                          " {} instead of {}.").format(obj, actual, expected))

if __name__ == "__main__":
    unittest.main()

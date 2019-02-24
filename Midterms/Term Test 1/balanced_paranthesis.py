""" use a stack to check whether parentheses are balanced
"""
from stack_api import Stack


def balanced_delimiters(s: str) -> bool:
    """
    Return whether the delimiters in string s
    are balanced.

    Assume: Only delimiters are brackets, parentheses, braces

    >>> balanced_delimiters("[({])}")
    False
    >>> balanced_delimiters("[({})]]")
    False
    >>> balanced_delimiters("[[]")
    False
    >>> balanced_delimiters("[(){}]")
    True
    """
    st = Stack()
    left_delim = {")": "(", "]": "[", "}": "{"}
    for c in s:
        if c not in "()[]{}":
            pass
        elif c in "([{":
            st.add(c)
        elif not st.is_empty():
            assert c in ")]}"
            if left_delim[c] != st.remove():
                    return False
        else:
            return False
            pass
    return st.is_empty()


if __name__ == '__main__':
    import doctest
    doctest.testmod()

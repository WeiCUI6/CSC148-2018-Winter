"""
super class state
"""
from typing import Any
from typing import List


class State:
    """
    class State
    """
    is_p1_turn: bool
    is_game_over: bool

    def __init__(self, is_p1_turn: bool) -> None:
        """
        initialzie a superclass state

        >>> state1 = State(True)
        >>> state2 = State(False)
        """
        self.is_p1_turn = is_p1_turn
        self.is_game_over = False

    def __eq__(self, other: Any) -> bool:
        """
        return whether self is equal to other

        >>> a1 = State(True)
        >>> a2 = State(False)
        >>> a1 == a2
        False
        >>> a3 = 3
        >>> a1 == a3
        False
        >>> a4 = State(True)
        >>> a1 == a4
        True
        """
        return (type(self) == type(other)
                and self.is_p1_turn == other.is_p1_turn
                and self.is_game_over == other.is_game_over)

    def __str__(self) -> str:
        """
        return a str representation of class State
        """
        raise NotImplementedError("subclass needed")

    def get_possible_moves(self) -> List:
        """
        get possible moves of the current game state
        """
        raise NotImplementedError("subclass needed")

    def is_valid_move(self, move_to_take: Any) -> bool:
        """
        whether a move is a valid move based on the rules of the game
        """
        raise NotImplementedError("subclass needed")

    def get_current_player_name(self) -> str:
        """
        get the current player name

        >>> is_p1_turn = True
        >>> state1 = State(is_p1_turn)
        >>> state1.get_current_player_name()
        'p1'
        >>> is_p1_turn = False
        >>> state2 = State(is_p1_turn)
        >>> state2.get_current_player_name()
        'p2'
        """
        if self.is_p1_turn:
            return 'p1'
        return 'p2'

    def make_move(self, move_to_make: Any):
        """
        make a move to play the game
        """
        raise NotImplementedError("subclass needed")


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")

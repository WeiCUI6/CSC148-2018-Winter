"""
subclass of State: Subtract_Square_State
"""
from typing import Any, List
from state import State


class SubtractSquareState(State):
    """
    subclass of State, game SubtractSquare
    """
    starting_number: int

    def __init__(self, p1: bool, starting_number=-1) -> None:
        """
        initialize a new game state for SubtractSquare game.

        >>> is_p1_turn = True
        >>> s1 = SubtractSquareState(is_p1_turn, 20)
        >>> is_p1_turn = False
        >>> s2 = SubtractSquareState(is_p1_turn, 30)
        """
        State.__init__(self, p1)
        if starting_number == -1:
            self.starting_number = int(input("Choose a non-negtive whole number"
                                             ":"))
        else:
            self.starting_number = starting_number
        if self.starting_number == 0:
            self.is_game_over = True
            if self.is_p1_turn:
                self.is_p1_turn = False
            else:
                self.is_p1_turn = True

    def __eq__(self, other: Any) -> bool:
        """
        return whether self is equal to other.

        >>> is_p1_turn = True
        >>> s1 = SubtractSquareState(is_p1_turn, 20)
        >>> s2 = SubtractSquareState(is_p1_turn, 30)
        >>> s1 == s2
        False
        >>> a1 = 7
        >>> a2 = 'few'
        >>> a1 == s1
        False
        >>> a2 == s2
        False
        >>> s3 = SubtractSquareState(is_p1_turn, 20)
        >>> s1 == s3
        True
        """
        return (State.__eq__(self, other)
                and self.starting_number == other.starting_number)

    def __str__(self) -> str:
        """
        return a str representation of game SubtractSquare state.

        >>> is_p1_turn = True
        >>> s2 = SubtractSquareState(is_p1_turn, 20)
        >>> print(s2)
        The current player is: p1, and the current value is: 20
        """
        return "The current player is: {}, and the current value is: " \
               "{}".format(self.get_current_player_name(), self.starting_number)

    def get_possible_moves(self) -> List:
        """
        get possible moves based on current value

        >>> is_p1_turn = True
        >>> s1 = SubtractSquareState(is_p1_turn, 20)
        >>> s1.get_possible_moves()
        [1, 4, 9, 16]
        >>> s2 = SubtractSquareState(is_p1_turn, 30)
        >>> s2.get_possible_moves()
        [1, 4, 9, 16, 25]
        >>> s3 = SubtractSquareState(is_p1_turn, 25)
        >>> s3.get_possible_moves()
        [1, 4, 9, 16, 25]
        """
        if self.starting_number == 1:
            possible_moves = [1]
        elif self.starting_number > 1:
            possible_moves = [i ** 2 for i in range(1, self.starting_number)
                              if i ** 2 <= self.starting_number]
        else:
            return []
        return possible_moves

    def is_valid_move(self, move_to_take: Any) -> bool:
        """
        return whether a move_to_make is a valid move for player based on
        the rules of game

        >>> is_p1_turn = True
        >>> s1 = SubtractSquareState(is_p1_turn, 30)
        >>> s1.is_valid_move('25')
        False
        >>> s1.is_valid_move(25)
        True
        >>> s1.is_valid_move(12.3435)
        False
        >>> s1.is_valid_move(None)
        False
        """
        return move_to_take in self.get_possible_moves()

    def get_current_player_name(self) -> str:
        """
        get current player name

        >>> is_p1_turn = True
        >>> s1 = SubtractSquareState(is_p1_turn, 20)
        >>> s1.get_current_player_name()
        'p1'
        >>> is_p1_turn = False
        >>> s2 = SubtractSquareState(is_p1_turn, 30)
        >>> s2.get_current_player_name()
        'p2'
        """
        return State.get_current_player_name(self)

    def make_move(self, move_to_make: int) -> 'SubtractSquareState':
        """
        make move for the game

        >>> is_p1_turn = True
        >>> s1 = SubtractSquareState(is_p1_turn, 30)
        >>> s1.make_move(16).is_p1_turn
        False
        >>> s1.make_move(16).starting_number
        14
        >>> s1.make_move(16).is_game_over
        False
        >>> s1.make_move(16).get_possible_moves()
        [1, 4, 9]
        >>> s1.make_move(16).get_current_player_name()
        'p2'
        >>> s2 = SubtractSquareState(is_p1_turn, 1)
        >>> s2.make_move(1).get_current_player_name()
        'p1'
        """
        current_number = self.starting_number - move_to_make
        current_player = self.is_p1_turn
        is_game_current_over = self.is_game_over
        if current_number <= 0:
            is_game_current_over = True
        else:
            if current_player:
                current_player = False
            else:
                current_player = True
        new_state = SubtractSquareState(current_player, current_number)
        new_state.is_p1_turn = current_player
        new_state.is_game_over = is_game_current_over
        return new_state


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")

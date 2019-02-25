"""
module game Subtract_Square
"""
from typing import Any
from subtract_square_state import SubtractSquareState


class SubtractSquare:
    """
    class game SubtractSquare
    """
    current_state: SubtractSquareState

    def __init__(self, is_p1_turn: bool) -> None:
        """
        initialize a new subtractsquare game

        #A docstring example is not needed for any functions or methods that
        use input() or random.
        """
        self.current_state = SubtractSquareState(is_p1_turn)

    def __eq__(self, other: Any) -> bool:
        """
        return whether self is equivalent to other

        # A docstring example is not needed for any functions or methods that
        use input() or random.
        """
        return (type(self) == type(other)
                and self.current_state.is_game_over ==
                other.current_state.is_game_over
                and self.current_state.starting_number ==
                other.current_state.starting_number
                and self.current_state.is_p1_turn ==
                other.current_state.is_p1_turn)

    def __str__(self) -> str:
        """
        return a str representation of self

        # A docstring example is not needed for any functions or methods that
        use input() or random.
        """
        return "The current player is: {}, and the current value is: " \
               "{}".format(self.current_state.get_current_player_name(),
                           self.current_state.starting_number)

    def get_instructions(self) -> str:
        """
        reutrn instruction of game for players

        # A docstring example is not needed for any functions or methods that
        use input() or random.
        """
        instruction = 'Players take turns subtracting square numbers ' \
                      'from the starting number. The winner is the person ' \
                      'who subtracts to 0'
        return instruction

    def is_over(self, current_state: SubtractSquareState) -> bool:
        """
        return whether this game is over

        # A docstring example is not needed for any functions or methods that
        use input() or random.
        """
        return current_state.is_game_over

    def str_to_move(self, move: str) -> int:
        """
        a method whcih converts a string into a move

        # A docstring example is not needed for any functions or methods that
        use input() or random.
        """
        return int(move)

    def is_winner(self, player: str) -> bool:
        """
        return which player is the winner

        # A docstring example is not needed for any functions or methods that
        use input() or random.
        """
        if not self.current_state.is_game_over:
            return False
        else:
            if self.current_state.is_p1_turn:
                if player == 'p1':
                    return True
                return False
            else:
                if player == 'p2':
                    return True
                return False


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")

"""
module strategy for game players
"""

import random
from typing import Any


def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def random_strategy(game: Any) -> Any:
    """
    return a move for game randomly
    """
    return random.choice(game.current_state.get_possible_moves())


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")

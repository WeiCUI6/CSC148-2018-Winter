"""
An implementation of a state for SubtractSquare.

NOTE: You do not have to run python-ta on this file.
"""
from typing import Any
from game_state import GameState


class SubtractSquareState(GameState):
    """
    The state of a game at a certain point in time.
    """

    def __init__(self, is_p1_turn: bool, current_total: int) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.
        """
        super().__init__(is_p1_turn)
        self.current_total = current_total

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        """
        return "Current total: {}".format(self.current_total)

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        """
        moves = []
        for i in range(1, self.current_total + 1):
            if i ** 2 <= self.current_total:
                moves.append(i ** 2)

        return moves

    def make_move(self, move: Any) -> "SubtractSquareState":
        """
        Return the GameState that results from applying move to this GameState.
        """
        if type(move) == str:
            move = int(move)

        new_state = SubtractSquareState(not self.p1_turn,
                                        self.current_total - move)
        return new_state

    def __repr__(self) -> str:
        """
        Return a representation of this state (which can be used for
        equality testing).
        """
        return "P1's Turn: {} - Total: {}".format(self.p1_turn,
                                                  self.current_total)

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        """
        if is_pos_square(self.current_total):
            return self.WIN
        elif all([is_pos_square(self.current_total - n ** 2)
                  for n in range(1, self.current_total + 1)
                  if n ** 2 < self.current_total]):
            return self.LOSE

        return self.DRAW


def is_pos_square(n: int) -> bool:
    """
    Return whether n is a positive perfect square

    >>> is_pos_square(5)
    False
    >>> is_pos_square(9)
    True
    """
    return 0 < n and (round(n ** 0.5) ** 2 == n)


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")

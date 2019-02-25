"""
An implementation of Subtract Square.

NOTE: You do not have to run python-ta on this file.
"""
from game import Game
from subtract_square_state import SubtractSquareState


class SubtractSquareGame(Game):
    """
    Abstract class for a game to be played with two players.
    """

    def __init__(self, p1_starts):
        """
        Initialize this Game, using p1_starts to find who the first player is.

        :param p1_starts: A boolean representing whether Player 1 is the first
                          to make a move.
        :type p1_starts: bool
        """
        count = int(input("Enter the number to subtract from: "))
        self.current_state = SubtractSquareState(p1_starts, count)

    def get_instructions(self):
        """
        Return the instructions for this Game.

        :return: The instructions for this Game.
        :rtype: str
        """
        instructions = "Players take turns subtracting square numbers from" + \
            " the starting number. The winner is the person who subtracts to 0."
        return instructions

    def is_over(self, state):
        """
        Return whether or not this game is over.

        :return: True if the game is over, False otherwise.
        :rtype: bool
        """
        return state.current_total == 0

    def is_winner(self, player):
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.

        :param player: The player to check.
        :type player: str
        :return: Whether player has won or not.
        :rtype: bool
        """
        return (self.current_state.get_current_player_name() != player
                and self.is_over(self.current_state))

    def str_to_move(self, string):
        """
        Return the move that string represents. If string is not a move,
        return an invalid move.

        :param string:
        :type string:
        :return:
        :rtype:
        """
        if not string.strip().isdigit():
            return -1

        return int(string.strip())


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")

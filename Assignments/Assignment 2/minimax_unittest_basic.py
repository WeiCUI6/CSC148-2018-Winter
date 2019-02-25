"""
A subset of unittests used for testing minimax.

These unittests only test for basic functionality and whether we can properly
test your strategies. They are not a guarantee that your code works flawlessly,
so please make sure to test your code yourself.

For minimax, the runtime (especially for Stonehenge) can be quite long. The
tests we provided should finish running within a minute, but are also contingent
on a correct implementation of Stonehenge.

When we test your code, we will NOT rely on your implementation of Stonehenge
or SubtractSquare. We will be testing it on the ideal implementation of the
games. Thus: If your Stonehenge implementation does not work but you pass the
SubtractSquare minimax tests, you might be okay for passing the minimax tests.

We will NOT test minimax on Chopsticks, and you shouldn't be using the minimax
strategy with Chopsticks either, unless you handle repeated/looping states.
"""

import unittest
from unittest.mock import patch
import inspect

# Import the student solution
from game_interface import playable_games, usable_strategies
minimax_iterative_strategy = usable_strategies['mi']
minimax_recursive_strategy = usable_strategies['mr']
StonehengeGame = playable_games['h']
SubtractSquareGame = playable_games['s']

STONEHENGE_MINIMAX_BOARD = """\
          2   1
         /   /
    1 - 1 - 1   @
       / \\ / \\ /
  1 - 2 - 1 - 1   2
     / \\ / \\ / \\ /
2 - 2 - 2 - H - 2
     \\ / \\ / \\ / \\
  @ - J - 2 - L   1
       \\   \\   \\
        2   2   1
"""

class MinimaxUnitTests(unittest.TestCase):
    def test_iterative_subtract_square_4(self):
        """
        Test iterative minimax on a game of SubtractSquare with a value of 4.
        The winning move is immediately in sight.
        """
        with patch('builtins.input', return_value='4'):
            game = SubtractSquareGame(True)

        move_chosen = minimax_iterative_strategy(game)
        expected_move = game.str_to_move("4")

        self.assertEqual(move_chosen, expected_move,
                         ("Calling iterative minimax on a game of " +
                          "SubtractSquare with " +
                          "a value of {} should result in the move {} " +
                          "being returned, but {} was returned instead.").format(
                             4, expected_move, move_chosen
                         ))

    def test_iterative_subtract_square_18(self):
        """
        Test iterative minimax on a game of SubtractSquare with a value of 18.
        The winning move is a few turns away.

        The chosen move should be 16 or 1, as picking 4 or 9 will result in a
        loss.
        """
        with patch('builtins.input', return_value='18'):
            game = SubtractSquareGame(True)

        move_chosen = minimax_iterative_strategy(game)
        expected_moves = [game.str_to_move("1"), game.str_to_move("16")]

        self.assertTrue(move_chosen in expected_moves,
                        ("Calling iterative minimax on a game of " +
                         "SubtractSquare with " +
                         "a value of {} should result in a move in {} " +
                         "being returned, but {} was returned instead.").format(
                            18, expected_moves, move_chosen
                         ))

    def test_iterative_stonehenge_one_winning_move(self):
        """
        Test iterative minimax on a game of Stonehenge where there is only 1
        winning move that is immediately in sight.
        """

        with patch('builtins.input', return_value='3'):
            game = StonehengeGame(False)

        moves_to_make = ['K', 'A', 'C', 'B', 'F', 'E', 'G', 'D', 'I']
        for move in moves_to_make:
            game.current_state = game.current_state.make_move(
                game.str_to_move(move))

        move_chosen = minimax_iterative_strategy(game)
        expected_moves = [game.str_to_move("H")]
        self.assertTrue(move_chosen in expected_moves,
                        ("Calling iterative minimax on a game of Stonehenge" +
                         " with " +
                         "the following board should return a move in {} " +
                          "but got {} instead.\n{}").format(
                             expected_moves, move_chosen,
                             STONEHENGE_MINIMAX_BOARD
                         ))

    def test_iterative_stonehenge_one_winning_move_not_immediate(self):
        """
        Test iterative minimax on a game of Stonehenge where there is only 1
        winning move that is not immediately in sight.
        """

        with patch('builtins.input', return_value='2'):
            game = StonehengeGame(True)

        moves_to_make = ['A', 'F', 'D']
        for move in moves_to_make:
            game.current_state = game.current_state.make_move(
                game.str_to_move(move))
        new_state = game.current_state

        expected_move = game.str_to_move('E')

        move_chosen = minimax_iterative_strategy(game)

        self.assertEqual(move_chosen, expected_move,
                         ("Calling iterative minimax on a game of Stonehenge" +
                          " with " +
                          "the following board should return the move {} " +
                          "but got {} instead.\n{}").format(
                             expected_move, move_chosen, str(new_state)
                         ))

    def test_recursive_subtract_square_4(self):
        """
        Test recursive minimax on a game of SubtractSquare with a value of 4.
        The winning move is immediately in sight.
        """
        with patch('builtins.input', return_value='4'):
            game = SubtractSquareGame(True)

        move_chosen = minimax_recursive_strategy(game)
        expected_move = game.str_to_move("4")

        self.assertEqual(move_chosen, expected_move,
                         ("Calling recursive minimax on a game of " +
                          "SubtractSquare with " +
                          "a value of {} should result in the move {} " +
                          "being returned, but {} was returned instead.").format(
                             4, expected_move, move_chosen
                         ))

    def test_recursive_subtract_square_18(self):
        """
        Test recursive minimax on a game of SubtractSquare with a value of 18.
        The winning move is a few turns away.

        The chosen move should be 16 or 1, as picking 4 or 9 will result in a
        loss.
        """
        with patch('builtins.input', return_value='18'):
            game = SubtractSquareGame(True)

        move_chosen = minimax_recursive_strategy(game)
        expected_moves = [game.str_to_move("1"), game.str_to_move("16")]

        self.assertTrue(move_chosen in expected_moves,
                        ("Calling recursive minimax on a game of " +
                         "SubtractSquare with " +
                         "a value of {} should result in a move in {} " +
                         "being returned, but {} was returned instead.").format(
                            18, expected_moves, move_chosen
                        ))

    def test_recursive_stonehenge_one_winning_move(self):
        """
        Test recursive minimax on a game of Stonehenge where there is only 1
        winning move that is immediately in sight.
        """

        with patch('builtins.input', return_value='3'):
            game = StonehengeGame(False)

        moves_to_make = ['K', 'A', 'C', 'B', 'F', 'E', 'G', 'D', 'I']
        for move in moves_to_make:
            game.current_state = game.current_state.make_move(
                game.str_to_move(move))

        move_chosen = minimax_recursive_strategy(game)
        expected_moves = [game.str_to_move("H")]
        self.assertTrue(move_chosen in expected_moves,
                        (
                        "Calling recursive minimax on a game of Stonehenge" +
                        " with " +
                        "the following board should return a move in {} " +
                        "but got {} instead.\n{}").format(
                            expected_moves, move_chosen,
                            STONEHENGE_MINIMAX_BOARD
                        ))

    def test_recursive_stonehenge_one_winning_move_not_immediate(self):
        """
        Test recursive minimax on a game of Stonehenge where there is only 1
        winning move that is not immediately in sight.
        """

        with patch('builtins.input', return_value='2'):
            game = StonehengeGame(True)

        moves_to_make = ['A', 'F', 'D']
        for move in moves_to_make:
            game.current_state = game.current_state.make_move(
                game.str_to_move(move))
        new_state = game.current_state

        expected_move = game.str_to_move('E')

        move_chosen = minimax_recursive_strategy(game)

        self.assertEqual(move_chosen, expected_move,
                         (
                         "Calling recursive minimax on a game of Stonehenge" +
                         " with " +
                         "the following board should return the move {} " +
                         "but got {} instead.\n{}").format(
                             expected_move, move_chosen, str(new_state)
                         ))

if __name__ == "__main__":
    unittest.main()

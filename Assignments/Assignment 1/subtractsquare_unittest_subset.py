import unittest
from unittest.mock import patch

import re

# Import the student solution
from game_interface import playable_games
SubtractSquareGame = playable_games['s']

SUBTRACT_SQUARE_FORMAT = ".*(?<=[^0-9])([0-9]+)"


class SubtractSquareUnitTests(unittest.TestCase):
    def extract_subtract_square_value(self, state):
        """
        A helper function that returns the value of a Subtract Square state
        given its string representation.

        Precondition: str(state) ends in a number.
        """
        state_str = str(state)
        str_group = re.search(SUBTRACT_SQUARE_FORMAT, state_str).group(1)
        state_value = int(str_group)
        return state_value

    @patch('builtins.input', side_effect = ['20'])
    def test_subtractsquare_init(self, input):
        """
        Test to make sure SubtractSquare can be initialized with a boolean
        parameter and having the correct attributes/methods.
        """
        game = SubtractSquareGame(True)

        self.assertTrue(isinstance(game, SubtractSquareGame),
                        ("The game initialized with value 20 should be of " +
                         "type {} (the class mapped to by playable_games['s']" +
                         ") but an object of type {} was returned" +
                         " instead.").format(playable_games['s'].__name__,
                                             type(game).__name__))

        self.assertTrue(hasattr(game, 'current_state'), 'An initialized game ' +
                        'should have the attribute current_state.')

        self.assertTrue(hasattr(game, 'get_instructions'),
                        'An initialized game ' +
                        'should have the method get_instructions.')

        self.assertTrue(hasattr(game, 'is_over'), 'An initialized game ' +
                        'should have the method is_over.')

        self.assertTrue(hasattr(game, 'is_winner'), 'An initialized game ' +
                        'should have the method is_winner.')

        self.assertTrue(hasattr(game, 'str_to_move'), 'An initialized game ' +
                        'should have the method str_to_move.')

    @patch('builtins.input', side_effect = ['20', 'END'])
    def test_subtractsquare_takes_input(self, input):
        """
        Test to make sure SubtractSquare can be initialized, taking in a boolean
        as a parameter and requiring a number as input.
        """
        game = SubtractSquareGame(True)

        actual_patch = input()
        expected_patch = "END"

        self.assertEqual(actual_patch, expected_patch,
                         "When initializing a game of Subtract Square, one " +
                         "input (e.g. 20) should be taken in.")

    @patch('builtins.input', side_effect=['20'])
    def test_get_current_player_name_true(self, input):
        """
        Test get_current_player_name to ensure it returns "p1" if SubtractSquare
        was initialized with True for is_p1_turn.
        """
        game = SubtractSquareGame(True)
        self.assertEqual('p1', game.current_state.get_current_player_name(),
                         "Calling get_current_player_name() on a game " +
                         "initialized with 'True' as the parameter passed " +
                         "in should return 'p1'.")

    @patch('builtins.input', side_effect=['20'])
    def test_get_current_player_name_return(self, input):
        """
        Test the return type of get_current_player_name to ensure that it
        returns a string.
        """
        game = SubtractSquareGame(True)
        player_name = game.current_state.get_current_player_name()
        self.assertEqual(type(player_name), str, "get_current_player_name()" +
                         " should return a string.")

    @patch('builtins.input', side_effect=['0'])
    def test_is_over_true(self, input):
        """
        Test is_over to ensure that it returns True when the game is over.
        """
        game = SubtractSquareGame(True)
        is_over = game.is_over(game.current_state)
        self.assertTrue(is_over, "is_over() should return True when given " +
                        "a state that is over (e.g. a count of 0 for " +
                        "SubtractSquare).")

    @patch('builtins.input', side_effect=['20'])
    def test_is_winner_return(self, input):
        """
        Test the return type of is_winner to ensure that it returns a boolean.
        """
        game = SubtractSquareGame(True)
        is_winner = game.is_winner("p1")

        self.assertEqual(type(is_winner), bool,
                         "is_winner() should return a bool.")

    @patch('builtins.input', side_effect=['20'])
    def test_is_winner_not_over(self, input):
        """
        Test is_winner to ensure that it returns False when the game is not
        over.
        """
        game = SubtractSquareGame(True)
        is_winner = game.is_winner("p1") or game.is_winner("p2")

        self.assertFalse(is_winner, "Calling is_winner() on an unfinished " +
                         "game should return False.")

    @patch('builtins.input', side_effect=['1'])
    def test_is_winner_p2_false(self, input):
        """
        Test is_winner('p2') to ensure that it returns False when the game is
        over and p1 is the winner.
        """
        game = SubtractSquareGame(True)
        game.current_state = game.current_state.make_move(game.str_to_move("1"))
        is_winner = game.is_winner("p2")

        self.assertFalse(is_winner, "Calling is_winner('p2') on a game where " +
                         "p1 won should return False.")

    @patch('builtins.input', side_effect=['20'])
    def test_subtractsquare_str_return(self, input):
        """
        Test the return type of Subtract Square's __str__ method to make sure
        it returns a string.
        """
        game = SubtractSquareGame(True)
        actual = type(str(game.current_state))

        self.assertEqual(actual, str, ("Calling __str__ on a game's current " +
                                       "state should return a string but a {}" +
                                       " was returned instead.").format(actual))

    @patch('builtins.input', side_effect=['20'])
    def test_subtractsquare_format(self, input):
        """
        Test the str output of Subtract Square's state to make sure it ends
        in a number.
        """
        game = SubtractSquareGame(True)
        state_str = str(game.current_state)
        self.assertRegex(state_str, SUBTRACT_SQUARE_FORMAT,
                         ("The string format of a state in Subtract Square " +
                          "should end in a number that matches the current " +
                          "total in the game, but '{}' was returned " +
                          "instead.").format(state_str))

    @patch('builtins.input', side_effect=['20'])
    def test_subtractsquare_str(self, input):
        """
        Test the str output of Subtract Square's state to make sure the number
        is extracted correctly.
        """
        game = SubtractSquareGame(True)
        state_value = self.extract_subtract_square_value(game.current_state)
        self.assertEqual(state_value, 20,
                         ("The string form of a state in Subtract Square " +
                          "with a value of 20 should end with the number 20 " +
                          "but the value '{}' was found instead.").format(
                             state_value))

    @patch('builtins.input', side_effect=['20'])
    def test_subtractsquare_get_possible_moves(self, input):
        """
        Test get_possible_moves() to make sure it returns the correct set
        of moves for Subtract Square with a value of 20.
        """
        game = SubtractSquareGame(True)
        moves = game.current_state.get_possible_moves()

        self.assertEqual(4, len(moves),
                         ("get_possible_moves() on a game of Subtract Square" +
                          " with a value of 20 should return 4 moves, but " +
                          "{} were returned.").format(len(moves)))

        expected_results = [4, 11, 16, 19]
        resulting_states = []

        for move in moves:
            new_state = game.current_state.make_move(move)
            state_value = self.extract_subtract_square_value(new_state)
            resulting_states.append(state_value)

        resulting_states.sort()

        self.assertEqual(expected_results, resulting_states,
                         ("get_possible_moves() should return moves which " +
                          "result in states with values 4, 11, 16 or 19 but " +
                          "the resulting states had values of {} " +
                          "instead.").format(resulting_states))

    @patch('builtins.input', side_effect=['1'])
    def test_subtractsquare_make_move(self, input):
        """
        Test make_move() on Subtract Square to make sure it can apply a move and
        correctly return the next state.
        """
        game = SubtractSquareGame(True)
        moves = game.current_state.get_possible_moves()
        self.assertEqual(len(moves), 1, ("get_possible_moves() on a game of " +
                                         "Subtract Square with a value of 1 " +
                                         "should return 1 move, but instead " +
                                         "{} were returned.").format(len(moves))
                         )

        new_state = game.current_state.make_move(moves[0])
        state_value = self.extract_subtract_square_value(new_state)

        self.assertEqual(state_value, 0, "make_move() on a game of " +
                         "Subtract Square with a value of 1 should result " +
                         "in a state with a value of 0 (as the only possible " +
                         "valid move should be '1').")

    @patch('builtins.input', side_effect=['20'])
    def test_subtractsquare_str_to_move(self, input):
        """
        Test str_to_move() to make sure it returns moves that are in the
        moves from get_possible_moves().
        """
        game = SubtractSquareGame(True)
        moves = game.current_state.get_possible_moves()
        move = game.str_to_move("16")

        self.assertTrue(move in moves, "str_to_move('16') should produce a " +
                        "move that's in get_possible_moves() in a game with " +
                        "the value 20.")

    def test_make_move_keeps_state(self):
        """
        Test make_move() to make sure it doesn't modify the current_state of
        a game.
        """
        with patch('builtins.input', return_value=str(20)):
            game = SubtractSquareGame(True)

        original_state = self.extract_subtract_square_value(game.current_state)

        move_to_make = game.str_to_move("16")
        new_state = game.current_state.make_move(move_to_make)
        after_move_state = self.extract_subtract_square_value(game.current_state)

        self.assertEqual(original_state, after_move_state,
                         "After calling make_move, the current_state of a " +
                         "game should not be changed.")

    @patch('builtins.input', side_effect=['20'])
    def test_subtractsquare_is_valid_move_true(self, input):
        """
        Test is_valid_move() to make sure all of the possible moves are valid.
        """
        game = SubtractSquareGame(True)
        moves = game.current_state.get_possible_moves()

        for move in moves:
            self.assertTrue(game.current_state.is_valid_move(move),
                            "is_valid_move() should return True for all " +
                            "moves returned by get_possible_moves().")

    @patch('builtins.input', side_effect=['20'])
    def test_subtractsquare_is_valid_move_false(self, input):
        """
        Test is_valid_move() to make sure an invalid move (e.g. '8') is not
        valid.
        """
        game = SubtractSquareGame(True)
        move = game.str_to_move("8")

        self.assertFalse(game.current_state.is_valid_move(move),
                         "is_valid_move() should return False for a move " +
                         "that is invalid (e.g. '8').")

    @patch('builtins.input', side_effect=['20'])
    def test_current_player_changed(self, input):
        """
        Test to make sure the current player changes after a move is made.
        """

        game = SubtractSquareGame(True)
        moves = game.current_state.get_possible_moves()
        old_player = game.current_state.get_current_player_name()
        new_state = game.current_state.make_move(moves[0])
        new_player = new_state.get_current_player_name()

        self.assertNotEqual(old_player, new_player, "After a move is made " +
                            "the current player returned by " +
                            "get_current_player_name() shoud change.")

    @patch('builtins.input', side_effect=['20'])
    def test_str_to_move_syntactically_valid_nonsquare(self, input):
        """
        Test to make sure str_to_move can create a move from a syntactically
        valid string that is not a square.
        """
        game = SubtractSquareGame(True)
        move = game.str_to_move("5")
        move2 = game.str_to_move("9")
        self.assertEqual(type(move), type(move2),
                         ("Trying to call make_move on a string that is " +
                          "syntactically valid but is not logically valid " +
                          "(e.g. from the string '5') should return a move " +
                          "that is of the same type as a valid move."))

    @patch('builtins.input', side_effect=['20'])
    def test_str_to_move_syntactically_valid_square(self, input):
        """
        Test to make sure str_to_move can create a move from a syntactically
        valid string that is not a valid move.
        """
        game = SubtractSquareGame(True)
        move = game.str_to_move("25")
        move2 = game.str_to_move("9")
        self.assertEqual(type(move), type(move2),
                         ("Trying to call make_move on a string that is " +
                          "syntactically valid but is not logically valid " +
                          "(e.g. from the string '25' for a game of Subtract " +
                          "Square with a value of 20) should return a move " +
                          "that is of the same type as a valid move."))


if __name__ == "__main__":
    unittest.main()

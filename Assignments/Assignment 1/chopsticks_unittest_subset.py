import unittest
from unittest.mock import patch

import re

# Import the student solution
from game_interface import playable_games
ChopsticksGame = playable_games['c']

# A very ugly regex which searches for a version of:
#    ...A-B...C-D...
# Where A and B are the left and right-hand values of Player 1 respectively,
# and similarly for C and D and Player 2.
CHOPSTICKS_FORMAT = (".*(?<=[^0-9])([0-9]+)([\s\-]+)([0-9]+).*" +
                     "(?<=[^0-9])([0-9]+)([\s\-]+)([0-9]+)(?<=[^0-9])*")


class ChopsticksUnitTests(unittest.TestCase):
    def extract_chopsticks_value(self, state):
        """
        A helper function that returns the value of a Chopsticks state
        given its string representation.

        Precondition: str(state) follows CHOPSTICKS_FORMAT.
        """
        state_str = str(state)
        str_group = re.search(CHOPSTICKS_FORMAT, state_str)
        (p1_left, p1_right, p2_left, p2_right) = (str_group.group(1),
                                                  str_group.group(3),
                                                  str_group.group(4),
                                                  str_group.group(6))
        return (p1_left, p1_right, p2_left, p2_right)

    def apply_moves(self, game, moves):
        """
        A helper function that returns the state of game after a series of
        moves are applied to it.
        """
        state = game.current_state
        for move in moves:
            state = state.make_move(game.str_to_move(move))

        return state

    def parallel_list_sort(self, values_list, parallel_list):
        """
        A helper function that sorts values_list and make the same swaps to
        parallel_list.

        Uses bubble sort.
        """
        upper_limit = len(values_list) - 1
        swaps_made = True

        while swaps_made and upper_limit > 0:
            swaps_made = False
            for i in range(upper_limit):
                # Swap the item at i with i + 1 if i > i + 1
                if values_list[i] > values_list[i+1]:
                    (values_list[i], values_list[i + 1]) = (values_list[i + 1],
                                                            values_list[i])
                    (parallel_list[i], parallel_list[i + 1]) =\
                        (parallel_list[i + 1], parallel_list[i])
                    swaps_made = True
            upper_limit -= 1

    # === END OF HELPER FUNCTIONS ===

    def test_chopsticks_init(self):
        """
        Test to make sure Chopsticks can be initialized, taking in a boolean
        as a parameter.
        """
        game = ChopsticksGame(True)

        self.assertTrue(isinstance(game, ChopsticksGame),
                        ("An initialized game of Chopsticks should be of " +
                         "type {} (the class mapped to by playable_games['c']" +
                         ") but an object of type {} was returned" +
                         " instead.").format(playable_games['c'].__name__,
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

        state_value = self.extract_chopsticks_value(game.current_state)
        self.assertEqual(state_value, ('1', '1', '1', '1'),
                         ("An initialized game of Chopsticks should start " +
                          "with hand values of 1 for all of Player 1 and " +
                          "Player 2's hands, but the values for Player 1 " +
                          "were {} and the values for Player 2 were " +
                          "{}.").format((1, 1), (1, 1)))

    @patch('builtins.input', side_effect=['START', 'END'])
    def test_chopsticks_takes_no_input(self, input):
        """
        Test to make sure Chopsticks can be initialized, taking in a boolean
        as a parameter and takes no input.
        """
        game = ChopsticksGame(True)

        actual_patch = input()
        expected_patch = "START"

        self.assertEqual(actual_patch, expected_patch,
                         "When initializing a game of Chopsticks, no input " +
                         "should be taken in.")

    def test_get_current_player_name_true(self):
        """
        Test get_current_player_name to ensure it returns "p1" if Chopsticks
        was initialized with True for is_p1_turn.
        """
        game = ChopsticksGame(True)
        self.assertEqual('p1', game.current_state.get_current_player_name(),
                         "Calling get_current_player_name() on a game " +
                         "initialized with 'True' as the parameter passed " +
                         "in should return 'p1'.")

    def test_get_current_player_name_return(self):
        """
        Test the return type of get_current_player_name to ensure that it
        returns a string.
        """
        game = ChopsticksGame(True)
        player_name = game.current_state.get_current_player_name()
        self.assertEqual(type(player_name), str, "get_current_player_name()" +
                         " should return a string.")

    def test_is_over_true(self):
        """
        Test is_over to ensure that it returns True when the game is over.
        """
        game = ChopsticksGame(True)
        new_state = self.apply_moves(game,
                                     ["ll", "ll", "ll", "rl", "lr"])
        is_over = game.is_over(new_state)
        self.assertTrue(is_over, "is_over() should return True when given " +
                        "a state that is over (e.g. a player with both " +
                        "hands being 0 in Chopsticks).")

    def test_is_winner_return(self):
        """
        Test the return type of is_winner to ensure that it returns a boolean.
        """
        game = ChopsticksGame(True)
        is_winner = game.is_winner("p1")

        self.assertEqual(type(is_winner), bool,
                         "is_winner() should return a bool.")

    def test_is_winner_not_over(self):
        """
        Test is_winner to ensure that it returns False when the game is not
        over.
        """
        game = ChopsticksGame(True)
        is_winner = game.is_winner("p1") or game.is_winner("p2")

        self.assertFalse(is_winner, "Calling is_winner() on an unfinished " +
                         "game should return False.")

    def test_is_winner_p2_false(self):
        """
        Test is_winner('p2') to ensure that it returns False when the game is
        over and p1 is the winner.
        """
        game = ChopsticksGame(True)
        new_state = self.apply_moves(game,
                                     ["ll", "ll", "ll", "rl", "lr"])
        game.current_state = new_state
        is_winner = game.is_winner("p2")

        self.assertFalse(is_winner, "Calling is_winner('p2') on a game where " +
                         "p1 won should return False.")

    def test_chopsticks_str_return(self):
        """
        Test the return type of Chopsticks's __str__ method to make sure
        it returns a string.
        """
        game = ChopsticksGame(True)
        actual = type(str(game.current_state))

        self.assertEqual(actual, str, ("Calling __str__ on a game's current " +
                                       "state should return a string but a {}" +
                                       " was returned instead.").format(actual))

    def test_chopsticks_format(self):
        """
        Test the str output of Chopsticks's state to make sure it ends
        in a number.
        """
        game = ChopsticksGame(True)
        state_str = str(game.current_state)
        self.assertRegex(state_str, CHOPSTICKS_FORMAT,
                         ("The string format of a state in Chopsticks " +
                          "should contain 2 pairs of number separated by a " +
                          "hyphen (-) and possibly spaces, but the following " +
                          "string was returned instead:\n{}").format(state_str))

    def test_chopsticks_str(self):
        """
        Test the str output of Chopsticks's state to make sure the numbers
        are extracted correctly.
        """
        game = ChopsticksGame(True)
        state_value = self.extract_chopsticks_value(game.current_state)
        result_str = str(game.current_state)
        self.assertEqual(state_value, ('1', '1', '1', '1'),
                         ("The string of a state in Chopsticks with hands " +
                          "{} - {} for Player 1 and {} - {} for Player 2 " +
                          "should have those numbers (in that order), separated" +
                          " by hyphens (-) and possibly spaces, but the " +
                          "following string was returned instead:\n{}").format(
                             1, 1, 1, 1, result_str
                         ))

    def test_chopsticks_get_possible_moves(self):
        """
        Test get_possible_moves() to make sure it returns the correct set
        of moves for Chopsticks at its initial state.
        """
        game = ChopsticksGame(True)
        moves = game.current_state.get_possible_moves()

        self.assertEqual(4, len(moves),
                         ("get_possible_moves() on a game of Chopsticks" +
                          " with all hands having a value of 1 should " +
                          "return 4 moves, but {} were returned.").format(
                             len(moves)
                         ))

        expected_results = [('1', '1', '2', '1'),
                            ('1', '1', '1', '2'),
                            ('1', '1', '2', '1'),
                            ('1', '1', '1', '2')]
        resulting_states = []

        for move in moves:
            new_state = game.current_state.make_move(move)
            state_value = self.extract_chopsticks_value(new_state)
            resulting_states.append(state_value)

        expected_results.sort()
        resulting_states.sort()

        str_result = ""
        for state in resulting_states:
            str_result += "Player 1: {} - {}; Player 2: {} - {}\n".format(
                state[0],
                state[1],
                state[2],
                state[3]
            )

        self.assertEqual(expected_results, resulting_states,
                         ("get_possible_moves() on a newly initialized game " +
                          "of Chopsticks where Player 1 starts should result " +
                          "in states where Player 2's hands have the values " +
                          "2 - 1 or 1 - 2. However, the following states " +
                          "were returned instead:\n{}").format(str_result))

    def test_chopsticks_str_to_move(self):
        """
        Test str_to_move() to make sure it returns moves that are in the
        moves from get_possible_moves().
        """
        game = ChopsticksGame(True)
        moves = game.current_state.get_possible_moves()
        move = game.str_to_move("rl")

        self.assertTrue(move in moves, "str_to_move('rl') should produce a " +
                        "move that's in get_possible_moves() in a newly " +
                        "initialized game of Chopsticks.")

    def test_chopsticks_make_move(self):
        """
        Test make_move() on Chopsticks to make sure it can apply a move and
        correctly return the next state.
        """
        game = ChopsticksGame(True)
        moves = game.current_state.get_possible_moves()

        new_state = game.current_state.make_move(moves[0])
        state_value = self.extract_chopsticks_value(new_state)
        str_result = "Player 1: {} - {}; Player 2: {} - {}\n".format(
            state_value[0], state_value[1], state_value[2], state_value[3]
        )

        self.assertTrue(state_value in [('1', '1', '2', '1'),
                                        ('1', '1', '1', '2')],
                        ("make_move() with one of the moves from " +
                         "get_possible_moves() on a newly initialized game " +
                         "of Chopsticks should return a state with either " +
                         "the hands 1 - 2 or 2 - 1 for Player 2, leaving " +
                         "Player 1 unchanged. However, the following hands " +
                         "were found instead:\n{}").format(str_result))

    def test_make_move_keeps_state(self):
        """
        Test make_move() to make sure it doesn't modify the current_state of
        a game.
        """
        game = ChopsticksGame(True)

        original_state = self.extract_chopsticks_value(game.current_state)

        move_to_make = game.str_to_move("ll")
        new_state = game.current_state.make_move(move_to_make)
        after_move_state = self.extract_chopsticks_value(game.current_state)

        self.assertEqual(original_state, after_move_state,
                         "After calling make_move, the current_state of a " +
                         "game should not be changed.")

    def test_chopsticks_is_valid_move_true(self):
        """
        Test is_valid_move() to make sure all of the possible moves are valid.
        """
        game = ChopsticksGame(True)
        moves = game.current_state.get_possible_moves()

        for move in moves:
            self.assertTrue(game.current_state.is_valid_move(move),
                            "is_valid_move() should return True for all " +
                            "moves returned by get_possible_moves().")

    def test_chopsticks_is_valid_move_false(self):
        """
        Test is_valid_move() to make sure an invalid move (e.g. '8') is not
        valid.
        """
        game = ChopsticksGame(True)
        move = game.str_to_move("ll")
        new_state = self.apply_moves(game,
                                     ["ll", "ll", "ll"])

        self.assertFalse(new_state.is_valid_move(move),
                         "is_valid_move() should return False for a move " +
                         "that is invalid (e.g. 'll' when the current " +
                         "Player's left hand is 0).")

    def test_current_player_changed(self):
        """
        Test to make sure the current player changes after a move is made.
        """

        game = ChopsticksGame(True)
        moves = game.current_state.get_possible_moves()
        old_player = game.current_state.get_current_player_name()
        new_state = game.current_state.make_move(moves[0])
        new_player = new_state.get_current_player_name()

        self.assertNotEqual(old_player, new_player, "After a move is made " +
                            "the current player returned by " +
                            "get_current_player_name() shoud change.")

    def test_dead_hand_str_0(self):
        """
        Test to make sure a 'dead' hand is represented with '0'.
        """
        game = ChopsticksGame(True)
        new_state = self.apply_moves(game, ["ll", "ll", "ll"])

        value = self.extract_chopsticks_value(new_state)[2]
        self.assertEqual('0', value, ("A dead hand should be represented " +
                                      "by the number 0 but {} was found " +
                                      "instead.").format(value))

    def test_str_to_move_syntactically_valid(self):
        """
        Test to make sure str_to_move can create a move from a syntactically
        valid string that is not a valid move.
        """
        game = ChopsticksGame(True)
        new_state = self.apply_moves(game, ["ll", "ll", "ll"])
        game.current_state = new_state
        move = game.str_to_move("ll")
        move2 = game.str_to_move("rl")
        self.assertEqual(type(move), type(move2),
                         ("Trying to call make_move on a string that is " +
                          "syntactically valid but is not logically valid " +
                          "(e.g. from the string 'll' when the current " +
                          "player's left hand is dead) should return a move " +
                          "that is of the same type as a valid move."))


if __name__ == "__main__":
    unittest.main()

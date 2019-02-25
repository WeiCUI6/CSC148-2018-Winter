"""
A subset of the unittests used for testing Stonehenge.

These unittests only test for basic functionality and whether we can properly
test your code (i.e. you take in the right parameters and your __str__ returns
something that the unittests can understand). They do *not* test your code
extensively.

The sample Stonehenge boards below are a version of the Stonehenge boards that
the unittests can properly read. i.e. The ley-lines and cells are in the right
spots and order; yours **do not** have to be formatted in exactly the same
way.
"""
import unittest
from unittest.mock import patch

# Import the student solution
from game_interface import playable_games
StonehengeGame = playable_games['h']

# Below are some sample Stonehenge boards for use in the unittests
# The extra \s are escape characters so we can print '\' as expected.
# i.e. print(BOARD_LENGTH_1) will give us:
#       @   @
#      /   /
# @ - A - B
#      \ / \
#   @ - C   @
#        \
#         @

BOARD_LENGTH_1 = \
"""\
      @   @
     /   /
@ - A - B
     \\ / \\
  @ - C   @
       \\
        @"""


BOARD_LENGTH_1_OVER = \
"""\
      1   @
     /   /
1 - 1 - B
     \\ / \\
  @ - C   @
       \\
        1"""


BOARD_LENGTH_2 = \
"""\
        @   @
       /   /
  @ - A - B   @
     / \\ / \\ /
@ - C - D - E
     \\ / \\ / \\
  @ - F - G   @
       \\   \\
        @   @"""

BOARD_LENGTH_2_AFTER_A = \
"""\
        1   @
       /   /
  1 - 1 - B   @
     / \\ / \\ /
@ - C - D - E
     \\ / \\ / \\
  @ - F - G   @
       \\   \\
        @   @"""

BOARD_LENGTH_2_AFTER_AG = \
"""\
        1   @
       /   /
  1 - 1 - B   2
     / \\ / \\ /
@ - C - D - E
     \\ / \\ / \\
  2 - F - 2   @
       \\   \\
        @   @"""

BOARD_LENGTH_2_AFTER_AGD = \
"""\
        1   @
       /   /
  1 - 1 - B   2
     / \\ / \\ /
@ - C - 1 - E
     \\ / \\ / \\
  2 - F - 2   @
       \\   \\
        @   1"""

BOARD_LENGTH_2_AFTER_AGDE = \
"""\
        1   @
       /   /
  1 - 1 - B   2
     / \\ / \\ /
@ - C - 1 - 2
     \\ / \\ / \\
  2 - F - 2   2
       \\   \\
        @   1"""

BOARD_LENGTH_2_AFTER_AGDEF = \
"""\
        1   1
       /   /
  1 - 1 - B   2
     / \\ / \\ /
@ - C - 1 - 2
     \\ / \\ / \\
  2 - 1 - 2   2
       \\   \\
        1   1"""


class StonehengeUnitTests(unittest.TestCase):
    def extract_stonehenge_values(self, state=None, board=""):
        """
        Return the ley_lines and cells in a stonehenge state.

        Precondition: At least one of state or board are given a value.
        """
        tokens = []

        # If board is provided; use that. Otherwise, use the str version of
        # the given state.
        if board:
            lines = board.split("\n")
        else:
            lines = str(state).split("\n")

        # Gather all of the tokens in the board
        for line in lines:
            line = line.strip().split()
            current_tokens = []
            for token in line:
                if token.isalpha() or token.isdigit() or token == "@":
                    current_tokens.append(token)

            if current_tokens:
                tokens.append(current_tokens)

        ley_lines = []
        cells = []

        # The first line should consist only of ley-lines
        ley_lines.extend(tokens[0])

        board_size = len(tokens) - 3

        # Go through all of the rows (except the first and last)
        # and collect the ley-line markers and cell values
        for i in range(1, len(tokens) - 1):
            # The first element is a ley-line
            ley_lines.append(tokens[i][0])

            # If the row is not the row with n + 1 cells, then the last token
            # is a ley-line and everything in-between is a cell.
            # Otherwise, everything after the first element is a cell
            if i != board_size:
                ley_lines.append(tokens[i][-1])
                cells.extend(tokens[i][1:-1])
            else:
                cells.extend(tokens[i][1:])

        # The last line consists only of ley-lines
        ley_lines.extend(tokens[-1])

        return (ley_lines, cells)

    # === END OF HELPER FUNCTIONS ===

    @patch('builtins.input', side_effect = ['2'])
    def test_stonehenge_init(self, input):
        """
        Test to make sure Stonehenge can be initialized with a boolean
        parameter and having the correct attributes/methods.
        """
        game = StonehengeGame(True)

        self.assertTrue(isinstance(game, StonehengeGame),
                        ("The game initialized with value 2 should be of " +
                         "type {} (the class mapped to by playable_games['h']" +
                         ") but an object of type {} was returned" +
                         " instead.").format(playable_games['h'].__name__,
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

    @patch('builtins.input', side_effect=['3', 'END'])
    def test_stonehenge_takes_input(self, input):
        """
        Test to make sure Stonehenge can be initialized, taking in a boolean
        as a parameter and requiring a number as input.
        """
        game = StonehengeGame(True)

        actual_patch = input()
        expected_patch = "END"

        self.assertEqual(actual_patch, expected_patch,
                         "When initializing a game of Stonehenge, only one " +
                         "input (e.g. 3) should be taken in.")

    @patch('builtins.input', side_effect=['3'])
    def test_get_current_player_name_true(self, input):
        """
        Test get_current_player_name to ensure it returns "p1" if Stonehenge
        was initialized with True for is_p1_turn.
        """
        game = StonehengeGame(True)
        self.assertEqual('p1', game.current_state.get_current_player_name(),
                         "Calling get_current_player_name() on a game " +
                         "initialized with 'True' as the parameter passed " +
                         "in should return 'p1'.")

    @patch('builtins.input', side_effect=['1'])
    def test_is_over_true(self, input):
        """
        Test is_over to ensure that it returns True when the game is over.
        """
        game = StonehengeGame(True)
        current_state = game.current_state
        current_state = current_state.make_move(game.str_to_move("A"))
        is_over = game.is_over(current_state)
        sample_board = ("      1   @\n     /   /\n1 - 1 - B\n     \\ / \\\n" +
                        "  @ - C   @\n       \\\n        1")
        self.assertTrue(is_over, "is_over() should return True when given " +
                        "a state that is over such as the following board:" +
                        "\n{}".format(sample_board))

    @patch('builtins.input', side_effect=['1'])
    def test_is_winner_p1_true(self, input):
        """
        Test is_winner('p1') to ensure that it returns True when the game is
        over and p1 is the winner.
        """
        game = StonehengeGame(True)
        current_state = game.current_state
        current_state = current_state.make_move(game.str_to_move("A"))
        game.current_state = current_state
        sample_board = ("      1   @\n     /   /\n1 - 1 - B\n     \\ / \\\n" +
                        "  @ - C   @\n       \\\n        1")
        is_winner = game.is_winner("p1")

        self.assertTrue(is_winner,
                        ("Calling is_winner('p1') on a game where p1 " +
                         "won should return True, such as in the" +
                         " board:\n{}").format(sample_board))

    @patch('builtins.input', side_effect=['1'])
    def test_stonehenge_format(self, input):
        """
        Test the str output of Stonehenge's state to make sure we can extract
        the correct tokens.
        """
        game = StonehengeGame(True)
        state_str = str(game.current_state)

        characters_found = []

        # Count the number of valid characters
        for line in state_str.split("\n"):
            line = line.strip().split()
            for ch in line:
                if ch in "@ABC12":
                    characters_found.append(ch)

        self.assertEqual(len(characters_found), 9,
                         ("The string form of a state in Stonehenge that " +
                          "was initialized with a board length of 1 should " +
                          "have 9 symbols in it representing the ley-lines," +
                          " and cells, but {} symbols were found.").format(
                             len(characters_found)
                         ))

        self.assertEqual(characters_found, ['@', '@', '@', 'A', 'B', '@',
                                            'C', '@', '@'],
                         ("From top-to-bottom and left-to-right, the symbols" +
                          " found in a newly initialized game of Stonehenge " +
                          "with a side-length of 1 should be @, @, @, A, B, " +
                          '@, C, @, @, but {} were found instead.').format(
                             characters_found
                         ))

    @patch('builtins.input', side_effect=['1'])
    def test_stonehenge_str(self, input):
        """
        Test the str output of Stonehenge's state to make sure the number
        is extracted correctly.
        """
        game = StonehengeGame(True)
        ley_lines, cells = self.extract_stonehenge_values(game.current_state)
        self.assertTrue(len(ley_lines) == 6 and len(cells) == 3,
                        ("A newly initialized game of Stonehenge should " +
                         "consist of 6 @s (empty ley-lines) and 3 cells " +
                         "labelled A, B, and C. The board:\n{}\nWas returned " +
                         "while the board should look like:\n{}").format(
                            str(game.current_state), BOARD_LENGTH_1)
                        )

        self.assertEqual(ley_lines, ['@', '@', '@', '@', '@', '@'],
                         ("The ley-lines in a newly initialized game of " +
                          "Stonehenge with a side-length of 1 should consist " +
                          "of 6 @s, but {} was found instead.").format(
                             ley_lines)
                         )

        self.assertEqual(cells, ['A', 'B', 'C'],
                         ("The cell letters in a newly initialized game of " +
                          "Stonehenge with a side-length of 1 should be " +
                          "A, B, and C, but {} was found instead.").format(
                             cells)
                         )

    @patch('builtins.input', side_effect=['1'])
    def test_stonehenge_str_one_move(self, input):
        """
        Test the str output of Stonehenge's state to make sure the number
        is extracted correctly after one move is made.
        """
        game = StonehengeGame(True)
        game.current_state = game.current_state.make_move(game.str_to_move("A"))
        ley_lines, cells = self.extract_stonehenge_values(game.current_state)
        expected_ley_lines = ['1', '@', '1', '@', '@', '1']
        self.assertEqual(ley_lines, expected_ley_lines,
                         ("The ley-lines in a newly initialized game of " +
                          "Stonehenge with a side-length of 1 where " +
                          "cell 'A' was taken by Player 1 should be {}" +
                          ", but {} was found instead.").format(
                             expected_ley_lines,
                             ley_lines)
                         )

        self.assertEqual(cells, ['1', 'B', 'C'],
                         ("The cell letters in a newly initialized game of " +
                          "Stonehenge with a side-length of 1 where " +
                          "cell 'A' was taken by Player 1 should be " +
                          "1, B, and C, but {} was found instead.").format(
                             cells)
                         )

    @patch('builtins.input', side_effect=['1'])
    def test_stonehenge_get_possible_moves(self, input):
        """
        Test get_possible_moves() to make sure it returns the correct set
        of moves for Stonehenge with a side length of 1.
        """
        game = StonehengeGame(True)
        moves = game.current_state.get_possible_moves()

        self.assertEqual(3, len(moves),
                         ("get_possible_moves() on a newly initialized " +
                          "game of Stonehenge with a side length of 1 should " +
                          "return 3 moves but " +
                          "{} were returned.").format(len(moves)))

        expected_ley_lines = [["1", "@", "1", "@", "@", "1"],
                              ["@", "1", "1", "@", "1", "@"],
                              ["@", "1", "@", "1", "@", "1"]]

        expected_cells = [["1", "B", "C"],
                          ["A", "1", "C"],
                          ["A", "B", "1"]]

        resulting_ley_lines = []
        resulting_cells = []

        for move in moves:
            new_state = game.current_state.make_move(move)
            lines, cells = self.extract_stonehenge_values(new_state)
            resulting_ley_lines.append(lines)
            resulting_cells.append(cells)

        # Create formatted versions of the expected and resulting values

        str_format = "Ley-lines: {}; Cells: {}"
        formatted_expected = ""
        for i in range(len(expected_ley_lines)):
            formatted_expected += str_format.format(expected_ley_lines[i],
                                                    expected_cells[i]) + "\n"

        formatted_expected = formatted_expected.strip()

        formatted_resulting = ""
        for i in range(len(resulting_ley_lines)):
            formatted_resulting += str_format.format(resulting_ley_lines[i],
                                                     resulting_cells[i]) + "\n"

        formatted_resulting = formatted_resulting.strip()

        # Make sure each of the resulting states can be found in the expected
        # states.
        for i in range(len(expected_ley_lines)):
            lines_to_find = resulting_ley_lines[i]
            cells_to_find = resulting_cells[i]
            found_match = False

            for j in range(len(expected_ley_lines)):
                if (lines_to_find == expected_ley_lines[j]) and \
                        (cells_to_find == expected_cells[j]):
                    found_match = True

            self.assertTrue(found_match,
                            ("The states reachable from a newly initialized " +
                             "game of Stonehenge with side-length 1 should " +
                             "have the following properties:\n{}\nBut the " +
                             "following were found:\n{}").format(
                                formatted_expected,
                                formatted_resulting
                            ))

    @patch('builtins.input', side_effect=['1'])
    def test_get_possible_moves_game_over(self, input):
        """
        Test get_possible_moves() to make sure it returns an empty list for
        a game that is over.
        """
        game = StonehengeGame(True)
        game.current_state = game.current_state.make_move(game.str_to_move("A"))
        moves = game.current_state.get_possible_moves()

        self.assertEqual(len(moves), 0, ("get_possible_moves() on a game of " +
                                         "Stonehenge that is over should " +
                                         "return 0 moves, but instead {} " +
                                         "moves were returned.").format(
            len(moves)))

    @patch('builtins.input', side_effect=['1'])
    def test_stonehenge_make_move(self, input):
        """
        Test make_move() on Stonehenge to make sure it can apply a move and
        correctly return the next state.
        """
        game = StonehengeGame(True)
        moves = game.current_state.get_possible_moves()
        self.assertEqual(len(moves), 3, ("get_possible_moves() on a game of " +
                                         "Stonehenge with a side-length of 1 " +
                                         "should return 3 moves, but instead " +
                                         "{} were returned.").format(len(moves))
                         )

        new_state = game.current_state.make_move(moves[0])

        expected_ley_lines = [["1", "@", "1", "@", "@", "1"],
                              ["@", "1", "1", "@", "1", "@"],
                              ["@", "1", "@", "1", "@", "1"]]

        expected_cells = [["1", "B", "C"],
                          ["A", "1", "C"],
                          ["A", "B", "1"]]

        resulting_ley_lines, resulting_cells = self.extract_stonehenge_values(
            new_state)

        # Create formatted versions of the expected and resulting values

        str_format = "Ley-lines: {}; Cells: {}"
        formatted_expected = ""
        for i in range(len(expected_ley_lines)):
            formatted_expected += str_format.format(expected_ley_lines[i],
                                                    expected_cells[i]) + "\n"

        formatted_expected = formatted_expected.strip()

        formatted_resulting = str_format.format(resulting_ley_lines,
                                                resulting_cells)

        # Make sure each of the resulting states can be found in the expected
        # states.
        found_match = False

        for j in range(len(expected_ley_lines)):
            if (resulting_ley_lines == expected_ley_lines[j]) and \
                    (resulting_cells == expected_cells[j]):
                found_match = True

        self.assertTrue(found_match,
                        ("Applying a move to a newly initialized " +
                         "game of Stonehenge with side-length 1 should " +
                         "result in a state with one of the properties from " +
                         "the following:\n{}\nBut the state formed had the " +
                         "following:\n{}").format(
                            formatted_expected,
                            formatted_resulting
                        ))

    @patch('builtins.input', side_effect=['1'])
    def test_stonehenge_str_to_move(self, input):
        """
        Test str_to_move() to make sure it returns moves that are in the
        moves from get_possible_moves().
        """
        game = StonehengeGame(True)
        moves = game.current_state.get_possible_moves()
        move = game.str_to_move(game.str_to_move("A"))

        self.assertTrue(move in moves, "str_to_move('A') should produce a " +
                        "move that's in get_possible_moves() in a game with " +
                        "a side-length of 1.")

    def test_make_move_keeps_state(self):
        """
        Test make_move() to make sure it doesn't modify the current_state of
        a game.
        """
        with patch('builtins.input', return_value='1'):
            game = StonehengeGame(True)

        original_state = game.current_state

        move_to_make = game.str_to_move("A")
        new_state = game.current_state.make_move(move_to_make)
        after_move_state = game.current_state

        self.assertEqual(original_state, after_move_state,
                         "After calling make_move, the current_state of a " +
                         "game should not be changed.")

    @patch('builtins.input', side_effect=['1'])
    def test_stonehenge_is_valid_move_false(self, input):
        """
        Test is_valid_move() to make sure an invalid move (e.g. '8') is not
        valid.
        """
        game = StonehengeGame(True)
        move = game.str_to_move("D")

        self.assertFalse(game.current_state.is_valid_move(move),
                         "is_valid_move() should return False for a move " +
                         "that is invalid (e.g. 'D' in a game with " +
                         "side-length 1.")

    @patch('builtins.input', side_effect = ['2'])
    def test_stonehenge_to_end(self, input):
        """
        Test to make sure Stonehenge can reach an end state correctly
        through the move sequence A, G, D, E, F
        """
        game = StonehengeGame(True)
        current_state = game.current_state

        self.assertFalse(game.is_over(current_state),
                         "A new game of Stonehenge returned True " +
                         "when .is_over() was called.")

        moves_to_use = ['A', 'G', 'D', 'E', 'F']

        expected_states = [BOARD_LENGTH_2_AFTER_A,
                           BOARD_LENGTH_2_AFTER_AG,
                           BOARD_LENGTH_2_AFTER_AGD,
                           BOARD_LENGTH_2_AFTER_AGDE,
                           BOARD_LENGTH_2_AFTER_AGDEF]

        # Make sure the student solution initialized correctly
        ley_lines, cells = self.extract_stonehenge_values(game.current_state)
        self.assertEqual(ley_lines, ['@' for i in range(9)],
                         ("The ley-lines in a newly initialized game of " +
                          "Stonehenge with a side-length of 2 should consist " +
                          "of 9 @s, but {} was found instead.").format(
                             ley_lines)
                         )

        self.assertEqual(cells, [i for i in "ABCDEFG"],
                         ("The cell letters in a newly initialized game of " +
                          "Stonehenge with a side-length of 1 should be " +
                          "A, B, and C, but {} was found instead.").format(
                             cells)
                         )

        # Apply each move and make sure they match the solution
        moves_used = ''
        for i in range(len(moves_to_use)):
            move = moves_to_use[i]
            moves_used += move
            expected_state = expected_states[i]

            current_state = current_state.make_move(game.str_to_move(move))

            # Make sure str(current_state)'s extracted values match the solution
            ley_lines, cells = self.extract_stonehenge_values(current_state)
            (expected_ley_lines, expected_cells) = \
                self.extract_stonehenge_values(expected_state)

            self.assertEqual(ley_lines, expected_ley_lines,
                             ("The ley-lines reached after applying the moves" +
                              " {} to a game of Stonehenge with a side-length" +
                              " of 2 should be {} but {} were found instead. " +
                              "The str returned looked like:\n{}\nWhile " +
                              "something like this was expected:\n{}").format(
                                 moves_used, expected_ley_lines, ley_lines,
                                 str(current_state), expected_state
                             ))

            self.assertEqual(cells, expected_cells,
                             ("The ley-cells reached after applying the moves" +
                              " {} to a game of Stonehenge with a side-length" +
                              " of 2 should be {} but {} were found instead. " +
                              "The str returned looked like:\n{}\nWhile " +
                              "something like this was expected:\n{}").format(
                                 moves_used, expected_cells, cells,
                                 str(current_state), expected_state
                             ))

    def test_stonehenge_repr_different_players_same_value(self):
        """
        Test to make sure the __repr__ of 2 states that have the same value
        but which have different current_players are different.
        """
        with patch('builtins.input', return_value='2'):
            game_1 = StonehengeGame(True)


        with patch('builtins.input', return_value='2'):
            game_2 = StonehengeGame(False)


        # Apply the moves A -> G to the initial state of game 1 (which starts
        # with player 1)
        game_1_state = game_1.current_state
        game_1_state = game_1_state.make_move(game_1.str_to_move("A"))
        game_1_state = game_1_state.make_move(game_1.str_to_move("G"))


        # Apply the moves G -> A to the initial state of game 2 (which starts
        # with player 2)
        game_2_state = game_2.current_state
        game_2_state = game_2_state.make_move(game_2.str_to_move("G"))
        game_2_state = game_2_state.make_move(game_2.str_to_move("A"))

        self.assertNotEqual(repr(game_1_state), repr(game_2_state),
                            "2 states that have the same values but different" +
                            " players should return different __repr__s.")

    @patch('builtins.input', side_effect = ['2'])
    def test_stonehenge_repr_same_players_same_value(self, input):
        """
        Test to make sure the __repr__ of 2 states that have the same value
        and the same player, but which were reached differently, have the
        same __repr__.
        """
        game = StonehengeGame(True)
        initial_state = game.current_state

        # Apply the moves A -> G -> B to the initial state
        state_1 = initial_state.make_move(game.str_to_move("A"))
        state_1 = state_1.make_move(game.str_to_move("G"))
        state_1 = state_1.make_move(game.str_to_move("B"))

        # Apply the moves B -> G -> A to the initial state
        state_2 = initial_state.make_move(game.str_to_move("B"))
        state_2 = state_2.make_move(game.str_to_move("G"))
        state_2 = state_2.make_move(game.str_to_move("A"))

        self.assertEqual(repr(state_1), repr(state_2),
                         "2 states that have the same values and the same " +
                         "current player but which were reached differently " +
                         "should return the same __repr__.")


    @patch('builtins.input', side_effect = ['1'])
    def test_stonehenge_rough_outcome_state_over(self, input):
        """
        Test to make sure the rough_outcome of a state that's over returns the
        score of the current player (e.g. -1 if the current player lost).
        """
        game = StonehengeGame(True)
        new_state = game.current_state.make_move(game.str_to_move("A"))
        ro = new_state.rough_outcome()

        self.assertEqual(ro, -1,
                         "rough_outcome() should return -1 for a state that " +
                         "is over an where the current player at that state " +
                         "has lost, but {} was returned instead.".format(ro))

    @patch('builtins.input', side_effect = ['2'])
    def test_stonehenge_rough_outcome_winning_move_immediate(self, input):
        """
        Test to make sure the rough_outcome of a state that has a move available
        which can win the game immediately returns 1.
        """
        game = StonehengeGame(True)
        new_state = game.current_state

        moves_to_make = ["A", "B"]
        for move in moves_to_make:
            new_state = new_state.make_move(game.str_to_move(move))

        ro = new_state.rough_outcome()

        self.assertEqual(ro, 1,
                         ("rough_outcome() should return 1 for a state where " +
                          "there is a move that will lead to the the current " +
                          "player winning immediately but {} was returned " +
                          "instead.").format(ro))

    @patch('builtins.input', side_effect = ['2'])
    def test_stonehenge_rough_outcome_other_player_winning_moves(self, input):
        """
        Test to make sure the rough_outcome of a state whose moves will all
        result in states where the other player can immediately win returns -1.
        """
        game = StonehengeGame(True)
        new_state = game.current_state

        moves_to_make = ["D", "A", "C", "E", "G"]
        for move in moves_to_make:
            new_state = new_state.make_move(game.str_to_move(move))

        ro = new_state.rough_outcome()

        self.assertEqual(ro, -1,
                         ("rough_outcome() should return -1 for a state where" +
                          " all moves will result in states where the other " +
                          "player can immediately win but {} was returned " +
                          "instead.").format(ro))

if __name__ == "__main__":
    unittest.main()

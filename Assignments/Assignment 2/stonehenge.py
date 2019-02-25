"""
An implementation of Stonehenge
"""
from math import ceil
from typing import Any
from game import Game
from game_state import GameState


def possible_moves(ley_line_row: list) -> list:
    """
    get the possible moves given current ley line row if the state is not over
    """
    moves = []
    for item in ley_line_row:
        for i in range(1, len(item)):
            if item[i].isalpha():
                moves.append(item[i])
    return moves


def find_who_is_winner(self):
    """
    find who is the winner of the current gamestate
    """
    player1 = 0
    player2 = 0

    for i in range(len(self.ley_line_down_right)):
        if self.ley_line_row[i][0] == '1':
            player1 += 1
        elif self.ley_line_row[i][0] == '2':
            player2 += 1
        if self.ley_line_down_left[i][0] == '1':
            player1 += 1
        elif self.ley_line_down_left[i][0] == '2':
            player2 += 1
        if self.ley_line_down_right[i][-1] == '1':
            player1 += 1
        elif self.ley_line_down_right[i][-1] == '2':
            player2 += 1

    num_of_half_ley_lines = ceil(((self.side_length + 1)*3) / 2)

    winner = 0

    if player1 >= num_of_half_ley_lines:
        if self.p1_turn == 1:
            winner = 1
        else:
            winner = -1
    elif player2 >= num_of_half_ley_lines:
        if self.p1_turn == 1:
            winner = 1
        else:
            winner = -1

    return winner


def get_better(self) -> int:
    """
    find who is the betther one of current gamestate
    """

    player1 = 0
    player2 = 0

    for i in range(len(self.ley_line_down_right)):
        if self.ley_line_row[i][0] == '1':
            player1 += 1
        elif self.ley_line_row[i][0] == '2':
            player2 += 1
        if self.ley_line_down_left[i][0] == '1':
            player1 += 1
        elif self.ley_line_down_left[i][0] == '2':
            player2 += 1
        if self.ley_line_down_right[i][-1] == '1':
            player1 += 1
        elif self.ley_line_down_right[i][-1] == '2':
            player2 += 1

    winner = 0

    if player1 == player2:
        winner = 0
    elif self.p1_turn and player1 > player2 or not self.p1_turn and player1 < \
            player2:
        winner = -1
    elif self.p1_turn and player1 < player2 or not self.p1_turn and player1 > \
            player2:
        winner = 1

    return winner


def check_conquer_for_p1(ley_line: str) -> str:
    """
    check the ley line and
    return the str representation of ley line which already be changed

    >>> ley_line = '@A1'
    >>> check_conquer_for_p1(ley_line)
    '1A1'
    >>> ley_line1 = '@CD1'
    >>> check_conquer_for_p1(ley_line1)
    '@CD1'
    >>> ley_line2 = '@1D1'
    >>> check_conquer_for_p1(ley_line2)
    '11D1'
    """
    number_of_cells = 0
    for char in ley_line:
        if char == '1':
            number_of_cells += 1
    if number_of_cells == ceil((len(ley_line) - 1) / 2):
        index = ley_line.index('@')
        ley_line = ley_line[:index] + '1' + ley_line[index + 1:]
    return ley_line


def check_conquer_for_p2(ley_line: str) -> str:
    """
    check the ley line and
    return the str representation of ley line which already be changed

    >>> ley_line = '@A2'
    >>> check_conquer_for_p2(ley_line)
    '2A2'
    >>> ley_line1 = '@CD2'
    >>> check_conquer_for_p2(ley_line1)
    '@CD2'
    >>> ley_line2 = '@2D2'
    >>> check_conquer_for_p2(ley_line2)
    '22D2'
    """
    number_of_cells = 0
    for char in ley_line:
        if char == '2':
            number_of_cells += 1
    if number_of_cells == ceil((len(ley_line) - 1) / 2):
        index = ley_line.index('@')
        ley_line = ley_line[:index] + '2' + ley_line[index + 1:]
    return ley_line


def help_make_move_row_for_p1(move: Any, ley_line: list) -> list:
    """
    help to make move for game stonehenge

    >>> ley_line_row = ['@AB', '@CDE', '@FGHI', '@JKL']
    >>> move = 'B'
    >>> help_make_move_row_for_p1(move, ley_line_row)
    ['1A1', '@CDE', '@FGHI', '@JKL']
    >>> ley_line_row1 = ['@AB', '@CDE', '@FGHI', '@JKL']
    >>> move = 'E'
    >>> help_make_move_row_for_p1(move, ley_line_row1)
    ['@AB', '@CD1', '@FGHI', '@JKL']
    """
    move = str(move)
    for i in range(len(ley_line)):
        if move in ley_line[i]:
            index = ley_line[i].index(move)
            if ley_line[i][0] != '@':
                temp_str = \
                    ley_line[i][:index] + '1' + \
                    ley_line[i][index + 1:]
                ley_line[i] = temp_str
            else:
                temp_str = ley_line[i][:index] + '1' + ley_line[i][index + 1:]
                temp_str = check_conquer_for_p1(temp_str)
                ley_line[i] = temp_str
    return ley_line


def help_make_move_down_left_for_p1(move: Any, ley_line: list) -> list:
    """
    help to nake move for game stonehenge

    >>> ley_line_down_left = ['@ACF', '@BDGJ', '@EHK', '@IL']
    >>> move = 'B'
    >>> help_make_move_down_left_for_p1(move, ley_line_down_left)
    ['@ACF', '@1DGJ', '@EHK', '@IL']
    >>> ley_line_down_left1 = ['@ACF', '@B1GJ', '@EHK', '@IL']
    >>> move = 'B'
    >>> help_make_move_down_left_for_p1(move, ley_line_down_left1)
    ['@ACF', '111GJ', '@EHK', '@IL']
    """
    move = str(move)
    for i in range(len(ley_line)):
        if move in ley_line[i]:
            index = ley_line[i].index(move)
            if ley_line[i][0] != '@':
                temp_str = \
                    ley_line[i][:index] + '1' + \
                    ley_line[i][index + 1:]
                ley_line[i] = temp_str
            else:
                temp_str = ley_line[i][:index] + '1' + ley_line[i][index + 1:]
                temp_str = check_conquer_for_p1(temp_str)
                ley_line[i] = temp_str
    return ley_line


def make_move_down_right_for_p1(move: Any, ley_line: list) -> list:
    """
    help to nake move for game stonehenge

    >>> ley_line_down_right = ['FJ@', 'CGK@', 'ADHL@', 'BEI@']
    >>> move = 'B'
    >>> make_move_down_right_for_p1(move, ley_line_down_right)
    ['FJ@', 'CGK@', 'ADHL@', '1EI@']
    >>> ley_line_down_right1 = ['FJ@', 'CGK@', 'A1HL@', 'BEI@']
    >>> move = 'A'
    >>> make_move_down_right_for_p1(move, ley_line_down_right1)
    ['FJ@', 'CGK@', '11HL1', 'BEI@']
    """
    move = str(move)
    for i in range(len(ley_line)):
        if move in ley_line[i]:
            index = ley_line[i].index(move)
            if ley_line[i][-1] != '@':
                temp_str = \
                    ley_line[i][:index] + '1' + \
                    ley_line[i][index + 1:]
                ley_line[i] = temp_str
            else:
                temp_str = ley_line[i][:index] + '1' + ley_line[i][index + 1:]
                temp_str = check_conquer_for_p1(temp_str)
                ley_line[i] = temp_str
    return ley_line


def help_make_move_row_for_p2(move: Any, ley_line: list) -> list:
    """
    help to make move for game stonehenge

    >>> ley_line_row = ['@AB', '@CDE', '@FGHI', '@JKL']
    >>> move = 'B'
    >>> help_make_move_row_for_p2(move, ley_line_row)
    ['2A2', '@CDE', '@FGHI', '@JKL']
    >>> ley_line_row1 = ['@AB', '@CDE', '@FGHI', '@2KL']
    >>> move = 'L'
    >>>
    ['@AB', '@CDE', '@FGHI', '22K2']
    >>> ley_line_row2 = ['@AB', '@CDE', '@FGHI', '@2KL']
    >>> move = 'F'
    >>> help_make_move_row_for_p2(move, ley_line_row2)
    ['@AB', '@CDE', '@2GHI', '@2KL']
    """
    move = str(move)
    for i in range(len(ley_line)):
        if move in ley_line[i]:
            index = ley_line[i].index(move)
            if ley_line[i][0] != '@':
                temp_str = \
                    ley_line[i][:index] + '2' + \
                    ley_line[i][index + 1:]
                ley_line[i] = temp_str
            else:
                temp_str = ley_line[i][:index] + '2' + ley_line[i][index + 1:]
                temp_str = check_conquer_for_p2(temp_str)
                ley_line[i] = temp_str
    return ley_line


def help_make_move_down_left_for_p2(move: Any, ley_line: list) -> list:
    """
    help to nake move for game stonehenge

    >>> ley_line_down_left = ['@ACF', '@BDGJ', '@EHK', '@IL']
    >>> move = 'B'
    >>> help_make_move_down_left_for_p2(move, ley_line_down_left)
    ['@ACF', '@2DGJ', '@EHK', '@IL']
    >>> ley_line_down_left1 = ['@ACF', '@B2GJ', '@EHK', '@IL']
    >>> move = 'B'
    >>> help_make_move_down_left_for_p2(move, ley_line_down_left1)
    ['@ACF', '222GJ', '@EHK', '@IL']
    """
    move = str(move)
    for i in range(len(ley_line)):
        if move in ley_line[i]:
            index = ley_line[i].index(move)
            if ley_line[i][0] != '@':
                temp_str = \
                    ley_line[i][:index] + '2' + \
                    ley_line[i][index + 1:]
                ley_line[i] = temp_str
            else:
                temp_str = ley_line[i][:index] + '2' + ley_line[i][index + 1:]
                temp_str = check_conquer_for_p2(temp_str)
                ley_line[i] = temp_str
    return ley_line


def make_move_down_right_for_p2(move: Any, ley_line: list) -> list:
    """
    help to nake move for game stonehenge

    >>> ley_line_down_right = ['FJ@', 'CGK@', 'ADHL@', 'BEI@']
    >>> move = 'B'
    >>> make_move_down_right_for_p2(move, ley_line_down_right)
    ['FJ@', 'CGK@', 'ADHL@', '2EI@']
    >>> ley_line_down_right1 = ['FJ@', 'CGK@', 'A1HL@', 'BEI@']
    >>> move = 'A'
    >>> make_move_down_right_for_p2(move, ley_line_down_right1)
    ['FJ@', 'CGK@', '21HL@', 'BEI@']
    """
    move = str(move)
    for i in range(len(ley_line)):
        if move in ley_line[i]:
            index = ley_line[i].index(move)
            if ley_line[i][-1] != '@':
                temp_str = \
                    ley_line[i][:index] + '2' + \
                    ley_line[i][index + 1:]
                ley_line[i] = temp_str
            else:
                temp_str = ley_line[i][:index] + '2' + ley_line[i][index + 1:]
                temp_str = check_conquer_for_p2(temp_str)
                ley_line[i] = temp_str
    return ley_line


class StoneHenge(Game):
    """
    Abstract class for a game to be played with two players.
    """

    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize this Game, using p1_starts to find who the first player is.

        :param p1_starts: A boolean representing whether Player 1 is the first
                          to make a move.
        :type p1_starts: bool
        """
        side_length = int(input("Enter the side length: "))
        self.current_state = StoneHengeState(p1_starts, side_length)

    def get_instructions(self) -> str:
        """
        Return the instructions for this Game.

        :return: The instructions for this Game.
        :rtype: str
        """
        instructions = "Players take turns claiming cells.When a player " \
                       "captures at least half of the cells in a ley-line," \
                       "then the player captures that ley-line. The first" \
                       "player to capture at least half of the ley-lines" \
                       "is the winner."
        return instructions

    def is_over(self, state) -> bool:
        """
        Return whether or not this game is over.

        :return: True if the game is over, False otherwise.
        :rtype: bool
        """
        winner = find_who_is_winner(state)
        return winner != 0

    def is_winner(self, player: str) -> bool:
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

    def str_to_move(self, string: str):
        """
        Return the move that string represents. If string is not a move,
        return an invalid move.

        :param string:
        :type string:
        :return:
        :rtype:
        """
        if not string.strip().isalpha():
            return -1

        return string.strip()


class StoneHengeState(GameState):
    """
    The state of a game at a certain point in time
    """
    def __init__(self, is_p1_turn: bool, side_length: int) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.

        >>> s1 = StoneHengeState(True, 2)
        >>> s1.p1_turn
        True
        >>> s1.side_length
        2
        >>> s1.ley_line_row
        ['@AB', '@CDE', '@FG']
        >>> s1.ley_line_down_left
        ['@AC', '@BDF', '@EG']
        >>> s1.ley_line_down_right
        ['CF@', 'ADG@', 'BE@']
        >>> s2 = StoneHengeState(False, 3)
        >>> s2.p1_turn
        False
        >>> s2.side_length
        3
        >>> s2.ley_line_row
        ['@AB', '@CDE', '@FGHI', '@JKL']
        >>> s2.ley_line_down_left
        ['@ACF', '@BDGJ', '@EHK', '@IL']
        >>> s2.ley_line_down_right
        ['FJ@', 'CGK@', 'ADHL@', 'BEI@']
        """
        super().__init__(is_p1_turn)
        self.side_length = side_length

        self.ley_line_row = []
        self.ley_line_down_left = []
        self.ley_line_down_right = []

        cells = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                 'Y', 'Z']

        row_numbers = []
        for i in range(side_length + 1):
            temp_num = i + 2
            if i == side_length:
                temp_num = side_length
            row_numbers.append(temp_num)

        # help_generate_ley_line
        index = 0
        help_ley_line1 = []
        for i in range(side_length + 1):
            if i == side_length:
                temp_str = '@' + ' '
                for j in range(row_numbers[i]):
                    temp_str = temp_str + cells[index + j]
                help_ley_line1.append(temp_str)
            else:
                temp_str = '@'
                for j in range(row_numbers[i]):
                    temp_str = temp_str + cells[index + j]
                temp_str = temp_str + (side_length + 1 - row_numbers[i])*' '
                help_ley_line1.append(temp_str)
                index = index + row_numbers[i]

        index = 0
        help_ley_line2 = []
        for i in range(side_length + 1):
            temp_str = '@'
            if i != side_length:
                temp_str = temp_str + (side_length + 1 - row_numbers[i])*' '
                for j in range(row_numbers[i]):
                    temp_str = temp_str + cells[index + j]
                help_ley_line2.append(temp_str)
                index += row_numbers[i]
            else:
                for j in range(row_numbers[i]):
                    temp_str = temp_str + cells[index + j]
                temp_str += ' '
                help_ley_line2.append(temp_str)

        # initialize ley_line_row
        for i in range(len(help_ley_line1)):
            if i == len(help_ley_line1) - 1:
                temp_str = help_ley_line1[i][0] + help_ley_line1[i][2:]
                self.ley_line_row.append(temp_str)
            else:
                self.ley_line_row.append(help_ley_line1[i].strip())

        # initialize ley_line_down_left
        for i in range(side_length + 1):
            temp_str = ''
            for item in help_ley_line1:
                temp_str += item[i + 1]
            temp_str = temp_str.strip()
            temp_str = '@' + temp_str
            self.ley_line_down_left.append(temp_str)

        # initialize ley_line_down_right
        for i in range(side_length + 1):
            temp_str = ''
            for item in help_ley_line2:
                temp_str += item[i + 1]
            temp_str = temp_str.strip()
            temp_str += '@'
            self.ley_line_down_right.append(temp_str)

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        """
        str_ = ''
        for i in range(2):
            str_ += self.ley_line_down_left[i][0]
        str_ += '\n'
        index = 0
        if self.side_length == 1:
            str_ += self.ley_line_row[index]
            str_ += '\n'
            str_ += self.ley_line_row[-1]
            str_ += self.ley_line_down_right[-1][-1]
            str_ += '\n'
            for i in range(len(self.ley_line_down_right) - 1):
                str_ += self.ley_line_down_right[i][-1]
        else:
            for i in range(self.side_length - 1):
                str_ += self.ley_line_row[i]
                str_ += self.ley_line_down_left[i + 2][0]
                str_ += '\n'
                index = i
            str_ += self.ley_line_row[index + 1]
            str_ += '\n'
            str_ += self.ley_line_row[-1]
            str_ += self.ley_line_down_right[-1][-1]
            str_ += '\n'
            for i in range(len(self.ley_line_down_right) - 1):
                str_ += self.ley_line_down_right[i][-1]

        str_list = str_.split('\n')
        str_ = ''
        for item in str_list:
            for i in range(len(item)):
                str_ += item[i]
                str_ += ' '
            str_ += '\n'
        str_ = str_[:len(str_) - 1]
        return str_

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.

        >>> s1 = StoneHengeState(True, 2)
        >>> s1.get_possible_moves()
        ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        >>> s1.ley_line_row = ['11B', '@C2E', '@FG']
        >>> s1.ley_line_down_left = ['11C', '@B2F', '@EG']
        >>> s1.ley_line_down_right = ['CF@', '12G@', 'BE@']
        >>> s1.get_possible_moves()
        ['B', 'C', 'E', 'F', 'G']
        """
        winner = find_who_is_winner(self)
        if winner:
            return []
        else:
            moves = possible_moves(self.ley_line_row)

        return moves

    def make_move(self, move: Any) -> "StoneHengeState":
        """
        Return the GameState that results from applying move to this GameState.

        >>> move = 'B'
        >>> s1 = StoneHengeState(True, 2)
        >>> s2 = s1.make_move(move)
        >>> s2.ley_line_row
        ['1A1', '@CDE', '@FG']
        >>> s2.ley_line_down_left
        ['@AC', '@1DF', '@EG']
        >>> s2.ley_line_down_right
        ['CF@', 'ADG@', '1E1']
        >>> s3 = s2.make_move('D')
        >>> s3.ley_line_row
        ['1A1', '@C2E', '@FG']
        >>> s3.ley_line_down_left
        ['@AC', '@12F', '@EG']
        >>> s3.ley_line_down_right
        ['CF@', 'A2G@', '1E1']
        >>> s4 = s3.make_move('F')
        >>> s4.ley_line_row
        ['1A1', '@C2E', '11G']
        >>> s4.ley_line_down_left
        ['@AC', '1121', '@EG']
        >>> s4.ley_line_down_right
        ['C11', 'A2G@', '1E1']
        """
        p1 = self.p1_turn
        new_ley_line_row = [x for x in self.ley_line_row]
        new_ley_line_down_left = [x for x in self.ley_line_down_left]
        new_ley_line_down_right = [x for x in self.ley_line_down_right]
        if p1:
            new_ley_line_row = help_make_move_row_for_p1(move, new_ley_line_row)
            new_ley_line_down_left = \
                help_make_move_down_left_for_p1(move, new_ley_line_down_left)
            new_ley_line_down_right = \
                make_move_down_right_for_p1(move, new_ley_line_down_right)
            p1 = not p1
        else:
            new_ley_line_row = help_make_move_row_for_p2(move, new_ley_line_row)
            new_ley_line_down_left = \
                help_make_move_down_left_for_p2(move, new_ley_line_down_left)
            new_ley_line_down_right = \
                make_move_down_right_for_p2(move, new_ley_line_down_right)
            p1 = not p1
        new_state = StoneHengeState(p1, self.side_length)
        new_state.ley_line_row = new_ley_line_row
        new_state.ley_line_down_left = new_ley_line_down_left
        new_state.ley_line_down_right = new_ley_line_down_right
        return new_state

    def __repr__(self) -> str:
        """
        Return a representation of this state (which can be used for
        equality testing).
        """
        return "Is_p1_turn: {}, State: {}".format(self.p1_turn, str(self))

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.

        >>> S = StoneHengeState(True, 1)
        >>> S2 = S.make_move('A')
        >>> S2.rough_outcome()
        -1
        """
        winner = find_who_is_winner(self)
        if winner:
            return winner
        moves = self.get_possible_moves()
        for move in moves:
            new_state = self.make_move(move)
            winner = get_better(new_state)
            if winner == 1:
                return self.WIN
        return self.LOSE


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")

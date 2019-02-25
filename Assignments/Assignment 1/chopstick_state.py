"""
subclass of State: ChopstickState
"""
from typing import Any, List
from state import State


class ChopstickState(State):
    """
    subclass of State
    """
    current_list: List

    def __init__(self, is_p1_turn: bool) -> None:
        """
        initialize a new subclass of state: ChopstickState

        >>> is_p1_turn = True
        >>> c1 = ChopstickState(is_p1_turn)
        >>> c1.is_p1_turn
        True
        >>> c1.is_game_over
        False
        >>> c1.current_list
        [1, 1, 1, 1]
        """
        State.__init__(self, is_p1_turn)
        self.current_list = [1, 1, 1, 1]

    def __eq__(self, other: Any) -> bool:
        """
        return whether self is equivalent to other

        >>> is_p1_turn = True
        >>> c1 = ChopstickState(is_p1_turn)
        >>> c2 = ChopstickState(False)
        >>> c3 = 3
        >>> c4 = 'Any'
        >>> c5 = ChopstickState(True)
        >>> c1 == c2
        False
        >>> c1 == c3
        False
        >>> c1 == c4
        False
        >>> c1 == c5
        True
        """
        return (State.__eq__(self, other)
                and self.current_list == other.current_list)

    def __str__(self) -> str:
        """
        return a str representation of game state: ChopstickState

        >>> is_p1_turn = True
        >>> c1 = ChopstickState(is_p1_turn)
        >>> print(c1)
        Player 1: 1 - 1; Player 2: 1 - 1
        """
        return "Player 1: {} - {}; Player 2: {} - {}".\
            format(self.current_list[0], self.current_list[1],
                   self.current_list[2], self.current_list[3])

    def get_possible_moves(self) -> List:
        """
        return a list containing possible moves for the game

        >>> is_p1_turn = True
        >>> c1 = ChopstickState(is_p1_turn)
        >>> c1.get_possible_moves()
        ['ll', 'lr', 'rl', 'rr']
        >>> c1.current_list[1] = 0
        >>> c1.get_possible_moves()
        ['ll', 'lr']
        """
        p1_left, p1_right = self.current_list[0], self.current_list[1]
        p1_list = [p1_left, p1_right]
        p2_left, p2_right = self.current_list[2], self.current_list[3]
        p2_list = [p2_left, p2_right]
        possible_moves = []
        if self.is_p1_turn:
            if p1_list[0] != 0 and p2_list[0] != 0:
                possible_moves.append('ll')
            if p1_list[0] != 0 and p2_list[1] != 0:
                possible_moves.append('lr')
            if p1_list[1] != 0 and p2_list[0] != 0:
                possible_moves.append('rl')
            if p1_list[1] != 0 and p2_list[1] != 0:
                possible_moves.append('rr')
            return possible_moves
        else:
            if p2_list[0] != 0 and p1_list[0] != 0:
                possible_moves.append('ll')
            if p2_list[0] != 0 and p1_list[1] != 0:
                possible_moves.append('lr')
            if p2_list[1] != 0 and p1_list[0] != 0:
                possible_moves.append('rl')
            if p2_list[1] != 0 and p1_list[1] != 0:
                possible_moves.append('rr')
            return possible_moves

    def is_valid_move(self, move_to_take: Any) -> bool:
        """
        return whether a move_to_take is valid for the game

        >>> is_p1_turn = True
        >>> c1 = ChopstickState(is_p1_turn)
        >>> c1.current_list[1] = 0
        >>> c1.is_valid_move(5)
        False
        >>> c1.is_valid_move('Any')
        False
        >>> c1.is_valid_move('rl')
        False
        >>> c1.is_valid_move('ll')
        True
        """
        return move_to_take in self.get_possible_moves()

    def get_current_player_name(self) -> str:
        """
        get current player name

        >>> is_p1_turn = True
        >>> c1 = ChopstickState(is_p1_turn)
        >>> c1.get_current_player_name()
        'p1'
        >>> c1.is_p1_turn = False
        >>> c1.get_current_player_name()
        'p2'
        >>> c2 = ChopstickState(False)
        >>> c2.get_current_player_name()
        'p2'
        """
        return State.get_current_player_name(self)

    def make_move(self, move_to_make: str) -> 'ChopstickState':
        """
        apply the move_to_make and return a new_state

        >>> is_p1_turn = True
        >>> c1 = ChopstickState(is_p1_turn)
        >>> c2 = c1.make_move('ll')
        >>> c2.current_list
        [1, 1, 2, 1]
        >>> c2.get_current_player_name()
        'p2'
        >>> c2.is_game_over
        False
        """
        current_player = self.is_p1_turn
        new_list = [item for item in self.current_list]
        new_is_game_over = self.is_game_over
        if current_player:
            if move_to_make == 'll':
                new_list[2] = new_list[0] + new_list[2]
            elif move_to_make == 'lr':
                new_list[3] = new_list[0] + new_list[3]
            elif move_to_make == 'rl':
                new_list[2] = new_list[1] + new_list[2]
            elif move_to_make == 'rr':
                new_list[3] = new_list[1] + new_list[3]
            if new_list[2] >= 5:
                a = new_list[2]
                new_list[2] = a % 5
            if new_list[3] >= 5:
                b = new_list[3]
                new_list[3] = b % 5
        else:
            if move_to_make == 'll':
                new_list[0] = new_list[2] + new_list[0]
            elif move_to_make == 'lr':
                new_list[1] = new_list[2] + new_list[1]
            elif move_to_make == 'rl':
                new_list[0] = new_list[3] + new_list[0]
            elif move_to_make == 'rr':
                new_list[1] = new_list[3] + new_list[1]
            if new_list[0] >= 5:
                c = new_list[0]
                new_list[0] = c % 5
            if new_list[1] >= 5:
                d = new_list[1]
                new_list[1] = d % 5
        if (new_list[0] == 0 and new_list[1] == 0) or (new_list[2] == 0 and
                                                       new_list[3] == 0):
            new_is_game_over = True
        else:
            if current_player:
                current_player = False
            else:
                current_player = True
        new_state = ChopstickState(current_player)
        new_state.current_list = [item for item in new_list]
        new_state.is_game_over = new_is_game_over
        return new_state


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")

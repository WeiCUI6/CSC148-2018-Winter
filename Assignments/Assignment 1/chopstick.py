"""
module game Chopstick
"""
from typing import Any
from chopstick_state import ChopstickState


class Chopstick:
    """
    class Chopstick
    """
    current_state: ChopstickState

    def __init__(self, is_p1_turn: bool) -> None:
        """
        initialize a new Chopstick game

        >>> is_p1_turn = True
        >>> c1 = Chopstick(is_p1_turn)
        >>> c1.current_state.is_p1_turn
        True
        >>> c1.current_state.is_game_over
        False
        >>> c1.current_state.current_list
        [1, 1, 1, 1]
        """
        self.current_state = ChopstickState(is_p1_turn)

    def __eq__(self, other: Any) -> bool:
        """
        return whether self is equal to other

        >>> is_p1_turn = True
        >>> c1 = Chopstick(is_p1_turn)
        >>> c2 = 3
        >>> c1 == c2
        False
        >>> c3 = 'Any'
        >>> c1 == c3
        False
        >>> c4 = Chopstick(False)
        >>> c1 == c4
        False
        >>> c5 = Chopstick(True)
        >>> c5 == c1
        True
        >>> c5.current_state.current_list = [1 ,0 ,1, 1]
        >>> c5 == c1
        False
        """
        return (type(self) == type(other)
                and self.current_state == other.current_state)

    def __str__(self) -> str:
        """
        return a str representation of game Chopstick

        >>> is_p1_turn = True
        >>> c1 = Chopstick(is_p1_turn)
        >>> print(c1)
        Player 1: 1 - 1; Player 2: 1 - 1
        """
        return self.current_state.__str__()

    def get_instructions(self) -> str:
        """
        return the instruction for the game chopstick

        >>> INSTRUCTION = "Players take turns adding the values of one"
        >>> is_p1_turn = True
        >>> c1 = Chopstick(is_p1_turn)
        >>> c1.get_instructions()[:43] == INSTRUCTION
        True
        """
        instruction = "Players take turns adding the values of one of their" \
                      "hands to one of their opponents(modulo 5). A hand" \
                      "with a total of 5(or 0; 5 modulo 5) is considered" \
                      "'dead'. The first player to have 2 dead hands is" \
                      "the loser."
        return instruction

    def is_over(self, current_state: ChopstickState) -> bool:
        """
        return whether game is over based on current state

        >>> is_p1_turn = True
        >>> c1 = Chopstick(is_p1_turn)
        >>> c2 = ChopstickState(True)
        >>> c1.is_over(c2)
        False
        >>> c2.is_game_over = True
        >>> c1.is_over(c2)
        True
        """
        return current_state.is_game_over

    def str_to_move(self, move_to_take: str) -> str:
        """
        converts a move_to_take into a move

        >>> is_p1_turn = True
        >>> c1 = Chopstick(is_p1_turn)
        >>> c1.str_to_move('ll')
        'll'
        >>> c1.str_to_move('lr')
        'lr'
        """
        return move_to_take

    def is_winner(self, player: str) -> bool:
        """
        return whether player is winner

        >>> is_p1_turn = True
        >>> c1 = Chopstick(is_p1_turn)
        >>> c1.is_winner('p1')
        False
        >>> c1.current_state.is_game_over = True
        >>> c1.is_winner('p1')
        True
        >>> c1.current_state.is_p1_turn = False
        >>> c1.is_winner('p1')
        False
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

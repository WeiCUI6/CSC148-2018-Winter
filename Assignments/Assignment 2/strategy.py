"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any


# TODO: Adjust the type annotation as needed.
def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


# TODO: Implement a recursive version of the minimax strategy.
def helper_recursive(game: Any, state: Any) -> int:
    """
    return one move's score
    """
    game.current_state = state
    if game.is_over(state):
        player = state.get_current_player_name()
        if player == 'p1':
            opposite = 'p2'
        else:
            opposite = 'p1'
        if game.is_winner(player):
            return 1
        elif not game.is_winner(player) and game.is_winner(opposite):
            return -1
        return 0
    else:
        return -1 * min([helper_recursive(game, state.make_move(move))
                         for move in state.get_possible_moves()])


def recursive_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest score for the opponent.
    """
    moves = game.current_state.get_possible_moves()
    current_state = game.current_state
    states = [current_state.make_move(move) for move in moves]
    score_for_move_next_player = [helper_recursive(game, state_)
                                  for state_ in states]
    score_for_move_original_player = [-1 * score
                                      for score in score_for_move_next_player]
    game.current_state = current_state
    if 1 in score_for_move_original_player:
        return moves[score_for_move_original_player.index(1)]
    elif 0 in score_for_move_original_player:
        return moves[score_for_move_original_player.index(0)]
    return moves[0]


# TODO: Implement an iterative version of the minimax strategy.
class StateNode:
    """
    a class tree_like_node to implement iterative strategy

    state - state
    score - score
    children - children
    """
    state: Any
    score: int
    children: list

    def __init__(self, state: Any) -> None:
        """
        initialize a new StateNode
        """
        self.state = state
        self.score = None
        self.children = None

    def __repr__(self) -> str:
        """
        return a str representation of StateNode for evaluating
        """
        return "StateNodeScore: {}, StateNodeChildren: {}, State: {}".\
            format(self.score, self.children, str(self.state))


def iterative_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest score for the opponent.
    """
    current_state = game.current_state
    old_state = game.current_state
    possible_moves = current_state.get_possible_moves()
    original_state_node = StateNode(current_state)
    stack = [original_state_node]
    while stack:
        last_one_pop = stack.pop()
        if game.is_over(last_one_pop.state):
            game.current_state = last_one_pop.state
            player = game.current_state.get_current_player_name()
            if player == 'p1':
                opposite = 'p2'
            else:
                opposite = 'p1'
            if game.is_winner(player):
                last_one_pop.score = 1
            elif not game.is_winner(player) and game.is_winner(opposite):
                last_one_pop.score = -1
            else:
                last_one_pop.score = 0
        else:
            if last_one_pop.children is not None:
                last_one_pop.score = -1 * min([child.score
                                               for child in
                                               last_one_pop.children])
            else:
                last_one_pop.children = [
                    StateNode(last_one_pop.state.make_move(move))
                    for move in last_one_pop.state.get_possible_moves()]
                stack.append(last_one_pop)
                stack.extend(last_one_pop.children)
    game.current_state = old_state
    if last_one_pop.score == 1:
        for child in last_one_pop.children:
            if child.score == -1:
                return possible_moves[last_one_pop.children.index(child)]
    elif last_one_pop.score == 0:
        for child in last_one_pop.children:
            if child.score == 0:
                return possible_moves[last_one_pop.children.index(child)]

    return possible_moves[0]


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")

import unittest
from unittest.mock import patch
from random import randint
from game_state import GameState
import re

# Import the student solution
from game_interface import playable_games
StonehengeGame = playable_games['h']

#############################################
# 注意事项
# 以下这个unittests是一勾CS大课堂X学长学姐帮帮忙给
# 全程班和A2辅导班的同学奉献的福利，请勿分享
# 请尊重我的劳动
# 请你点击run的时候，心里发自肺腑的默念
# I love you Diao sir
# 否则这个文件不工作哟
#############################################


class StonehengeUnitTests(unittest.TestCase):

    def get_tokens(self, state_str):
        everything = [re.sub("[/\- ]", "", x).replace("\\", "") for x in state_str.split("\n")]
        while "" in everything:
            everything.remove("")
        return everything

    def count_char(self, s, charset):
        return len(list(filter(lambda x: x in charset, s)))

    # 以下就是整体检查一下你的str对不对，只考虑1-5长度，你自己肯定也得肉眼再确认一下
    # 我的代码和学校的test一样，只在乎@, 1, 2, A-Z 这些，你的/ - \ 空格都会无视

    @patch('builtins.input', side_effect=['1'])
    def test_stonehenge_str_1(self, input):
        game = StonehengeGame(True)
        first_state = game.current_state
        raw_tokens = self.get_tokens(str(first_state))
        a_tokens = "".join(raw_tokens)
        self.assertTrue(raw_tokens[0] == "@@", "第一行应该永远两个@")
        self.assertTrue(raw_tokens[-1] == "@" * 1, "最后一行应该有1个@")
        self.assertTrue(self.count_char(a_tokens, "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 3, "长度为1的初始游戏应该有3个字母")
        self.assertTrue(self.count_char(a_tokens, "@") == 6, "长度为1的初始游戏应该有6个@")

    @patch('builtins.input', side_effect=['2'])
    def test_stonehenge_str_2(self, input):
        game = StonehengeGame(True)
        first_state = game.current_state
        raw_tokens = self.get_tokens(str(first_state))
        a_tokens = "".join(raw_tokens)
        self.assertTrue(raw_tokens[0] == "@@", "第一行应该永远两个@")
        self.assertTrue(raw_tokens[-1] == "@" * 2, "最后一行应该有2个@")
        self.assertTrue(self.count_char(a_tokens, "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 7, "长度为2的初始游戏应该有7个字母")
        self.assertTrue(self.count_char(a_tokens, "@") == 9, "长度为2的初始游戏应该有9个@")

    @patch('builtins.input', side_effect=['3'])
    def test_stonehenge_str_3(self, input):
        game = StonehengeGame(True)
        first_state = game.current_state
        raw_tokens = self.get_tokens(str(first_state))
        a_tokens = "".join(raw_tokens)
        self.assertTrue(raw_tokens[0] == "@@", "第一行应该永远两个@")
        self.assertTrue(raw_tokens[-1] == "@" * 3, "最后一行应该有3个@")
        self.assertTrue(self.count_char(a_tokens, "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 12, "长度为3的初始游戏应该有12个字母")
        self.assertTrue(self.count_char(a_tokens, "@") == 12, "长度为3的初始游戏应该有12个@")

    @patch('builtins.input', side_effect=['4'])
    def test_stonehenge_str_4(self, input):
        game = StonehengeGame(True)
        first_state = game.current_state
        raw_tokens = self.get_tokens(str(first_state))
        a_tokens = "".join(raw_tokens)
        self.assertTrue(raw_tokens[0] == "@@", "第一行应该永远两个@")
        self.assertTrue(raw_tokens[-1] == "@" * 4, "最后一行应该有4个@")
        self.assertTrue(self.count_char(a_tokens, "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 18, "长度为4的初始游戏应该有18个字母")
        self.assertTrue(self.count_char(a_tokens, "@") == 15, "长度为4的初始游戏应该有15个@")

    @patch('builtins.input', side_effect=['5'])
    def test_stonehenge_str_5(self, input):
        game = StonehengeGame(True)
        first_state = game.current_state
        raw_tokens = self.get_tokens(str(first_state))
        a_tokens = "".join(raw_tokens)
        self.assertTrue(raw_tokens[0] == "@@", "第一行应该永远两个@")
        self.assertTrue(raw_tokens[-1] == "@" * 5, "最后一行应该有5个@")
        self.assertTrue(self.count_char(a_tokens, "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 25, "长度为5的初始游戏应该有25个字母")
        self.assertTrue(self.count_char(a_tokens, "@") == 18, "长度为5的初始游戏应该有18个@")

    # 这个test的目的就是看看你的make_move 首先走一步对不对，同时大概的确保当你make_move以后，新产生的
    # state 必须是一个"deepcopy" 也就是，不能跟以前的list里面share任何一样的东西

    @patch('builtins.input', side_effect=['1'])
    def test_stonehenge_make_move(self, input):
        game = StonehengeGame(True)
        first_state = game.current_state
        a_state = first_state.make_move(game.str_to_move("A"))
        b_state = first_state.make_move(game.str_to_move("B"))
        a_tokens = "".join(self.get_tokens(str(a_state)))
        b_tokens = "".join(self.get_tokens(str(b_state)))
        self.assertTrue(self.count_char(a_tokens, "ABC") == 2, "这个test你要是不过，那说明你make_move根本没写对")
        self.assertTrue(self.count_char(b_tokens, "ABC") == 2, "这个test你要是不过，那说明你make_move里面没有把之前的state里面的数据做一个copy")

    # 这个test是确保一个人占领了ley line以后，无论另外一个玩家如何挣扎都不能易主

    @patch('builtins.input', side_effect=['1'])
    def test_stonehenge_ley_line_ownership(self, input):
        game = StonehengeGame(True)
        first_state = game.current_state
        step1 = first_state.make_move(game.str_to_move("A"))  # p1 走A
        step2 = step1.make_move(game.str_to_move("B"))        # p2 走B
        step1tokens = "".join(self.get_tokens(str(step1)))
        step2tokens = "".join(self.get_tokens(str(step2)))
        self.assertTrue(step1tokens == "1@11B@C@1", "第一步结束以后，P1应该已经占领了3个leyline了")
        self.assertTrue(step2tokens == "12112@C21", "第二步结束以后，P2应该占领了2个，但是以前由P1占领的3个不能易主，如果这个test不过，"
                                                    "那么有可能你是在游戏进行中临时计算的归属，你应该只有在make_move 时候才计算归属")

    # 检查一下get_possible_moves，这个代码会随机的检查一下possible moves

    @patch('builtins.input', side_effect = ['5'])
    def test_stonehenge_possible_moves(self, input):
        game = StonehengeGame(True)

        # 长度为5的游戏，应该一开始有25个选择
        possibles = list("ABCDEFGHIJKLMNOPQRSTUVWXY")
        first_state = game.current_state
        curr_state = first_state
        self.assertTrue(possibles == sorted(first_state.get_possible_moves()), "游戏刚开局，我应该走哪步都可以")
        move_made = []
        while possibles:
            index = randint(0, len(possibles) - 1)
            move = possibles.pop(index)
            curr_state = curr_state.make_move(game.str_to_move(move))
            move_made.append(move)
            if game.is_over(curr_state):
                self.assertTrue(curr_state.get_possible_moves() == [], "游戏已经分出胜负了，get possible moves 应该返回空的了，即使还有地方可以走，虽然不影响你的make_move 工作，只是get_possible_moves应该结束了")
            else:
                self.assertTrue(possibles == sorted(curr_state.get_possible_moves()), "玩家已经走过了{}, 剩下的应该是{}, 但你的possible move是{}".format(move_made, possibles, curr_state.get_possible_moves()))

    # 简单检查一下rough_outcome, 当长度为1的游戏时候，对于p1 来讲，刚开局时候rough_outcome 就应该是个至少>0 的数字

    @patch('builtins.input', side_effect=['1'])
    def test_stonehenge_length1_rough_outcome(self, input):
        game = StonehengeGame(True)

        first_state = game.current_state
        a_state = first_state.make_move(game.str_to_move("A"))
        b_state = first_state.make_move(game.str_to_move("B"))
        c_state = first_state.make_move(game.str_to_move("C"))

        # 注意下面这个test，因为我也不确定你具体怎么实现的，总之这里不可能是< 0的数字，因为你没有任何输的可能
        self.assertTrue(first_state.rough_outcome() >= 0, "长度1的游戏开局，p1你能输就见鬼了")
        # 下面这个三个，不管你怎么实现你的rough outcome，你都应该是-1，因为已经是必输（游戏其实都结束了)
        self.assertTrue(a_state.rough_outcome() == -1, "长度1的游戏p1随便走一步，p2你能赢就见鬼了")
        self.assertTrue(b_state.rough_outcome() == -1, "长度1的游戏p1随便走一步，p2你能赢就见鬼了")
        self.assertTrue(c_state.rough_outcome() == -1, "长度1的游戏p1随便走一步，p2你能赢就见鬼了")


    # 当游戏长度为1的时候，无论谁先走，无论走哪步，游戏都会立刻结束
    # 因为第一个人走完，就直接占了6个ley line中3个了，就没得玩了

    @patch('builtins.input', side_effect = ['1'])
    def test_stonehenge_length1_is_over(self, input):
        game = StonehengeGame(True)

        first_state = game.current_state
        a_state = first_state.make_move(game.str_to_move("A"))
        b_state = first_state.make_move(game.str_to_move("B"))
        c_state = first_state.make_move(game.str_to_move("C"))

        self.assertTrue(not game.is_over(game.current_state), "刚开局，不能结束")
        self.assertTrue(game.is_over(a_state), "走ABC任意一个游戏都应该结束了")
        self.assertTrue(game.is_over(b_state), "走ABC任意一个游戏都应该结束了")
        self.assertTrue(game.is_over(c_state), "走ABC任意一个游戏都应该结束了")
        game.current_state = a_state
        self.assertTrue(game.is_winner("p1"), "获胜的都应该是玩家1")
        game.current_state = b_state
        self.assertTrue(game.is_winner("p1"), "获胜的都应该是玩家1")
        game.current_state = c_state
        self.assertTrue(game.is_winner("p1"), "获胜的都应该是玩家1")


    # 测试一场长度3的游戏
    # 请确保前面的tests都过了

    @patch('builtins.input', side_effect=['3'])
    def test_stonehenge_game_3(self, input):
        game = StonehengeGame(True)

        first_state = game.current_state
        curr_state = first_state

        moves = ['G', 'E', 'J', 'A', 'D', 'L', 'C', 'H', 'I', 'K', 'F']
        expected_progress = ['@@@AB@@CDE@@F1HI@JKL@@@@', '@@@AB@@CD2@@F1HI@JKL@@@@', '@1@AB@@CD2@@F1HI@1KL@1@@', '@122B@@CD2@@F1HI@1KL@1@@', '@122B@@C12@@F1HI@1KL@1@@', '@122B@@C122@F1HI@1K2@1@2', '@122B@11122@F1HI@1K2@112', '@122B211122@F12I@1K2@112', '@122B2111221F121@1K2@112', '@122B2111221F1212122@112', '1122B211122111212122@112']

        my_go = []
        for i in range(len(moves)):
            self.assertTrue(not game.is_winner("p1"), "游戏还没结束，谁都不该赢")
            self.assertTrue(not game.is_winner("p2"), "游戏还没结束，谁都不该赢")
            move = moves[i]
            my_go.append(move)
            curr_state = curr_state.make_move(game.str_to_move(move))
            self.assertTrue(expected_progress[i] == "".join(self.get_tokens(str(curr_state))),
                            "长度3的游戏，进行到第{}步，你的游戏state不太正确，到目前为止双方moves是{}".format(i, my_go))
            game.current_state = curr_state

        self.assertTrue(game.is_winner("p1"), "这场游戏应该是P1获胜")
        self.assertTrue(not game.is_winner("p2"), "这场游戏应该是P1获胜")

    # 测试一场长度为5的较量
    # 激动人心，骇人听闻

    @patch('builtins.input', side_effect=['5'])
    def test_stonehenge_game_5(self, input):
        game = StonehengeGame(True)

        first_state = game.current_state
        curr_state = first_state

        moves = ['A', 'N', 'W', 'E', 'H', 'O', 'L', 'M', 'T', 'U', 'I', 'R', 'F', 'Y', 'V', 'K', 'C', 'G', 'X']
        expected_progress = ['@@11B@@CDE@@FGHI@@JKLMN@@OPQRST@UVWXY@@@@@@', '@@11B@@CDE@@FGHI@@JKLM2@@OPQRST@UVWXY@@@@@@', '@@11B@@CDE@@FGHI@@JKLM2@@OPQRST@UV1XY@@@@@@', '@@11B@@CD2@@FGHI@@JKLM2@@OPQRST@UV1XY@@@@@@', '@@11B@@CD2@@FG1I@@JKLM2@@OPQRST@UV1XY@@@@@@', '@@11B@@CD2@@FG1I@@JKLM2@@2PQRST@UV1XY@2@@@@', '@@11B@@CD2@@FG1I@@JK1M2@@2PQRST@UV1XY@2@@@@', '@@11B@@CD2@@FG1I@@JK122@@2PQRST@UV1XY@2@@@@', '@@11B@@CD2@@FG1I@@JK1221@2PQRS1@UV1XY@2@@@@', '@@11B@@CD2@@FG1I@@JK1221@2PQRS1@2V1XY@2@@@@', '@@11B@@CD211FG11@@JK1221@2PQRS1@2V1XY@2@@@@', '@@11B@@CD211FG11@@JK1221@2PQ2S1@2V1XY@2@@@@', '@@11B@@CD2111G11@@JK1221@2PQ2S1@2V1XY@2@1@@', '@@11B@@CD2111G11@@JK1221@2PQ2S1@2V1X2@2@1@@', '@@11B1@CD2111G11@@JK1221@2PQ2S1@211X2@2@1@@', '@@11B1@CD2111G11@2J21221@2PQ2S1@211X2@2@1@@', '1@11B1@1D2111G11@2J21221@2PQ2S1@211X2@2@1@@', '1211B1@1D2111211@2J21221@2PQ2S1@211X2@2@1@@', '1211B1@1D2111211@2J21221@2PQ2S1121112@2@11@']

        my_go = []
        for i in range(len(moves)):
            move = moves[i]
            my_go.append(move)
            curr_state = curr_state.make_move(game.str_to_move(move))
            self.assertTrue(expected_progress[i] == "".join(self.get_tokens(str(curr_state))),
                            "长度5的游戏，进行到第{}步，你的游戏state不太正确，到目前为止双方moves是{}".format(i, my_go))
            game.current_state = curr_state

        self.assertTrue(game.is_winner("p1"), "这场游戏应该是P1获胜")
        self.assertTrue(not game.is_winner("p2"), "这场游戏应该是P1获胜")

    # 以下这几个tests都没有assertTrue，他们的目的就是把游戏的所有情况都走一遍，看看你程序没有crash就可以

    @patch('builtins.input', side_effect=['1'])
    def test_stonehenge_game_1_all_routes(self, input):
        game = StonehengeGame(True)
        self.c = 0
        first_state = game.current_state
        self.go_over_all_states(game, first_state)

    @patch('builtins.input', side_effect=['2'])
    def test_stonehenge_game_2_all_routes(self, input):
        game = StonehengeGame(True)
        self.c = 0
        first_state = game.current_state
        self.go_over_all_states(game, first_state)

    ###################
    # 以下的3个会运行，很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久
    # 很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久
    # 很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久
    # 很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久
    # 很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久很久
    # 你可以睡觉前让他开始运行
    # 等你起床的时候，要不就是test运行失败了，要不就是完成了, 要不就是你的电脑已经烧掉了
    # 你需要运行的时候uncomment 掉就可以了，请不要三个一起运行....可能一晚上都停不下来
    #
    # 但是如果你一天一夜还不停。。没事。。起码说明没严重错误，就不用非要等到天荒地老了
    # 给你的大概感觉，长度为1的游戏，一共有6种可能性
    # 长度为2的游戏，有5040种可能性
    # 长度为3的，有479,001,600种可能性 (大概需要一晚上运行)
    # 长度为4的，有6.4023737e+15种可能性 （大概需要一年？maybe?）
    # 长度为5的，有1.551121e+25种可能性  (大概需要几辈子???)
    ###################

    # @patch('builtins.input', side_effect=['3'])
    # def test_stonehenge_game_3_all_routes(self, input):
    #     game = StonehengeGame(True)
    #     first_state = game.current_state
    #     self.go_over_all_states(game, first_state)

    # @patch('builtins.input', side_effect=['4'])
    # def test_stonehenge_game_4_all_routes(self, input):
    #     game = StonehengeGame(True)
    #
    #     first_state = game.current_state
    #     self.go_over_all_states(game, first_state)

    # @patch('builtins.input', side_effect=['5'])
    # def test_stonehenge_game_5_all_routes(self, input):
    #    game = StonehengeGame(True)
    #
    #    first_state = game.current_state
    #    self.go_over_all_states(game, first_state)

    def go_over_all_states(self, game: StonehengeGame, state: GameState):
        possibles = state.get_possible_moves()
        if possibles:
            [self.go_over_all_states(game, state.make_move(game.str_to_move(m))) for m in possibles]


if __name__ == "__main__":
    unittest.main()

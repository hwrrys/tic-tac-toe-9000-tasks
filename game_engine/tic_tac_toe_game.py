from copy import deepcopy
from typing import Callable, List, Optional
from .tic_tac_toe_common_lib import TicTacToeTurn, TicTacToeGameInfo, AbstractTicTacToeGame


class TicTacToeGame(AbstractTicTacToeGame):
    """Наследуемся от абстрактного класса и реализуем ручками все методы"""

    def __init__(self, game_id: str, first_player_id: str, second_player_id: str,
                 strategy: Optional[Callable[[TicTacToeGameInfo], TicTacToeTurn]] = None) -> None:
        self.__game_id = game_id
        self.__first_player_id = first_player_id
        self.__second_player_id = second_player_id
        self.__winner_id = ""
        self.__strategy = strategy
        self.__turns: List[TicTacToeTurn] = []

    def is_turn_correct(self, turn: TicTacToeTurn) -> bool:
        if self.__winner_id != "":
            return False

        if self.current_player_id() != turn.player_id:
            return False

        if not (0 <= turn.x_coordinate <= 2 and 0 <= turn.y_coordinate <= 2):
            return False

        return self.get_game_info().field[turn.x_coordinate][turn.y_coordinate] == " "

    def current_player_id(self) -> str:
        if not self.__turns:
            return self.__first_player_id

        if self.__turns[-1].player_id == self.__first_player_id:
            return self.__second_player_id

        return self.__first_player_id

    def do_turn(self, turn: TicTacToeTurn) -> TicTacToeGameInfo:
        if not self.is_turn_correct(turn):
            return self.get_game_info()

        self.__turns.append(deepcopy(turn))
        self._set_winner()

        if self.__winner_id == "" and self.__strategy is not None:
            self.__turns.append(self.__strategy(self.get_game_info()))
            self._set_winner()

        return self.get_game_info()

    def _set_winner(self) -> None:
        if self.__winner_id != "":
            return

        field = self.get_game_info().field

        for i in range(3):
            row1 = []
            row2 = []

            for j in range(3):
                row1.append(field[i][j])
                row2.append(field[j][i])

            if row1 == ["X"] * 3 or row2 == ["X"] * 3:
                self.__winner_id = self.__first_player_id
                return

            if row1 == ["O"] * 3 or row2 == ["O"] * 3:
                self.__winner_id = self.__second_player_id
                return

            if ("X" not in row1) or ("X" not in row2) or ("O" not in row1) or ("O" not in row2):
                draw = False

        row1 = []
        row2 = []
        draw = True

        for i in range(3):
            row1.append(field[i][i])
            row2.append(field[i][2 - i])

        if row1 == ["X"] * 3 or row2 == ["X"] * 3:
            self.__winner_id = self.__first_player_id
            return

        if row1 == ["O"] * 3 or row2 == ["O"] * 3:
            self.__winner_id = self.__second_player_id
            return

        if ("X" not in row1) or ("X" not in row2) or ("O" not in row1) or ("O" not in row2):
            draw = False

        if draw:
            self.__winner_id = "draw"

    def get_game_info(self) -> TicTacToeGameInfo:
        result = TicTacToeGameInfo(
            game_id=self.__game_id,
            field=[
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]
            ],
            sequence_of_turns=deepcopy(self.__turns),
            first_player_id=self.__first_player_id,
            second_player_id=self.__second_player_id,
            winner_id=self.__winner_id
        )
        for turn in self.__turns:
            if turn.player_id == self.__first_player_id:
                symb = "X"
            else:
                symb = "O"
            result.field[turn.x_coordinate][turn.y_coordinate] = symb
        return result

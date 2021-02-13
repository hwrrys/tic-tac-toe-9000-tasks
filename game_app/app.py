from typing import Dict

from game_engine import TicTacToeGame, TicTacToeGameInfo, TicTacToeTurn
from .user_info import UserInfo


class TicTacToeApp:
    def __init__(self):
        """пока не знаю, мб что-то ещё тут будет :)
        в обоих случаях айдишник - ключ, значение - угадайте, что)"""
        self._games: Dict[str, TicTacToeGame] = {}
        self._passwords: Dict[str, str] = {}

    def start_game(self, first_player_id: str, second_player_id: str) -> TicTacToeGameInfo:
        raise NotImplementedError

    def get_game_by_id(self, game_id: str, user_id: str) -> TicTacToeGameInfo:
        raise NotImplementedError

    def do_turn(self, turn: TicTacToeTurn, game_id: str) -> TicTacToeGameInfo:
        raise NotImplementedError

    def add_user(self) -> UserInfo:
        raise NotImplementedError

    def is_autentified(self, user: UserInfo) -> bool:
        raise NotImplementedError

class Board:
    """Класс, который описывает игровое поле."""

    # Размер игрового поля.
    FIELD_SIZE: int = 3

    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]

    def make_move(self, row: int, col: int, player: str):
        """Ставит текущего игрока в нужную ячейку."""
        self.board[row][col] = player

    def is_board_full(self):
        """Проверяет, что поле уже заполнилось(Ничья), или еще нет."""
        for i in range(self.FIELD_SIZE):
            for j in range(self.FIELD_SIZE):
                if self.board[i][j] == '':
                    return False
        return True

    def check_win(self, player):
        """Метод, отвечающий за проверку победителя на игровом поле."""
        # Тут реализована проверка по вертикали и горизонтали.
        for i in range(3):
            if (all([self.board[i][j] == player for j in range(3)]) or
                    all([self.board[j][i] == player for j in range(3)])):
                return True
        # Тут реализована проверка по диагонали.
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == player
            or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True

        return False

    def __str__(self) -> str:
        return (
            f'Игровое поле размером '
            f'{self.FIELD_SIZE}x{self.FIELD_SIZE}'
        )

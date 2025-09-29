import unittest
from unittest.mock import patch

from tic_tac_toe import *

class TestTicTacToe(unittest.TestCase):

    def test_check_winner_horizontal(self):
        """Тест на победу по горизонтали."""
        board = [
            ['X', 'X', 'X'], 
            ['O', 'O', '6'], 
            ['7', '8', '9']
        ]
        self.assertTrue(check_winner(board, 'X'))
        self.assertFalse(check_winner(board, 'O'))

    def test_check_winner_vertical(self):
        """Тест на победу по вертикали."""
        board = [
            ['X', 'O', '3'], 
            ['X', 'O', '6'], 
            ['X', '8', '9']
        ]
        self.assertTrue(check_winner(board, 'X'))
        self.assertFalse(check_winner(board, 'O'))

    def test_check_winner_diagonal(self):
        """Тест на победу по диагонали."""
        board = [
            ['X', 'O', '3'], 
            ['O', 'X', '6'], 
            ['7', '8', 'X']
        ]
        self.assertTrue(check_winner(board, 'X'))
        self.assertFalse(check_winner(board, 'O'))

        board = [
            ['O', 'X', 'X'], 
            ['4', 'O', '6'], 
            ['7', '8', 'O']
        ]
        self.assertTrue(check_winner(board, 'O'))

    def test_check_draw(self):
        """Тест на ничью."""
        # Поле полностью заполнено, и нет победителя
        board = [
            ['X', 'O', 'X'], 
            ['X', 'O', 'O'], 
            ['O', 'X', 'X']
        ]
        self.assertTrue(check_draw(board))

        # Поле не полностью заполнено
        board = [
            ['X', 'O', 'X'], 
            ['X', 'O', '6'], 
            ['O', 'X', 'X']
        ]
        self.assertFalse(check_draw(board))

    def test_get_player_input(self):
        """Тест на ввод пользователя."""
        board = [
            ['X', 'O', '3'], 
            ['4', 'X', '6'], 
            ['7', '8', '9']
        ]

        # Проверяем правильный ход
        input_values = ['3']

        def mock_input(s):
            return input_values.pop(0)

        with patch('builtins.input', mock_input):
            row, col = get_player_input(board, 'O')
            self.assertEqual((row, col), (0, 2)) # Проверяем, что ячейка (0, 2) выбрана

        # Проверяем занятую ячейку
        board[0][2] = 'X'
        input_values = ['2', '9'] # Вводим занятую ячейку и затем правильную

        with patch('builtins.input', mock_input):
            row, col = get_player_input(board, 'O')
            self.assertEqual((row, col), (2, 2)) # Ожидаем (2, 2), так как '9' - корректный выбор

if __name__ == "__main__":
    unittest.main()
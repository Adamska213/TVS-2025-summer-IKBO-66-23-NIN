def draw_board(board):
    """Отображает игровое поле."""
    for row in range(3):
        print(" | ".join(board[row]))
        if row < 2:
            print("-" * 9)

def check_winner(board, player):
    """Проверяет наличие победителя."""
    win_conditions = [
        # Горизонтальные линии
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Вертикальные линии
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Диагональные линии
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    
    for condition in win_conditions:
        if all(board[r][c] == player for r, c in condition):
            return True
    return False

def check_draw(board):
    """Проверяет, заполнено ли всё поле (ничья)."""
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_player_input(board, player):
    """Получает ввод от игрока и проверяет корректность хода."""
    while True:
        try:
            move = int(input(f"Игрок {player}, выберите ячейку (1-9): ")) - 1
            if move < 0 or move >= 9:
                print("Некорректный ввод. Введите число от 1 до 9.")
                continue

            row, col = divmod(move, 3)
            if board[row][col] in ['X', 'O']:
                print("Эта ячейка уже занята. Попробуйте другую.")
            else:
                return row, col
        except ValueError:
            print("Некорректный ввод. Введите число.")

def play_game():
    """Основная функция игры."""
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    current_player = 'X'

    while True:
        draw_board(board)
        row, col = get_player_input(board, current_player)
        board[row][col] = current_player

        if check_winner(board, current_player):
            draw_board(board)
            print(f"Игрок {current_player} победил!")
            break
        elif check_draw(board):
            draw_board(board)
            print("Ничья!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
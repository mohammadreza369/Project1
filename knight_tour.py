# اندازه صفحه شطرنج
N = 6

# حرکات ممکن برای اسب در شطرنج
move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]

# تابع برای بررسی اینکه حرکت در محدوده صفحه شطرنج است یا نه
def is_safe(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

# تابع برای چاپ صفحه شطرنج
def print_solution(board):
    for row in board:
        print(" ".join(f"{cell:2}" for cell in row))

# تابع بازگشتی برای حل مسئله تور اسب
def solve_kt_util(x, y, movei, board):
    if movei == N * N:
        return True

    for i in range(8):
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        if is_safe(next_x, next_y, board):
            board[next_x][next_y] = movei
            if solve_kt_util(next_x, next_y, movei + 1, board):
                return True
            board[next_x][next_y] = -1  # بازگشت به حالت قبلی (Backtracking)

    return False

# تابع اصلی برای حل مسئله تور اسب
def solve_kt():
    # مقداردهی اولیه صفحه شطرنج
    board = [[-1 for _ in range(N)] for _ in range(N)]

    # موقعیت شروع (0, 0)
    start_x, start_y = 0, 0
    board[start_x][start_y] = 0

    if not solve_kt_util(start_x, start_y, 1, board):
        print("Solution does not exist")
        return False
    else:
        print("Solution found:")
        print_solution(board)
        return True

# اجرای حل کننده تور اسب
solve_kt()

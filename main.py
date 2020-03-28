import pygame
# tic tac toe
# [0][1][2]
# [3][4][5]
# [6][7][8]
#
l = 360

board = [
    0, 0, 0,
    0, 0, 0,
    0, 0, 0]

board_pos = [
    (0, 0), (int(l/3), 0), (l-int(l/3), 0),
    (0, int(l/3)), (int(l/3), int(l/3)), (l-int(l/3), int(l/3)),
    (0, l-int(l/3)), (int(l/3), l-int(l/3)), (l-int(l/3), l-int(l/3))]

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((l, l))


def draw_board():
    screen.fill(white)
    pygame.draw.rect(screen, black, ((l / 3), 0, 1, l), 2)
    pygame.draw.rect(screen, black, ((l - (l / 3)), 0, 1, l), 2)
    pygame.draw.rect(screen, black, (0, (l / 3), l, 1), 2)
    pygame.draw.rect(screen, black, (0, (l - (l / 3)), l, 1), 2)


state = 0


def draw_player(u):
    if state == 0:
        pygame.draw.circle(screen, black, (u[0]+int(l/6), u[1]+int(l/6)), int(l/6)-int(l/18), 8)
    elif state == 1:
        pygame.draw.polygon(screen, black, ((u[0], u[1]), (u[0]+int(l/3), u[1]+int(l/3))), 8)
        pygame.draw.polygon(screen, black, ((u[0]+int(l/3), u[1]), (u[0], u[1]+int(l/3))), 8)
    else:
        return


def player_move(z):
    if state == 0:
        draw_player(z)
        next_player()
        return 1
    else:
        draw_player(z)
        next_player()
        return 2


def next_player():
    global state
    if state == 0:
        state = 1
    else:
        state = 0


def mouse_position():
    pos = pygame.mouse.get_pos()
    return pos


def check_win():
    if board[0] == board[1] == board[2]:
        check_player_win(board[0])
    if board[3] == board[4] == board[5]:
        check_player_win(board[3])
    if board[6] == board[7] == board[8]:
        check_player_win(board[6])
    if board[0] == board[4] == board[8]:
        check_player_win(board[0])
    if board[2] == board[4] == board[6]:
        check_player_win(board[2])
    else:
        return


def check_player_win(a):
    if a == 1:
        print("O wins!")
    elif a == 2:
        print("X wins!")
    else:
        return


def restart():
    global board
    global state
    draw_board()
    board = [
        0, 0, 0,
        0, 0, 0,
        0, 0, 0]
    state = 0


def mouse_board():
    pos = mouse_position()
    print(pos)
    # board c3
    if pos[0] > l-int(l/3):
        print("x pos is in board c3")
        if pos[1] > l-int(l/3):
            print("y pos is in board r3")
            z = player_move(board_pos[8])
            board[8] = z
        if int(l/3) < pos[1] < l-int(l/3):
            print("y pos is in board r2")
            z = player_move(board_pos[5])
            board[5] = z
        if pos[1] < int(l/3):
            print("y pos is in board r1")
            z = player_move(board_pos[2])
            board[2] = z
    # board c2
    if int(l/3) < pos[0] < l-int(l/3):
        print("x pos is in board c2")
        if pos[1] > l-int(l/3):
            print("y pos is in board r3")
            z = player_move(board_pos[7])
            board[7] = z
        if int(l/3) < pos[1] < l-int(l/3):
            print("y pos is in board r2")
            z = player_move(board_pos[4])
            board[4] = z
        if pos[1] < int(l/3):
            print("y pos is in board r1")
            z = player_move(board_pos[1])
            board[1] = z
    # board c1
    if pos[0] < int(l/3):
        print("x pos is in board c1")
        if pos[1] > l-int(l/3):
            print("y pos is in board r3")
            z = player_move(board_pos[6])
            board[6] = z
        if int(l/3) < pos[1] < l-int(l/3):
            print("y pos is in board r2")
            z = player_move(board_pos[3])
            board[3] = z
        if pos[1] < int(l/3):
            print("y pos is in board r1")
            z = player_move(board_pos[0])
            board[0] = z
    check_win()


running = True
draw_board()
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                restart()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_board()
            print(state)
            print(board)
exit()

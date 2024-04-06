import pygame

from loadPices import *

width = 736 #736
height = 736
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Chess')
timer = pygame.time.Clock()
fps = 60

turn = 0
selection = 100
valid_moves = []

pygame.init()

def drawBoard():
    # white/black field 92x92
    y = 0
    for i in range(8):
        x = 0
        for j in range(8):
            if (i + j) % 2 == 0:
                screen.blit(white_field, (x, y))
            else:
                screen.blit(black_field, (x, y))
            x += 92
        y += 92

def drawPieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        screen.blit(white_images[index], (white_position[i][0] * 92, white_position[i][1] * 92))
        if turn < 2:
            if selection == i:
                pygame.draw.rect(screen, 'white', [white_position[i][0] * 92, white_position[i][1] * 92, 92, 92], 4)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        screen.blit(black_images[index], (black_position[i][0] * 92, black_position[i][1] * 92))
        if turn >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'white', [black_position[i][0] * 92, black_position[i][1] * 92, 92, 92], 4)

def drawValid(moves):
    transparent_surface = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
    transparent_surface.fill((0, 0, 0, 0))

    for move in moves:
        pygame.draw.circle(transparent_surface, (0, 0, 0, 64), (move[0] * 92 + 46, move[1] * 92 + 46), 15)
    screen.blit(transparent_surface, (0, 0))


def check_options(pieces, positions, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        position = positions[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = checkPawn(position, turn)
        elif piece == 'rook':
            moves_list = checkRook(position, turn)
        elif piece == 'knight':
            moves_list = checkKnight(position, turn)
        elif piece == 'bishop':
            moves_list = checkBishop(position, turn)
        elif piece == 'queen':
            moves_list = checkQueen(position, turn)
        elif piece == 'king':
            moves_list = checkKing(position, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

def checkPawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] - 1) not in white_position and (position[0], position[1] - 1) not in black_position and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_position and (position[0], position[1] - 2) not in black_position and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] - 1, position[1] - 1) in black_position:
            moves_list.append((position[0] - 1, position[1] - 1))
        if (position[0] + 1, position[1] - 1) in black_position:
            moves_list.append((position[0] + 1, position[1] - 1))
    else:
        if (position[0], position[1] + 1) not in white_position and (position[0], position[1] + 1) not in black_position and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_position and (position[0], position[1] + 2) not in black_position and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] - 1, position[1] + 1) in white_position:
            moves_list.append((position[0] - 1, position[1] + 1))
        if (position[0] + 1, position[1] + 1) in white_position:
            moves_list.append((position[0] + 1, position[1] + 1))
    return moves_list

def checkRook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_position
        friends_list = white_position
    else:
        enemies_list = white_position
        friends_list = black_position
    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def checkKnight(position, color):
    moves_list = []
    if color == 'white':
        friends_list = white_position
    else:
        friends_list = black_position
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

def checkBishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_position
        friends_list = white_position
    else:
        friends_list = black_position
        enemies_list = white_position
    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def checkQueen(position, color):
    moves_list = checkBishop(position, color)
    second_list = checkRook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list

def checkKing(position, color):
    moves_list = []
    if color == 'white':
        friends_list = white_position
    else:
        friends_list = black_position
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

def checkValidMoves():
    if turn < 2:
        options_list = white_options
    else:
        options_list = black_options
    return options_list[selection]

def drawCheck():
    if turn < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_position[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if flasher < 15:
                        pygame.draw.rect(screen, 'dark red', [white_position[king_index][0] * 92, white_position[king_index][1] * 92, 92, 92], 5)
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_position[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if flasher < 15:
                        pygame.draw.rect(screen, 'dark red', [black_position[king_index][0] * 92, black_position[king_index][1] * 92, 92, 92], 5)

def drawGameover():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    font = pygame.font.SysFont(None, 36)
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))

black_options = check_options(black_pieces, black_position, 'black')
white_options = check_options(white_pieces, white_position, 'white')

flasher = 0
winner = ''
gameover = False
run = True
while run:
    timer.tick(fps)
    if flasher < 30:
        flasher += 1
    else:
        flasher = 0
    screen.fill('black')
    drawBoard()
    drawPieces()
    drawCheck()
    if selection != 100:
        valid_moves = checkValidMoves()
        drawValid(valid_moves)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not gameover:
            click_coords = (event.pos[0] // 92, event.pos[1] // 92)

            # white turn
            if turn <= 1:
                if click_coords in white_position:
                    selection = white_position.index(click_coords)
                    if turn == 0:
                        turn = 1
                if click_coords in valid_moves and selection != 100:
                    white_position[selection] = click_coords
                    if click_coords in black_position:
                        black_piece = black_position.index(click_coords)
                        # captured_pieces_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_position.pop(black_piece)
                    black_options = check_options(black_pieces, black_position, 'black')
                    white_options = check_options(white_pieces, white_position, 'white')
                    turn = 2
                    selection = 100
                    valid_moves = []

            # black turn
            if turn > 1:
                if click_coords in black_position:
                    selection = black_position.index(click_coords)
                    if turn == 2:
                        turn = 3
                if click_coords in valid_moves and selection != 100:
                    black_position[selection] = click_coords
                    if click_coords in white_position:
                        white_piece = white_position.index(click_coords)
                        # captured_pieces_white.append(black_pieces[black_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                        white_pieces.pop(white_piece)
                        white_position.pop(white_piece)
                    black_options = check_options(black_pieces, black_position, 'black')
                    white_options = check_options(white_pieces, white_position, 'white')
                    turn = 0
                    selection = 100
                    valid_moves = []
        if event.type == pygame.KEYDOWN and gameover:
            if event.key == pygame.K_RETURN:
                gameover = False
                winner = ''
                white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                white_position = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                  (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                black_position = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                  (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                turn = 0
                selection = 100
                valid_moves = []
                black_options = check_options(black_pieces, black_position, 'black')
                white_options = check_options(white_pieces, white_position, 'white')
    if winner != '':
        gameover = True
        drawGameover()
    pygame.display.flip()
pygame.quit()
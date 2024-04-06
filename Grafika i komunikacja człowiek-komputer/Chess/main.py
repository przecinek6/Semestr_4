from loadPices import *

width = 740 #736
height = 740
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
            moves_list = check_pawn(position, turn)
        # elif piece == 'rook':
        #     moves_list = check_rook(position, turn)
        # elif piece == 'knight':
        #     moves_list = check_knight(position, turn)
        # elif piece == 'bishop':
        #     moves_list = check_bishop(position, turn)
        # elif piece == 'queen':
        #     moves_list = check_queen(position, turn)
        # elif piece == 'king':
        #     moves_list = check_king(position, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

def check_pawn(position, color):
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


def checkValidMoves():
    if turn < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

black_options = check_options(black_pieces, black_position, 'black')
white_options = check_options(white_pieces, white_position, 'white')

run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    drawBoard()
    drawPieces()
    if selection != 100:
        valid_moves = checkValidMoves()
        drawValid(valid_moves)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # x_mouse = event.pos[0] // 92
            # y_mouse = event.pos[1] // 92
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
                        white_pieces.pop(white_piece)
                        white_position.pop(white_piece)
                    black_options = check_options(black_pieces, black_position, 'black')
                    white_options = check_options(white_pieces, white_position, 'white')
                    turn = 0
                    selection = 100
                    valid_moves = []


    pygame.display.flip()
pygame.quit()
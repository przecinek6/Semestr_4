import pygame

white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_position = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_position = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

black_queen = pygame.image.load('assets/black/queen.png')
black_king = pygame.image.load('assets/black/king.png')
black_bishop = pygame.image.load('assets/black/bishop.png')
black_knight = pygame.image.load('assets/black/knight.png')
black_rook = pygame.image.load('assets/black/rook.png')
black_pawn = pygame.image.load('assets/black/pawn.png')

white_queen = pygame.image.load('assets/white/queen.png')
white_king = pygame.image.load('assets/white/king.png')
white_bishop = pygame.image.load('assets/white/bishop.png')
white_knight = pygame.image.load('assets/white/knight.png')
white_rook = pygame.image.load('assets/white/rook.png')
white_pawn = pygame.image.load('assets/white/pawn.png')

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

white_field = pygame.image.load('assets/white_field.png')
black_field = pygame.image.load('assets/black_field.png')
import pygame

#white/black field 92x92

pygame.init()

width = 740 #736
height = 740
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Chess')
timer = pygame.time.Clock()
fps = 60

run = True
while run:
    timer.tick(fps)
    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
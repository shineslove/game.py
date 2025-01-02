import sys
import pygame

from pygame.locals import QUIT

pygame.init()

FPS = 30
SCREEN_SIZE = 500
SCREEN_OFFSET = 1.55
SCREEN_WIDTH = SCREEN_SIZE * SCREEN_OFFSET
SCREEN_HEIGHT = SCREEN_SIZE * SCREEN_OFFSET

WOODBROWN = (198, 152, 116)

WHITE = (255, 255, 255)

DISPLAYSCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

DISPLAYSCREEN.fill(WOODBROWN)

pygame.display.set_caption("Gungi")

frames = pygame.time.Clock()

SIZE = 50
OFFSET = 10
UPSCALE = 1.5
DIMENSION = 9

while True:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            pygame.quit()
            sys.exit()
    x, y = OFFSET, OFFSET
    width, height = SIZE * UPSCALE, SIZE * UPSCALE
    for row in range(DIMENSION):
        for cell in range(DIMENSION):
            pygame.draw.rect(
                DISPLAYSCREEN,
                WHITE,
                (x + row * (width + OFFSET), y + cell * (width + OFFSET), width, height),
            )
    pygame.display.update()
    frames.tick(FPS)

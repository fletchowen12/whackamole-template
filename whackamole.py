import pygame
import random

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        color = "dark green"
        running = True
        molex = 0
        moley = 0

        screen.fill("light green")
        for i in range(1, 20):
            pygame.draw.line(screen, color, (0, i * 32), (640, i * 32))
        for i in range(1, 36):
            pygame.draw.line(screen, color, (i * 32, 0), (i * 32, 512))
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))


        while running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = x // 32
                    col = y // 32
                    if row == molex//32 and col == moley//32:
                        molex = random.randint(0,19) * 32
                        moley = random.randint(0,15) * 32
                        screen.fill("light green")
                        for i in range(1, 20):
                            pygame.draw.line(screen, color, (0, i * 32), (640, i * 32))
                        for i in range(1, 36):
                            pygame.draw.line(screen, color, (i * 32, 0), (i * 32, 512))
                        screen.blit(mole_image, mole_image.get_rect(topleft=(molex, moley)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()


import pygame
import random
import sys
import math

WIDTH, HEIGHT = 1200, 700
BACKGROUND_COLOR = (11, 11, 11)
FPS = 60

class Square:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.speed = random.uniform(0.5, 2)
        self.alpha = 255
        self.angle = 0

    def move(self):
        self.y -= self.speed
        self.alpha -= 0.5
        if self.alpha < 0:
            self.alpha = 0
        self.angle += 2

    def draw(self, screen):
        square_surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.rect(square_surface, (*self.color, self.alpha), (0, 0, self.size, self.size), border_radius=15)
        rotated_surface = pygame.transform.rotate(square_surface, self.angle)
        new_rect = rotated_surface.get_rect(center=(self.x + self.size / 2, self.y + self.size / 2))
        screen.blit(rotated_surface, new_rect.topleft)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Летающие квадратики")
    clock = pygame.time.Clock()
    squares = []

    pygame.time.set_timer(pygame.USEREVENT, 500)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.USEREVENT:
                size = random.randint(20, 80)
                x = random.randint(0, WIDTH - size)
                squares.append(Square(x, HEIGHT, size))

        screen.fill(BACKGROUND_COLOR)

        for square in squares:
            square.move()
            square.draw(screen)

        squares = [square for square in squares if square.alpha > 0]

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DVD Screensaver")

# Colors
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255),
          (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Load or create the logo
logo_width, logo_height = 100, 50
logo_surface = pygame.Surface((logo_width, logo_height), pygame.SRCALPHA)
logo_color = random.choice(colors)
pygame.draw.rect(logo_surface, logo_color, logo_surface.get_rect(), border_radius=10)

# Initial position and velocity
x, y = random.randint(0, WIDTH - logo_width), random.randint(0, HEIGHT - logo_height)
dx, dy = 3, 3  # speed

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((0, 0, 0))  # Black background
    screen.blit(logo_surface, (x, y))

    # Move the logo
    x += dx
    y += dy

    # Bounce and change color
    if x <= 0 or x + logo_width >= WIDTH:
        dx *= -1
        logo_color = random.choice(colors)
        pygame.draw.rect(logo_surface, logo_color, logo_surface.get_rect(), border_radius=10)

    if y <= 0 or y + logo_height >= HEIGHT:
        dy *= -1
        logo_color = random.choice(colors)
        pygame.draw.rect(logo_surface, logo_color, logo_surface.get_rect(), border_radius=10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)  # 60 frames per second

pygame.quit()

import pygame
import random

pygame.init()

# Fullscreen settings
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("DVD Screensaver")

# Load image
logo_image = pygame.image.load("images.png")
logo_width, logo_height = logo_image.get_size()

# Scale image 
max_width, max_height = 150, 100
if logo_width != max_width or logo_height != max_height:
    logo_image = pygame.transform.scale(logo_image, (max_width, max_height))
    logo_width, logo_height = logo_image.get_size()

# Initial position and speed
x = random.randint(0, WIDTH - logo_width)
y = random.randint(0, HEIGHT - logo_height)

clock = pygame.time.Clock()
running = True

# Bounce logic
def bounce():
    return random.choice([-1, 1])

dx = 3 * bounce()  
dy = 3 * bounce()  

while running:
    screen.fill((0, 0, 0))
    screen.blit(logo_image, (x, y))

    x += dx
    y += dy

    # Bounce on walls
    if x <= 0 or x + logo_width >= WIDTH:
        dx *= -1
        logo_image = pygame.transform.rotate(logo_image, 0)  

    if y <= 0 or y + logo_height >= HEIGHT:
        dy *= -1
        logo_image = pygame.transform.rotate(logo_image, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
           (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

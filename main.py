import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Игра Тир')
icon = pygame.image.load('img/Тир.jpg')
pygame.display.set_icon(icon)

target_image = pygame.image.load('img/target.png')
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_dx = random.randint(-3, 3)
target_dy = random.randint(-3, 3)
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

score = 0
font = pygame.font.Font(None, 36)

running = True
clock = pygame.time.Clock()
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    target_x += target_dx
    target_y += target_dy
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_dx = -target_dx
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_dy = -target_dy

    text = font.render("Счет: {}".format(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    screen.blit(target_image, (target_x, target_y))
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()


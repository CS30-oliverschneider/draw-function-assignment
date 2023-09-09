import pygame
import sys
import math
import random

pygame.init()

displaySize = (800, 800)
surface = pygame.display.set_mode(displaySize)
mousedown = "up"
flowerNum = 200

def draw_flower(center_coords, radius, petal_num, center_color, petal_color):
    for n in range(petal_num):
        length = radius * 2.5
        width = (0.066 * petal_num + 1) * (2 * math.pi * radius) / petal_num
        draw_angled_ellipse(center_coords, (length, width), petal_color, n * 360 / petal_num, 0)

    pygame.draw.circle(surface, center_color, center_coords, radius)

def draw_angled_ellipse(pivot, size, color, angle, offset):
    ellipse_surface = pygame.Surface(size, pygame.SRCALPHA)
    pygame.draw.ellipse(ellipse_surface, color, (0, 0, *size))
    offset_vector = pygame.math.Vector2(size[0] / 2 + offset, 0)

    rotated_offset = offset_vector.rotate(-angle)
    rotated_ellipse = pygame.transform.rotate(ellipse_surface, angle)
    
    surface.blit(rotated_ellipse, rotated_ellipse.get_rect(center = pivot + rotated_offset))

def draw_random_flowers():
    pygame.draw.rect(surface, (255, 255, 255), (0, 0, *displaySize))

    for _ in range(flowerNum):
        random_center_coords = (random.randrange(displaySize[0]), random.randrange(displaySize[1]))
        random_center_radius = random.randrange(10, 31)
        random_petalNum = random.randrange(3, 31)
        random_center_color = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
        random_petal_color = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))

        draw_flower(random_center_coords, random_center_radius, random_petalNum, random_center_color, random_petal_color)
        pygame.display.flip()

draw_random_flowers()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_pressed()[0]:
        if mouse == "up":
            mouse = "click"
        else:
            mouse = "down"
    else:
        mouse = "up"

    if mouse == "click":
        draw_random_flowers()

pygame.quit()
sys.exit()

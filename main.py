import os
import sys
import pygame


def load_image(name):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"File with image '{fullname}' not found.")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


running = True
px = 20
chpx = 0
chpy = 0
py = 20
ex = 1600
ey = 900
gx = 0.0
gy = 0.0
screen = pygame.display.set_mode((ex, ey))
pygame.init()
car = load_image('lada0.png')
car = pygame.transform.scale(car, (100, 200))
car0 = car
car45 = pygame.transform.rotate(car, 45)
car90 = pygame.transform.rotate(car, 90)
car135 = pygame.transform.rotate(car, 135)
car180 = pygame.transform.rotate(car, 180)
car225 = pygame.transform.rotate(car, 225)
car270 = pygame.transform.rotate(car, 270)
car315 = pygame.transform.rotate(car, 315)
ice_fon = load_image('ice_main.png')
ice_fon = pygame.transform.scale(ice_fon, (1920, 1080))
menu = load_image('start_menu.png')
menu = pygame.transform.scale(menu, (1920, 1080))
first_launch = True
up = False
down = False
left = False
right = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                up = True
            if event.key == pygame.K_d:
                right = True
            if event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_s:
                down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                up = False
            if event.key == pygame.K_d:
                right = False
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_s:
                down = False
    if first_launch:
        screen.blit(menu, (0, 0))
        screen.blit(car90, (px, py))
        first_launch = False
    chpx += 0.25*(int(right)-int(left))
    gx += (int(right)-int(left))*0.05
    chpy += 0.25*(int(down)-int(up))
    gy += (int(down)-int(up))*0.05

    if chpx + int(gx / 0.1) > 0 and chpy + int(gy / 0.1) > 0:
        screen.blit(ice_fon, (0, 0))
        screen.blit(car45, (px, py))

    elif chpx + int(gx / 0.1) > 0 and chpy == 0:
        screen.blit(ice_fon, (0, 0))
        screen.blit(car90, (px, py))

    elif chpy + int(gy / 0.1) < 0 < chpx + int(gx / 0.1):
        screen.blit(ice_fon, (0, 0))
        screen.blit(car135, (px, py))

    elif chpx == 0 and chpy + int(gy / 0.1) < 0:
        screen.blit(ice_fon, (0, 0))
        screen.blit(car180, (px, py))

    elif chpx + int(gx / 0.1) < 0 and chpy + int(gy / 0.1) < 0:
        screen.blit(ice_fon, (0, 0))
        screen.blit(car225, (px, py))

    elif chpx + int(gx / 0.1) < 0 and chpy == 0:
        screen.blit(ice_fon, (0, 0))
        screen.blit(car270, (px, py))

    elif chpx + int(gx / 0.1) < 0 < chpy + int(gy / 0.1):
        screen.blit(ice_fon, (0, 0))
        screen.blit(car315, (px, py))

    elif chpx == 0 and chpy + int(gy / 0.1) > 0:
        screen.blit(ice_fon, (0, 0))
        screen.blit(car0, (px, py))

    if chpx + gx >= 1 or chpx + gx <= -1:
        if 10 <= px <= ex - 80:
            px += int(chpx + gx)
            chpx = 0
        elif px < 10 and int(chpx + gx) > 0:
            px += int(chpx + gx)
            chpx = 0
        elif px > ex - 80 and int(chpx + gx) < 0:
            px += int(chpx + gx)
            chpx = 0
    if chpy + gy >= 1 or chpy + gy <= -1:
        if 10 <= py <= ey - 80:
            py += int(chpy + gy)
            chpy = 0
        elif py < 10 and int(chpy + gy) > 0:
            py += int(chpy + gy)
            chpy = 0
        elif py > ey - 80 and int(chpy + gy) < 0:
            py += int(chpy + gy)
            chpy = 0

    if not up and not down:
        chpy = 0
    if not left and not right:
        chpx = 0

    if gx > 0.05:
        gx -= 0.04
    elif gx < -0.05:
        gx += 0.04
    else:
        gx *= 0.95

    if gy > 0.05:
        gy -= 0.04
    elif gy < -0.05:
        gy += 0.04
    else:
        gy *= 0.95
    pygame.display.flip()

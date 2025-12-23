import pygame
from random import randint

pygame.init()

window_width = 640
window_height = 480
screen = pygame.display.set_mode((window_width, window_height))

robot = pygame.image.load("robot.png")

robots = []
for i in range(20):
    robots.append([-1000, window_height])

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    for i in range(20):
        if robots[i][1] + robot.get_height() < window_height:
            robots[i][1] += 1
        else:
            if robots[i][0] < -robot.get_width() or robots[i][0] > window_width:
                robots[i][0] = randint(0, window_width - robot.get_width())
                robots[i][1] = -randint(100, 1000)
            elif robots[i][0] + robot.get_width() / 2 < window_width / 2:
                robots[i][0] -= 1
            else:
                robots[i][0] += 1

    screen.fill((0, 0, 0))

    for i in range(20):
        screen.blit(robot, (robots[i][0], robots[i][1]))

    pygame.display.flip()

    clock.tick(60)


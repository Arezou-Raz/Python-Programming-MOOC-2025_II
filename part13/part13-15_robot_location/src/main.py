import pygame
import random

pygame.init()

window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

def get_random_position():
    x = random.randint(0, window_width - robot_width)
    y = random.randint(0, window_height - robot_height)
    return x, y

x, y = get_random_position()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            # Check if the mouse click is within the bounds of the robot image
            if x <= mouse_x <= x + robot_width and y <= mouse_y <= y + robot_height:
                x, y = get_random_position()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))

    pygame.display.flip()

    clock.tick(60)

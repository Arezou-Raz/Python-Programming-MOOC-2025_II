import pygame

pygame.init()

window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    mouse_x, mouse_y = pygame.mouse.get_pos()

    x = mouse_x - robot_width // 2
    y = mouse_y - robot_height // 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))

    pygame.display.flip()

    clock.tick(60)

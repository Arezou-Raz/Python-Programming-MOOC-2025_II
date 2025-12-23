import pygame
from random import randint

pygame.init()

window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Asteroids")

font = pygame.font.SysFont("Arial", 22)
BLACK = (0, 0, 0)

rock = pygame.image.load("rock.png")
robot = pygame.image.load("robot.png")

x = start_x = window.get_width() // 2 - robot.get_width() / 2
y = start_y = 480 - robot.get_height()
score = 0
rocks = []

to_right = False
to_left = False

clock = pygame.time.Clock()

game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

    if not game_over:
        if to_right and x <= 640 - robot.get_width():
            x += 5
        if to_left and x > 0:
            x -= 5

        if randint(1, 100) == 1:
            rock_x = randint(0, 640 - rock.get_width())
            rock_y = 0 - rock.get_height()
            rocks.append((rock_x, rock_y))

        window.fill(BLACK)

        for i, (rock_x, rock_y) in enumerate(rocks):
            rock_y += 1
            rocks[i] = (rock_x, rock_y)

            robot_rectangle = robot.get_rect(topleft=(x, y))
            rock_rectangle = rock.get_rect(topleft=(rock_x, rock_y))

            if robot_rectangle.colliderect(rock_rectangle):
                del rocks[i]
                score += 1
            elif rock_y >= 480 - rock.get_height():
                game_over = True

            window.blit(rock, (rock_x, rock_y))

        window.blit(robot, (x, y))
        text = font.render(f"Score: {score}", True, (255, 0, 0))
        window.blit(text, (550, 10))

    else:
        window.fill(BLACK)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        final_score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
        window.blit(game_over_text, (640 // 2 - game_over_text.get_width() // 2, 480 // 2 - 24))
        window.blit(final_score_text, (640 // 2 - final_score_text.get_width() // 2, 480 // 2 + 24))

    pygame.display.flip()
    clock.tick(60)
